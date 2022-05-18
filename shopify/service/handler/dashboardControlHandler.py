import os
from shopify.util.dirUtil import DirUtil
from shopify.service.handler.baseHandler import BaseHandler

class DashboardControlHandler(BaseHandler):

    def get(self, slug=None):
        if slug is not None:
            slug = slug.upper()
        if slug == '' or slug is None or slug == 'DISPLAY':
            self.render(os.path.join(DirUtil.getWebDir(), 'index.html'))
        elif slug == 'UNDELETE':
            self.render(os.path.join(DirUtil.getWebDir(), 'undelete.html'))
