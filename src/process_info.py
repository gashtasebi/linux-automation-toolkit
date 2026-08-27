import psutil

def get_process_count() -> int:
    """Return the number of running processes."""
    return len(psutil.pids())

def get_process_info(limit: int=10) -> list[dict[str, str | int]]:
    """Return information about running processes."""
    processes = []

    for process in psutil.process_iter(["pid", "name"]):
        try:
            info = process.info

            processes.append(
                {
                    "pid" : info["pid"],
                    "name" : info["name"] or "unknown",
                }
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        if len(processes) >= limit:
            break
    return processes


def main() -> None:
    """Run the process information tool."""
    count = get_process_count()
    print(f"Running processes: {count}")
    print("\nFirst processes:")

    for process in get_process_info():
        print(f'PID: {process["pid"]:<6} Name: {process["name"]}')


if __name__ == "__main__":
    main()
