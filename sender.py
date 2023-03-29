import data
import requests
import configuration


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json=body,
                         headers=data.headers)


response = post_new_order(data.headers)


def get_track_number():
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER)


print(response.status_code)
print(response.json())
