import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from shopify.logger.logger import logger
from shopify.service.handler.inventoryControlHandler import InventoryControlHandler
from shopify.service.handler.dashboardControlHandler import DashboardControlHandler
from shopify.util.envUtil import EnvUtil
from shopify.util.dirUtil import DirUtil
from shopify.util.configUtil import ConfigUtil

define('port', default=ConfigUtil().getServicePort(), help='Port to listen on')

settings = {
    "static_path": os.path.join(DirUtil.getShopifyDir(), "web")
}

app = Application([
    ('/api/inventory/([^/]+)', InventoryControlHandler),
    ('/(.*)', DashboardControlHandler),
], **settings)

http_server = HTTPServer(app)
http_server.listen(options.port)
logger.info('[{}] Dashboard service listening on http://localhost:{}'.format(EnvUtil.getEnv().upper(), options.port))
IOLoop.current().start()
