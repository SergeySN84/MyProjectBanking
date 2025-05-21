from src.utils import read_transactions
from unittest.mock import patch, mock_open
import json


def test_successful_read():
    mock_data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": -50}
    ]

    with (patch("builtins.open",
                mock_open(read_data=json.dumps(mock_data)))):
        with patch("os.path.exists", return_value=True):
            result = read_transactions("dummy_path.json")
            assert result == mock_data


def test_file_not_found():
    with patch("os.path.exists", return_value=False):
        result = read_transactions("non_existent_file.json")
        assert result == []


def test_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("os.path.exists", return_value=True):
            result = read_transactions("dummy_path.json")
            assert result == []


def test_data_not_list():
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        with patch("os.path.exists", return_value=True):
            result = read_transactions("dummy_path.json")
            assert result == []


def test_elements_not_dicts():
    with patch("builtins.open", mock_open(read_data="[1, 2, 3]")):
        with patch("os.path.exists", return_value=True):
            result = read_transactions("dummy_path.json")
            assert result == []
