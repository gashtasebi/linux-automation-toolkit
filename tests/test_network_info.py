from src.network_info import get_active_interfaces, get_network_interfaces

def test_get_network_interfaces_returns_list():
    interfaces = get_network_interfaces()
    assert isinstance(interfaces, list)


def test_get_network_interfaces_contains_name_and_addresses():
    interfaces = get_network_interfaces()

    if interfaces:
        assert "name" in interfaces[0]
        assert "addresses" in interfaces[0]
        assert isinstance(interfaces[0]["name"], str)
        assert isinstance(interfaces[0]["addresses"], list)


def test_get_active_interfaces_returns_list():
    interfaces = get_active_interfaces()
    assert isinstance(interfaces, list)

def test_active_interfaces_contains_strings():
    interfaces = get_active_interfaces()
    assert all(isinstance(name, str) for name in interfaces)
