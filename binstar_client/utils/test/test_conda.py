import os
import mock

import unittest


def test_conda_root():
    from binstar_client.utils.conda import get_conda_root

    assert get_conda_root() is not None


@mock.patch('binstar_client.utils.conda._import_conda_root_dir')
def test_conda_root_outside_root_environment(mock_import_conda_root_dir):
    def _import_conda_root():
        raise ImportError()

    mock_import_conda_root_dir.side_effect = _import_conda_root
    from binstar_client.utils.conda import get_conda_root

    assert get_conda_root() is not None
    assert mock_import_conda_root_dir.called


def test_conda_root_from_conda_info():
    from binstar_client.utils.conda import _conda_root_from_conda_info

    conda_root = _conda_root_from_conda_info()
    assert conda_root is not None
    assert os.path.isdir(conda_root)
