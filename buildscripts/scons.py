#!/usr/bin/env python

from __future__ import print_function

import os
import sys

if (sys.version_info[0], sys.version_info[1]) != (2, 7):
    print("This version of MongoDB can only be built with Python 2.7"
          " you appear to be using version: %s" % sys.version)
    sys.exit(1)

SCONS_VERSION = os.environ.get('SCONS_VERSION', "2.5.0")

mongodb_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
scons_dir = os.path.join(mongodb_root, 'src', 'third_party','scons-' + SCONS_VERSION,
                         'scons-local-' + SCONS_VERSION)

if not os.path.exists(scons_dir):
    print("Could not find SCons in '%s'" % (scons_dir))
    sys.exit(1)

sys.path = [scons_dir] + sys.path

try:
    import SCons.Script
except ImportError as import_err:
    print("Could not import SCons from '%s'" % (scons_dir))
    print("ImportError:", import_err)
    sys.exit(1)

SCons.Script.main()
