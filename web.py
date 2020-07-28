import tornado
import tornado.ioloop
import tornado.web
import tornado.locks

class HomeHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write("This is home page")

class IndexHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write("this is index page")


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            templates = "template",
            static_url = "static"
        )
        handler = [
            (r'/', HomeHandler),
            (r'/index', IndexHandler)
        ]
        super().__init__(handler, **settings)

async def main():
    app = Application()
    app.listen(8888)
    shut_down = tornado.locks.Event()
    await shut_down.wait()

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)