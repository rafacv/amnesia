Amnesia
=======

Inspired by [shotgun](http://github.com/rtomayko/shotgun) and [memento](http://pypi.python.org/pypi/memento/0.2), Amnesia is a tool that aids the development of WSGI compliant applications reloading modules on each request.

Restart your webserver no more.

Overview
--------
Amnesia takes care of loaded modules by the time it's instantiated and reloads all modules imported afterwards on-the-fly as an aid for development of WSGI compliant applications.
Amnesia is meant to be used like a standalone executable, running on the shell like:

    amnesia mymodule my_wsgi_app

or as a WSGI Middleware as follows:

    >>> from wsgiref.simple_server import make_server
    >>> from amnesia import Amnesia
    >>> 
    >>> my_reloading_app = Amnesia("mymodule", "wsgi_app")
    >>> 
    >>> if __name__ == "__main__":
    >>>     httpd = make_server("", 8080, my_reloading_app)
    >>>     print("Running on localhost:8080...")
    >>>     print("Modify your app and refresh your browser's page.")
    >>>     httpd.serve_forever()
    >>> 


Meta
------
* Author: Rafael Carlos Valverde, rafael@codeazur.com.br
* License: [MIT](http://www.opensource.org/licenses/mit-license.php)
* Home: http://rafaelcv.github.com/amnesia
* Bugs and other issues: http://github.com/rafaelcv/amnesia/issues
