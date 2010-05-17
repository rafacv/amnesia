from distutils.core import setup
from amnesia import __version__ as amnesia_version
from amnesia import __doc__ as long_description

version = ".".join(map(str, amnesia_version))

setup(name='amnesia',
      version=version,
      description="Amnesia eases web development by reloading WSGI apps "\
                  "and imported modules before each request.",
      author="Rafael Carlos Valverde",
      author_email="rafael@codeazur.com.br",
      url="http://rafaelcv.github.com/amnesia",
      scripts=["amnesia"],
      py_modules=['amnesia'],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        ],
      long_description=long_description,
     )
