#!/usr/bin/python
# Copyright (c) 2015.
#

# Author(s):
#   Martin Raspaud <martin.raspaud@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
"""

from setuptools import setup
import versioneer

setup(name="trollmoves",
      version=versioneer.get_version(),
      description='Pytroll file utilities',
      author='Martin Raspaud',
      author_email='martin.raspaud@smhi.se',
      cmdclass=versioneer.get_cmdclass(),
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License v3 " +
                   "or later (GPLv3+)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Scientific/Engineering"],
      url="https://github.com/pytroll/pytroll-file-utils",
      scripts=['bin/move_it.py',
               'bin/move_it_server.py',
               'bin/move_it_client.py',
               'bin/move_it_mirror.py',
               'bin/remove_it.py',
               ],
      data_files=[],
      packages=['trollmoves'],
      zip_safe=False,
      install_requires=['pyinotify', 'posttroll>=1.5.1',
                        'trollsift', 'netifaces',
                        'pyzmq', 'six',
                        'scp', 'paramiko'],
      )
