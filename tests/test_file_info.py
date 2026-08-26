from src.file_info import format_size, get_path_info

def test_format_size_bytes():
    assert format_size(500) == "500 B"

def test_format_size_kilobytes():
    assert format_size(2048) == " 2.00 KB"

def test_format_size_megabytes():
    assert format_size(1024**2) == " 1.00 MB"

def test_get_path_info_for_file():
    info = get_path_info("src/file_info.py")
    assert info["exists"] == "True"
    assert info["type"] == "file"

def test_get_path_info_for_missing_path():
    info = get_path_info("this/path/does/not/exist")
    assert info["exists"] == "False"
