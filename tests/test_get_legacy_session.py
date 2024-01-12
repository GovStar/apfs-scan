import pytest

from apfs_scan import get_legacy_session


def test_get_legacy_session():
  session = get_legacy_session()
  assert session.adapters['https://'].__class__.__name__ == 'CustomHttpAdapter'
