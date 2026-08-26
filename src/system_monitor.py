import platform


def get_system_info() -> dict[str, str]:
    """Return basic information about the operating system."""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }

def print_system_info(info: dict[str, str]) -> None:
    """Print system information in a readable format."""
    for key, value in info.items():
        print(f"{key}: {value}")

def main() -> None:
    """Run the system operating program."""
    try:
        info = get_system_info()
        print_system_info(info)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
