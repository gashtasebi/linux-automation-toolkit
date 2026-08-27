from src.process_info import get_process_count, get_process_info

def test_get_process_count_returns_integer():
    count = get_process_count()

    assert isinstance(count, int)

def test_get_process_count_is_not_negative():
    count = get_process_count()

    assert count >= 0

def test_get_process_info_returns_list():
    processes = get_process_info()

    assert isinstance(processes, list)

def test_get_process_info_contains_expected_keys():
    processes = get_process_info()

    if processes:
        assert "pid" in processes[0]
        assert "name" in processes[0]

def test_get_process_info_respects_limit():
    processes = get_process_info(limit = 3)

    assert len(processes) <=3
