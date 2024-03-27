# HTTP common verifications that we do are stored here

def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected status code" + expect_data

def verify_json_key_for_not_null(key):
    assert key != 0, "key not empty" + key
    assert key >= 0, "key is not zero"


def verify_response(key):
    assert key is not None, "token is not none"  #check for token should be not null


def verify_json_response(response_data, is_json):
    assert response_data == is_json, " is json "


def verify_headers(headers):
    assert headers != 0


def verify_response_time(expected_response_time, actual_time):
    assert actual_time == expected_response_time, "response time not matching"
