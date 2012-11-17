from setuptools import setup
import re
import sys

verstr = "unknown"
try:
    verstrline = open('klout/_version.py', "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^__release__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("unable to find version in yourpackage/_version.py")

INSTALL_REQUIRES = []
if sys.version_info < (2 , 6):
    INSTALL_REQUIRES = ['simplejson']

TEST_REQUIRE = ['nose', 'unittest2']
if sys.version_info >= (3, 0):
    TEST_REQUIRE = ['nose', 'unittest2py3k']

setup(
    name='Klout',
    version=verstr,
    author='Irfan Ahmad',
    author_email='klout@i.com.pk',
    packages=['klout'],
    url='http://pypi.python.org/pypi/klout/',
    license='LICENSE.txt',
    description='Minimalist Klout API interface.',
    long_description=open('README').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
    ],
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRE
)