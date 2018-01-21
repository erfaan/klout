import sys

requirements = ['coveralls==1.2.0', 'coverage==4.4.2', 'unittest2']
if sys.version_info >= (3, 0):
    requirements = ['coveralls==1.2.0', 'coverage==4.4.2', 'unittest2py3k']

f = open('requirements.txt', 'w')
for package in requirements:
    f.write("%s\n" % package)

f.close()
