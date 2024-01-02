import pytest
from apfs-scan import CustomHttpAdapter, get_legacy_session, get_apfs_data, apfs_data

def test_CustomHttpAdapter():
  assert CustomHttpAdapter()

def test_get_legacy_session():
  assert get_legacy_session()

def test_get_apfs_data():
  assert get_apfs_data()

def test_apfs_data():
  assert apfs_data()
