import json
def payload_create_booking():
    payload = {

            "firstname": "Henok",
            "lastname": "Brown",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Lunch"
    }

    return json.dumps(payload)


def payload_create_token():
    payload = {

            "username": "admin",
            "password": "password123"
    }
    return json.dumps(payload)

