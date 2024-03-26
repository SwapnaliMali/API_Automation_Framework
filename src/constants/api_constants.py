# Add your constants here

def base_url():
    return "https://restful-booker.herokuapp.com"

def create_booking():
    return "https://restful-booker.herokuapp.com/booking"

def create_token():
    return "https://restful-booker.herokuapp.com/auth"


# Update - Put/ Patch / Delete booking

def put_patch_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/:id" + str(booking_id)
