from pathlib import Path

def format_size(size: int) -> str:
    """Convert a size in bytes to a human-readable string."""
    if size < 1024:
        return f"{size} B"

    if size < 1024**2:
        return f"{size / 1024: .2f} KB"

    if size < 1024**3:
        return f"{size /(1024**2): .2f} MB"

    return f"{size / (1024**3): .2f} GB"



def get_path_info(path: str) -> dict[str, str]:
    """Return information about the filesystem path."""
    target = Path(path)

    if not target.exists():
        return {
            "path": str(target),
            "exists": "False",
        }

    if target.is_file():
        path_type = "file"
        size = format_size(target.stat().st_size)
    elif target.is_dir():
        path_type = "directory"
        size = "N/A"
    else:
        path_type = "other"
        size = "N/A"

    return {
        "path": str(target),
        "exists": "True",
        "type": path_type,
        "size": size,
}

def print_path_info(info: dict[str, str]) -> None:
    """Print filesystem information"""
    for key, value in info.items():
        print(f"{key}: {value}")


def main() -> None:
    """Run the filesystem information tool."""
    path = input("Enter a path: ")

    try:
        info = get_path_info(path)
        print_path_info(info)
    except OSError as error:
        print(f"Filesystem error: {error}")

if __name__ == "__main__":
    main()
