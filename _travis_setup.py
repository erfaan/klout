import sys

requirements = ['nose', 'unittest2']
if sys.version_info >= (3, 0):
    requirements = ['nose', 'unittest2py3k']

f = open('requirements.txt' ,'w')
for package in requirements:
    f.write("%s\n" % package)

f.close()