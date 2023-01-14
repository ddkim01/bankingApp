# Understanding Python and REST APIs.
# https://realpython.com/api-integration-in-python/#:~:text=REST%20APIs%20provide%20access%20to%20web%20service%20data%20through%20public%20web%20URLs.&text=This%20URL%20allows%20you%20to,URL%20and%20processing%20the%20response.


# Personal Access Token for UP Bank and getting started:
# up:yeah:maW5zK0VEhvPisXf3E1OBdfDNieJEYK5nEPsHbsf7preN1jY9nP1esf5qMMhue75Ohzgu0aLxzKsv1cYpa5cxnKPeLnXSEOoE4gnz3upe9pw9YlxP97AzN2ucF29KJwK

# Python & APIs: A Winning Combo for Reading Public Data:
# https://realpython.com/python-api/#:~:text=API%20stands%20for%20application%20programming,in%20many%20forms%20or%20shapes.


import requests

from bankingApp.utils import authTokenData

accessToken = "up:yeah:maW5zK0VEhvPisXf3E1OBdfDNieJEYK5nEPsHbsf7preN1jY9nP1esf5qMMhue75Ohzgu0aLxzKsv1cYpa5cxnKPeLnXSEOoE4gnz3upe9pw9YlxP97AzN2ucF29KJwK"


def spenderBalance(authToken):

    api_url = "https://api.up.com.au/api/v1/accounts?filter[INDIVIDUAL]"

    response = requests.get(
        api_url,
        headers={"Authorization": "Bearer " + authToken},
    )

    data = (response.json())["data"][0]["attributes"]["balance"]["value"]
    print(data)


print(spenderBalance(accessToken))


