
from setuptools import setup
import sys, os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'dmbrl'))

setup(name='dmbrl',
      packages=['dmbrl', 'dmbrl.misc', 'dmbrl.misc.optimizers', 'dmbrl.env', 'dmbrl.controllers','dmbrl.modeling.models', 'dmbrl.modeling.layers', 'dmbrl.modeling.utils', 'dmbrl.config'],
      version='0.1.0',
      install_requires=['tensorflow', 'gpflow', 'dotmap'],
      package_data={'': ['*.xml','*.urdf', '*.json', '*.yaml', '*.pickle']},
      include_package_data=True
)
