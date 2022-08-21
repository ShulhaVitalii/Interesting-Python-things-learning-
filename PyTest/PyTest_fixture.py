"""Sample"""

import pytest


@pytest.fixture
def order():
    return []

@pytest.fixture
def append_first(order):
    order.append(1)

@pytest.fixture
def append_second(order, append_first):
    order.extend([2])

@pytest.fixture(autouse=True)
def append_third(order, append_second):
    order += [3]

def test_order(order):
    assert order == [1, 2, 3]
 




@pytest.fixture
def smtp_connection():
    import smtplib

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # в демонстрационных целях
    
