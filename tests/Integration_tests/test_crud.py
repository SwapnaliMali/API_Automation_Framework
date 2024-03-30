import json

import pytest
import requests

from src.constants.api_constants import create_token
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_token
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verifications import verify_http_status_code



class TestBooking_Crud(object):

    def test_create_token(self):
        response = post_request(url = create_token(),auth= {},headers = common_headers_json(),payload = payload_create_token(),in_json=True)
        print(create_token())
        print(payload_create_token())
        print(response)

        verify_http_status_code(response,200) # API giving wrong status code as 400.
        print(response.json)

    # def test_create_token(self):
    #     url = "https://restful-booker.herokuapp.com/auth"
    #     headers = {
    #     'Content-Type': 'application/json'
    #     }
    #     payload = {
    #         "username": "admin",
    #         "password": "password123"
    #     }
    #     response = requests.post(url=url,headers=headers,data=payload)
    #     print((response))






