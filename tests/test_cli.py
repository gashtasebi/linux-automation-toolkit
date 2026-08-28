import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the CLI as a subprocess."""
    return subprocess.run(
        [sys.executable, "-m", "src.main", *args],
        capture_output=True,
        text=True,
    )


def test_system_command():
    result = run_cli("system")

    assert result.returncode == 0
    assert "INFO" in result.stderr


def test_processes_command():
    result = run_cli("processes")

    assert result.returncode == 0
    assert "Running processes:" in result.stdout


def test_network_command():
    result = run_cli("network")

    assert result.returncode == 0
    assert "Network interfaces:" in result.stdout


def test_file_command():
    result = run_cli("file", "README.md")

    assert result.returncode == 0


def test_version_command():
    result = run_cli("--version")

    assert result.returncode == 0
    assert "Linux Automation Toolkit" in result.stdout
