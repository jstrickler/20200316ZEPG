#!/usr/bin/env python
from ze.pg import zelib as ze
from ze.pg.zelib import spam as sp, ham as h

ze.spam()
print(ze.COLORS)

sp()
h()

# search algorithm
# 1. current dir
# 2. dirs in PYTHONPATH environment variable
# 3. sys.prefix/lib...

# Windows
#  C:\dir\one;F:\dir\two;\\some\place

# Non-Windows
#  /dir/one:/dir/two:/some/other/location


