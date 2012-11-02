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
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
    ],
)