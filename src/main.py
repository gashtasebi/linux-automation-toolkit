import argparse


from src.file_info import get_path_info, print_path_info
from src.network_info import get_active_interfaces, get_network_interfaces
from src.process_info import get_process_count, get_process_info
from src.system_monitor import get_system_info

def show_system_info() -> None:
    """Display system information"""
    info = get_system_info()

    for key, value in info.items():
        print(f"{key}: {value}")

def show_process_info() -> None:
    """Display process information."""
    count = get_process_count()

    print(f"Running processes: {count}")
    print(f"\nFirst processes:")

    for process in get_process_info():
        print(f'PID: {process["pid"]:<6} name: {process["name"]}')

def show_network_info() -> None:
    """Display network interface information."""
    interfaces = get_network_interfaces()
    active_interfaces = get_active_interfaces()

    print("Network interfaces:")

    for interface in interfaces:
        status = "UP" if interface["name"] in active_interfaces else "DOWN"

    print(f'\nInterface: {interface["name"]}')
    print(f"status: {status}")


def main() -> None:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(
        description = "Linux Automation Toolkit"
    )

    parser.add_argument(
        "command",
        choices = ["system", "processes", "network"],
        help = "Information to display",
    )

    args = parser.parse_args()

    if args.command == "system":
        show_system_info()

    elif args.command == "processes":
        show_process_info()

    elif args.command == "network":
        show_network_info()


if __name__ == "__main__":
    main()
