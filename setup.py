from distutils.core import setup

setup(
    name = "phonehub",
    packages = ["phonehub"],
    version = "1.0.0",
    description = "django-phonehub is a django app for simple and fast Aastra phones xml creation",
    author = "Andrea Mucci",
    author_email = "cingusoft@gmail.com",
    url = "",
    keywords = ["aastra", "sip", "xml", "django"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
Django app for automatic generation of Aastra XML SIP Phones
-------------------------------------

Work with
 - All Aastra SIP Phones of 67xxi serie ( 6730i, 6731i, 6735i, 6737i, 6753i, 6755i, 6757i, 6739i )
Support
 - All XML Root commands ( latest firmware release 3.2.2 )
 - Offer specific HTTP Response that format the code and the HTTP Header for correct phone push
 - Support ISO-8859-1 and UTF-8
 
This version requires Python 2 or later;
"""
)