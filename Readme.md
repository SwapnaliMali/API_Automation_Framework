# Python API automation framework

Hybrid custom framework to test the REST API's

### Tech Stack
1. Python 3.11
2. Requests - HTTP Requests
3. Pytest - Testing framework
4. Reporting - Allure Reports, Pytest HTML
5. Test data - csv, Excel, JSON
6. Parallel Execution - x distribute


# How to install all packages -
 pip install requests pytest pytest-html faker allure-pytest json

# To install the freeze version
pip install -r requirements.txt

# Packages to be installed -
allure-pytest             2.13.2
allure-python-commons     2.13.2
attrs                     23.2.0
certifi                   2024.2.2
charset-normalizer        3.3.2
colorama                  0.4.6
Faker                     23.3.0
idna                      3.6
iniconfig                 2.0.0
Jinja2                    3.1.3
jsonschema                4.21.1
jsonschema-specifications 2023.12.1
six                       1.16.0
urllib3                   2.2.1

#Command to run test cases parallel  ( using pyest-xdist)
 pytest -n auto tests/Parallel/test_parallel.py