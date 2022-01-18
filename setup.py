# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycep', 'pycep.models', 'pycep.services']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['pycep = main:cep_cli']}

setup_kwargs = {
    'name': 'pycep',
    'version': '2.0.0',
    'description': 'A simple cli that get cep information',
    'long_description': None,
    'author': 'Guilherme Seganzerla',
    'author_email': 'g.seganzerla@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

