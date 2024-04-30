import json

import pytest
import requests

from src.constants.api_constants import create_token, create_booking, put_patch_delete_booking
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_token, payload_create_booking
from src.helpers.api_requests_wrapper import post_request, put_request
from src.helpers.common_verifications import verify_http_status_code, verify_response_key_should_not_be_none


class TestBooking_Crud(object):

    @pytest.fixture()
    def test_create_token(self):
        # body = json.dumps(payload_create_token())   # for formatting the payload to json
        response = post_request(url=create_token(), auth=None, headers=common_headers_json(),
                                payload=payload_create_token(), in_json=False)
        print(create_token())
        print(payload_create_token())
        print(response)

        verify_http_status_code(response, 200)  # API giving wrong status code as 400.
        print(response.json)
        token = response.json()["token"]
        print("Token : ", token)
        verify_response_key_should_not_be_none(token)
        return token

    @pytest.fixture()
    def test_create_booking(self):  #we can remove the word test here and above & mark it as functions
                                    #because we have already tested it in previous file.
        response = post_request(url=create_booking(), auth=None, headers=common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        print(response)
        verify_http_status_code(response, 200)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        bookingid = response.json()["bookingid"]
        print(bookingid)
        return bookingid

    def test_update_booking(self,test_create_token,test_create_booking):
        bookingID = test_create_booking
        url = create_booking() + "/" + str(bookingID)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
        }
        data = payload_create_booking()
        response = put_request(url=url, auth=None, headers=headers, payload=payload_create_booking(), in_json=True)
        print(url, headers, data)
        print(response, "API Response")
        print(response.text)
        # print(type(headers),"headers")
        # print(type(payload_create_booking()),"payload")
        # print(type(data),"payload func data")
        # verify_http_status_code(response,200)
        # print(test_create_token)
        # print(test_create_booking)





    # def test_put_req(self):
    #     url = "https://restful-booker.herokuapp.com/booking/3392"
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
    #     }
    #     payload = {
    #     "firstname": "Swapnali",
    #     "lastname": "M",
    #     "totalprice": 554,
    #     "depositpaid": False,
    #     "bookingdates": {
    #     "checkin": "2024-02-19",
    #     "checkout": "2024-11-03"
    #     }
    #     }
    #     data = json.dumps(payload)
    #     response = requests.put(url=url,headers=headers,data=data)
    #     print(type(payload),"payload")
    #     print(type(headers),"headers")
    #     print(response, "response")
    #     print(response.text)
