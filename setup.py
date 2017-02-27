# Always prefer setuptools over distutils
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='boston_analytics_example',
      version='1',
      description='Short description of what your project is supposed to do',
      url='https://github.com/cityofboston/<boston_analytics_example>',
      author='Your Name',
      author_email='<youremail>@boston.gov',
      packages=['boston_analytics_example'],
      zip_safe=False)

