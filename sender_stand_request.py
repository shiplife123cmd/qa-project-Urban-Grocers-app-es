import requests
import configuration
import data


def post_new_user(body):
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH

    headers = {
        "Content-Type": "application/json"
    }

    return requests.post(url, json=body, headers=headers)


def post_new_client_kit(kit_body, token):
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    return requests.post(url, json=kit_body, headers=headers)