import os
import sys


def reconfigure(options=None,buildout=None):
    c = os.getcwd()
    os.chdir(options['compile-directory'])
    os.remove('configure.in')
    os.system('aclocal')
    os.system("libtoolize --copy --force --install")
    os.system("autoconf")
    os.system("autoheader")
    os.system("automake -fcav")
    import pdb;pdb.set_trace()  ## Breakpoint ##



# vim:set ts=4 sts=4 et  :
