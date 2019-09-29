# Copyright 2019 Bruno P. Kinoshita
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

from pathlib import Path

import pytest

from protobuf_uml_diagram import PathPath, Diagram


def test_path_path():
    """Test the converter used for the command line args."""
    path_path = PathPath()
    path = path_path.convert(value="blue", param="color", ctx=None)
    assert isinstance(path, Path)


class TestDiagramBuilder:

    def test_from_file_raises(self):
        with pytest.raises(ValueError) as e:
            Diagram().from_file('')
            assert 'Missing proto file' in str(e.value)

    def test_to_file_raises(self):
        with pytest.raises(ValueError) as e:
            Diagram().to_file(None)
            assert 'Missing output location' in str(e.value)
