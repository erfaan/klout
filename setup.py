from distutils.core import setup
from klout import __release__

setup(
    name='Klout',
    version=__release__,
    author='Irfan Ahmad',
    author_email='klout@i.com.pk',
    packages=['klout'],
    url='http://pypi.python.org/pypi/klout/',
    license='LICENSE.txt',
    description='Minimalist Klout API interface.',
    long_description=open('README.rst').read(),
)