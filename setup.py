from distutils.core import setup

setup(
    name='Klout',
    version='0.1.0',
    author='Irfan Ahmad',
    author_email='klout@i.com.pk',
    packages=['klout', 'tests'],
    url='http://pypi.python.org/pypi/klout/',
    license='LICENSE.txt',
    description='Minimalist Klout API interface.',
    long_description=open('README.rst').read(),
)