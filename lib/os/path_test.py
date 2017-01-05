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

# pylint: disable=g-import-not-at-top

import os
import os.path
path = os.path

import weetest
import tempfile


def TestIsAbs():
  assert path.isabs('/abc')
  assert not path.isabs('abc/123')


def TestJoin():
  assert path.join('') == ''
  assert path.join('', '') == ''
  assert path.join('abc') == 'abc'
  assert path.join('abc', '') == 'abc/'
  assert path.join('abc', '', '') == 'abc/'
  assert path.join('abc', '', '123') == 'abc/123'
  assert path.normpath(path.join('abc', '.', '123')) == 'abc/123'
  assert path.normpath(path.join('abc', '..', '123')) == '123'
  assert path.join('/abc', '123') == '/abc/123'
  assert path.join('abc', '/123') == '/123'
  assert path.join('abc/', '123') == 'abc/123'
  assert path.join('abc', 'x/y/z') == 'abc/x/y/z'
  assert path.join('abc', 'x', 'y', 'z') == 'abc/x/y/z'


def TestNormPath():
  assert path.normpath('abc/') == 'abc'
  assert path.normpath('/a//b') == '/a/b'
  assert path.normpath('abc/../123') == '123'
  assert path.normpath('../abc/123') == '../abc/123'
  assert path.normpath('x/y/./z') == 'x/y/z'


def TestDirname():
  assert path.dirname('/a/b/c') == '/a/b'
  assert path.dirname('/a/b/c/') == '/a/b/c'


def TestExists():
  _, file_path = tempfile.mkstemp()
  dir_path = tempfile.mkdtemp()
  try:
    assert path.exists(file_path)
    assert path.exists(dir_path)
  finally:
    os.remove(file_path)
    os.rmdir(dir_path)


def TestIsDir():
  _, file_path = tempfile.mkstemp()
  dir_path = tempfile.mkdtemp()
  try:
    assert not path.isdir(file_path)
    assert path.isdir(dir_path)
  finally:
    os.remove(file_path)
    os.rmdir(dir_path)


def TestIsFile():
  _, file_path = tempfile.mkstemp()
  dir_path = tempfile.mkdtemp()
  try:
    assert path.isfile(file_path)
    assert not path.isfile(dir_path)
  finally:
    os.remove(file_path)
    os.rmdir(dir_path)


if __name__ == '__main__':
  weetest.RunTests()
