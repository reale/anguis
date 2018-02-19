#!/usr/bin/env python

# anguis - A generic key-store library

# The MIT License (MIT)
# 
# Copyright (c) 2018 Roberto Reale
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from git import Repo
from anguis import anguisFS

class AnguisGit(anguisFS.AnguisFS):

    def set(self, key, value):
        super(AnguisGit, self).set(key, value)
        index = self.repo.index
        path = self._key_to_path(key)
        index.add([path])
        index.commit("Add key %s" % key)

    def erase(self, key):
        index = self.repo.index
        path = self._key_to_path(key)
        index.remove([path])
        index.commit("Erase key %s" % key)
        super(AnguisGit, self).erase(key)

    def __init__(self, dir, autoDestroy=False):
        super(AnguisGit, self).__init__(dir, autoDestroy)
        self.repo = Repo(self.dir)

    def __del__(self):
        super(AnguisGit, self).__del__()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
