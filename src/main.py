import argparse
import logging

from src.config import APP_NAME, APP_VERSION
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

    for address in interface["addresses"]:
        print(f"Address: {address}")


def run_command(command: str) -> None:
    """Run the selected command."""
    logging.info("Excuting command: %s", command)

    if command == "system":
        show_system_info()

    elif command == "processes":
        show_process_info()

    elif command == "network":
        show_network_info()

def configure_logging() -> None:
    """Configure application logging."""
    logging.basicConfig(
        level= logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def main() -> None:
    """Run the command-line interface."""
    configure_logging()

    logging.info("Linux Automation Toolkit started")

    parser = argparse.ArgumentParser(
        description = APP_NAME
    )

    parser.add_argument(
        "--version",
        action= "version",
        version= f"{APP_NAME} {APP_VERSION}",
    )

    parser.add_argument(
        "command",
        choices = ["system", "processes", "network", "file"],
        help = "Information to display",
    )

    parser.add_argument(
        "path",
        nargs= "?",
        help= "path to a file or directory",
    )

    args = parser.parse_args()

    if args.command == "file":
        if args.path is None:
            parser.error("The 'file' command requires a path.")

        logging.info("Inspecting path: %s, args.path")

        try:

            info = get_path_info(args.path)
            print_path_info(info)

        except FileNotFoundError:

            logging.error("path not found: %s", args.path)
            parser.error(f"Path not found: {args.path}")

    else:
         run_command(args.command)


if __name__ == "__main__":
    main()
