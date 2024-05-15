# data driven testing
#Read excel, csv file
# Create  a function create_token which can take values from excel file
# Verify expected result

# Read the Excel  - openpyxl
import openpyxl
import requests
import pytest

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password = row
        credentials.append({"username":username,"password":password})
        return credentials



def make_auth_request(username,password):
    payload = {
        "username":username,
        "password":password
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url="https://restful-booker.herokuapp.com/auth",headers=headers,data=payload)
    #assert response.status_code == 200
    return response

def test_post_create_token():
    file_path = "Datadriven.xlsx"
    credentials = read_credentials_from_excel(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response = make_auth_request(username,password)
        print(response)

