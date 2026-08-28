from src.config import APP_NAME, APP_VERSION
from src.main import main

def test_main_exists():
    assert callable(main)

def test_app_configuration():
    assert APP_NAME == "Linux Automation Toolkit"
    assert APP_VERSION == "0.1.0"
