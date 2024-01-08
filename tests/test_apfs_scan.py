import pytest
from apfs_scan import CustomHttpAdapter
# , get_legacy_session, get_apfs_data, apfs_data

def test_custom_http_adapter_ssl_context(): 
  adapter = CustomHttpAdapter()
  assert adapter.ssl_context is not None


def test_custom_http_adapter_init():
  ssl_context = 'dummy context'
  adapter = CustomHttpAdapter(ssl_context=ssl_context)
  assert adapter.ssl_context == ssl_context

def test_custom_http_adapter_pool_manager():
  ssl_context = 'dummy context'
  adapter = CustomHttpAdapter(ssl_context=ssl_context)
  pool_manager = adapter.init_poolmanager(10, 100)
  assert pool_manager.ssl_context == ssl_context

@pytest.mark.parametrize('connections.maxsize', [
  (5, 20),
  (10, 100),
  (1, 10)
])

def test_custom_http_adapter_pool_manager_params(connections, maxsize):
  adapter = CustomHttpAdapter()
  adapter.init_poolmanager(connections, maxsize)
  assert adapter.poolmanager.num_pools == connections
  assert adapter.poolmanager.maxsize == maxsize

# def test_get_legacy_session():
#   session = get_legacy_session()
#   assert session.adapters['https://'].__class__.__name__ == 'CustomHttpAdapter'

# def test_get_apfs_data():
#   data = get_apfs_data()
#   assert isinstance(data, dict)
#   assert 'forecastDate' in data

# def test_apfs_data():
#   first_data = apfs_data()
#   second_data = apfs_data()
#   assert first_data == second_data #checks caching works
