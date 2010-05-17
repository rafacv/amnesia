# -*- coding: utf-8 -*-

# Copyright (c) 2010 Rafael Carlos Valverde
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
    Amnesia reloads modules on-the-fly as an aid for development
    of WSGI compliant applications.
    Amnesia is meant to be used like a standalone executable,
    running on the shell like `amnesia mymodule my_wsgi_app`
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
"""

import sys

__author__ = ("Rafael Carlos Valverde", "rafael@codeazur.com.br")
__version__ = (0, 2, 0)
__license__ = ("MIT",)

class Amnesia:
    """Track imported modules after instantiation and reload them
        at each request.
    """
    def __init__(self, module, appname):
        self.wsgi_app = {"module": module, "app": appname}
        self.existing_modules = set(sys.modules.keys())
    def _reload(self):
        modules = list(sys.modules.keys())
        for module in modules:
            if module not in self.existing_modules:
                del(sys.modules[module])
    def __call__(self, environ, start_response):
        module = self.wsgi_app["module"]
        appname = self.wsgi_app["app"]
        self._reload()
        __import__(module, globals(), locals(), (appname,))
        app = sys.modules[module].__getattribute__(appname)
        return app.__call__(environ, start_response)
