import pytest


@pytest.fixture
def numbers_card():
    return "7000 79** **** 6361"


@pytest.fixture
def numbers_card_error():
    return None


@pytest.fixture
def numbers_card_zero():
    return None


@pytest.fixture
def numbers_acc():
    return "**4305"


