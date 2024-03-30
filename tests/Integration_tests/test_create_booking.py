
import pytest
import json
import requests

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import create_booking
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers_json
from src.helpers.common_verifications import verify_response_key_should_not_be_none ,verify_http_status_code


class TestCreateBooking(object):

    @pytest.mark.positive
    def test_create_booking_tc1(self):
        #print(json.dumps(payload_create_booking()))
        link = create_booking()
        body = json.dumps(payload_create_booking())
        # headers = {
        #     'Content-Type': 'application/json'
        # }
        #response_data = requests.post(url= link,headers=common_headers_json(),data = body)
        #print(response_data.text)
        response = post_request(url= link,headers= common_headers_json(), auth= None,payload = body, in_json =False)  # want response in json

        print(create_booking())
        print(common_headers_json())
        print(payload_create_booking())
        print(type(response))
        print(response)

        verify_response_key_should_not_be_none(response.json()["bookingid"]) # check for getting the booking id
        verify_http_status_code(response,200) #to check if the status code is correct
        bookingid = response.json()["bookingid"]
        print('Booking id',bookingid)

    @pytest.mark.negative  # when payload is empty/none provided.
    def test_create_booking_tc2(self):
        response = post_request(create_booking(),auth= None, headers=common_headers_json(),payload=None,in_json=False)

        verify_http_status_code(response,500)



