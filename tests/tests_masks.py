from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("7458231456987412") == "7458 23** **** 7412"
