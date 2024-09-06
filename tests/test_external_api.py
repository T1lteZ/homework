from unittest.mock import patch

import requests

from src.external_api import conversion_api


@patch("requests.get")
def test_conversion(mock_get, transaction_t):
    mock_get.return_value.json.return_value = {'success': True, 'query':
                                               {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info':
                                               {'timestamp': 1724671757, 'rate': 91.475458},
                                               'date': '2024-08-26', 'result': 752053.586137}
    assert conversion_api(transaction_t) == 752053.586137