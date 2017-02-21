# Always prefer setuptools over distutils
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='module_name',
      version='1',
      description='Short description of what your project is supposed to do',
      url='https://github.com/cityofboston/<module_name>',
      author='Your Name',
      author_email='<youremail>@boston.gov',
      packages=['module_name'],
      zip_safe=False)

