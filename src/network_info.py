import psutil

def get_network_interfaces() -> list[dict[str, str]]:
    """Return information about network interfaces."""
    interfaces = []

    for name, addresses in psutil.net_if_addrs().items():
        interface_info = {
            "name" : name,
            "addresses" : [],
        }

        for address in addresses:
            interface_info["addresses"].append(address.address)
        interfaces.append(interface_info)

    return interfaces

def get_active_interfaces() -> list[str]:
    """Return names of active network interfaces."""
    interfaces = []

    for name, status in psutil.net_if_stats().items():
        if status.isup:
            interfaces.append(name)
    return interfaces

def main() -> None:
    """Run the network information tool."""
    interfaces = get_network_interfaces()
    active_interfaces = get_active_interfaces()

    print("Network interfaces:")

    for interface in interfaces:
        status = "UP" if interface["name"] in active_interfaces else "DOWN"

    print(f'\nInterface: {interface["name"]}')
    print(f"Status: {status}")

    for address in interface["addresses"]:
        print(f"Address: {address}")

if __name__ == "__main__":
    main()
