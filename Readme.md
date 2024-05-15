# Python API automation framework

Hybrid custom framework to test the REST API's

### Tech Stack
1. Python 3.11
2. Requests - HTTP Requests
3. Pytest - Testing framework
4. Reporting - Allure Reports, Pytest HTML
5. Test data - csv, Excel, JSON
6. Parallel Execution - x distribute [ x-dist]
7. Concepts - Fixtures,DDT,CRUD, Dynamic payload, Dot env, Json scehma check


# How to install all packages -
 pip install requests pytest pytest-html faker allure-pytest json

# To install the freeze version
pip install -r requirements.txt

# Packages to be installed -
1. allure-pytest             2.13.2
2. allure-python-commons     2.13.2
3. attrs                     23.2.0
4. certifi                   2024.2.2
5. charset-normalizer        3.3.2
6. colorama                  0.4.6
7. Faker                     23.3.0
8. idna                      3.6
9. iniconfig                 2.0.0
10. Jinja2                    3.1.3
11. jsonschema                4.21.1
12. jsonschema-specifications 2023.12.1
13. six                       1.16.0
14. urllib3                   2.2.1

#Command to run test cases parallel ( using pyest-xdist)

 pytest -n auto tests/Parallel/test_parallel.py
 
# Data Driven Testing
# Read excel file using openpyxl package
