# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""""Utilities for manipulating and inspecting OS paths."""

from __go__.path.filepath import Clean as normpath, IsAbs as isabs, Join, Dir as dirname  # pylint: disable=g-multiple-import,unused-import
from __go__.os import Stat


# NOTE(compatibility): This method uses Go's filepath.Join() method which
# implicitly normalizes the resulting path (pruning extra /, .., etc.) The usual
# CPython behavior is to leave all the cruft. This deviation is reasonable
# because a) result paths will point to the same files and b) one cannot assume
# much about the results of join anyway since it's platform dependent.
def join(*paths):
  if not paths:
    raise TypeError('join() takes at least 1 argument (0 given)')
  parts = []
  for p in paths:
    if isabs(p):
      parts = [p]
    else:
      parts.append(p)
  result = Join(*parts)
  if result and not paths[-1]:
    result += '/'
  return result


def exists(path):
  _, err = Stat(path)
  if err is None:
    return True
  return False


def isdir(path):
  info, err = Stat(path)
  if info and err is None:
    return info.Mode().IsDir()
  return False


def isfile(path):
  info, err = Stat(path)
  if info and err is None:
    return info.Mode().IsRegular()
  return False
