# ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['image_manipulator'],       # This is the name of the package
    package_dir={'': 'src'})  # This says that the package is in the "python" directory

setup(**setup_args)

