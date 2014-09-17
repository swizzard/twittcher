import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open('twittcher/version.py').read()) # loads __version__

setup(name='twittcher',
      version=__version__,
      author='swizzard',
    description=("Watch tweets on Twitter's user pages or search pages."),
    long_description=open('README.rst').read(),
    license='see LICENSE.txt',
    keywords="Twitter tweet search bot",
    install_requires=['beautifulsoup', 'redis'],
    packages= find_packages(exclude='docs'))
