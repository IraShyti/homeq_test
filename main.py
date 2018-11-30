from tornado.httpserver import HTTPServer
import tornado.web
from tornado.options import define, options
from Handlers.main_handler import *
from Handlers.rabitmq import *
from tornado.ioloop import IOLoop


define("port", default=8888, help="run on the given port", type=int)


settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "main": os.path.join(os.path.dirname(__file__), "templates/index.html"),
    "debug": True,
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "xsrf_cookies": False
}


if __name__ == '__main__':
    tornado.options.parse_command_line()
    # Initialize RabbitMq
    RabbitMq()

    app = tornado.web.Application([

        (r"/", MainHandler),



    ], **settings)

    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.instance().start()
