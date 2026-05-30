import sender_stand_request
import data


# ---------- FUNCIONES AUXILIARES ----------

def get_kit_body(name):
    return {"name": name}


def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        data.auth_token
    )

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        data.auth_token
    )

    assert response.status_code == 400


# ---------- TESTS ----------

def test_1_char():
    positive_assert(get_kit_body("a"))


def test_511_char():
    positive_assert(get_kit_body("a" * 511))


def test_empty_name():
    negative_assert(get_kit_body(""))


def test_512_char():
    negative_assert(get_kit_body("a" * 512))


def test_special_chars():
    positive_assert(get_kit_body("№%@"))


def test_spaces():
    positive_assert(get_kit_body(" A Aaa "))


def test_numbers():
    positive_assert(get_kit_body("123"))


def test_no_name():
    response = sender_stand_request.post_new_client_kit({}, data.auth_token)
    assert response.status_code == 400


def test_wrong_type():
    response = sender_stand_request.post_new_client_kit(
        {"name": 123},
        data.auth_token
    )
    assert response.status_code == 400


def test_create_user():
    response = sender_stand_request.post_new_user(data.user_body)
    print(response.status_code)
    print(response.text)

