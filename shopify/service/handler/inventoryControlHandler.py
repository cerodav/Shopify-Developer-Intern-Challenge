from shopify.logger.logger import logger
from shopify.service.cache.inventoryCache import InventoryResponseCache
from shopify.service.handler.baseHandler import BaseHandler
from shopify.db.helper.inventoryDAOHelper import InventoryTableDA0Helper
from shopify.db.helper.undeleteDAOHelper import UndeleteDAOHelper
from shopify.service.type.types import ResponseType

class InventoryControlHandler(BaseHandler):

    inventoryCache = InventoryResponseCache()

    async def get(self, slug=None):
        logger.info('[GET] Request - {}'.format(self.request.path))
        slug = slug.upper()
        try:
            if slug == 'LIST':
                response, state = self.getAll()
            elif slug == 'UNDELETELIST':
                response, state = self.getAllUndelete()
            else:
                raise Exception('Unknow request received: {}'.format(slug))
            self.send_response(response, state)
            logger.info('[GET] Response - {}'.format(self.request.path))
        except Exception as e:
            logger.exception(e)
            self.throwError()

    async def post(self, slug=None):
        logger.info('[POST] Request - {}'.format(self.request.path))
        slug = slug.upper()
        try:
            if slug == 'CREATE':
                response, state = self.createItem()
            elif slug == 'UPDATE':
                response, state = self.updateItem()
            elif slug == 'DELETE':
                response, state = self.deleteItem()
            elif slug == 'UNDELETE':
                response, state = self.undeleteItem()
            self.redirect('/?status={}'.format(state.name))
            logger.info('[POST] Response - {}'.format(self.request.path))
        except Exception as e:
            self.redirect('/?status={}'.format('ERROR'))

    def isArgumentsSafe(self, args):
        return True

    def getAllUndelete(self):
        state = ResponseType.SUCCESS
        res = UndeleteDAOHelper.getAll()
        if len(res) != 0:
            res = UndeleteDAOHelper.toDict(res)
        return res, state

    def getAll(self):
        state = ResponseType.SUCCESS
        collectedFromCache = False
        res = InventoryControlHandler.inventoryCache.getCache('all', None)
        if res is not None:
            collectedFromCache = True

        if not collectedFromCache:
            res = InventoryTableDA0Helper.getAll()
            if len(res) != 0:
                res = InventoryTableDA0Helper.toDict(res)
            InventoryControlHandler.inventoryCache.setCache('all', res)
        else:
            logger.info('Serving the request from cached data...')

        return res, state

    def createItem(self):
        args = self.getArgsFromByteString(self.request.body)
        state = ResponseType.SUCCESS
        try:
            res = InventoryTableDA0Helper.create(**args)
        except Exception as e:
            state = ResponseType.INVALID_ARGS
            InventoryTableDA0Helper.rollback()

        if state == ResponseType.SUCCESS:
            InventoryControlHandler.inventoryCache.setIsDirty()

        return {}, state

    def updateItem(self):
        args = self.getArgsFromByteString(self.request.body)
        state = ResponseType.SUCCESS
        try:
            res = InventoryTableDA0Helper.update(**args)
        except Exception as e:
            state = ResponseType.SERVER_ERROR
            InventoryTableDA0Helper.rollback()

        if state == ResponseType.SUCCESS:
            InventoryControlHandler.inventoryCache.setIsDirty()

        return {'operation': 'UPDATE',  'numberOfRows': res}, state

    def deleteItem(self):
        args = self.getArgsFromByteString(self.request.body)
        state = ResponseType.SUCCESS
        try:
            res = InventoryTableDA0Helper.delete(args['code'], comment=args['comment'])
        except Exception as e:
            state = ResponseType.SERVER_ERROR
            InventoryTableDA0Helper.rollback()

        if state == ResponseType.SUCCESS:
            InventoryControlHandler.inventoryCache.setIsDirty()

        return {'operation': 'DELETE',  'numberOfRows': res}, state

    def undeleteItem(self):
        args = self.getArgsFromByteString(self.request.body)
        state = ResponseType.SUCCESS
        try:
            res = UndeleteDAOHelper.undelete(args['code'])
        except Exception as e:
            state = ResponseType.SERVER_ERROR
            UndeleteDAOHelper.rollback()

        if state == ResponseType.SUCCESS:
            InventoryControlHandler.inventoryCache.setIsDirty()

        return {'operation': 'UNDELETE', 'numberOfRows': res}, state



