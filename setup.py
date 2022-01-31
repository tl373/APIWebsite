from setuptools import setup

config = {
    'description': 'LoanStreet API test',
    'install_requires': ['flask'],
    'packages': ['mymodule','mymodule.submodule1','mymodule.submodule2','mymodule.webapp'],
    'include_package_data' : True,
    'package_data' : {
        'templates' : 'mymodule/webapp/templates/*',
        'static' : 'mymodule/webapp/static/*'
        },
    'scripts': [],
    'name': 'mulch',
    'zip_safe' : False
}

setup(**config)