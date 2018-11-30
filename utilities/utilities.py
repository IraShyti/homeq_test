import tornado.ioloop
import tornado.web
import threading

def background(f):
    """
    a threading decorator
    use @background above the function you want to thread
    (run in the background)
    """
    def bg_f(*a, **kw):
        threading.Thread(target=f, args=a, kwargs=kw).start()
    return bg_f