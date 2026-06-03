import sender_stand_request
import data


# Función para obtener el token
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]


# Función para construir el cuerpo del kit
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Función para casos positivos (espera código 201)
def positive_assert(kit_body):
    token = get_new_user_token()

    response = sender_stand_request.post_new_client_kit(
        kit_body,
        token
    )

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Función para casos negativos (espera código 400)
def negative_assert_code_400(kit_body):
    token = get_new_user_token()

    response = sender_stand_request.post_new_client_kit(
        kit_body,
        token
    )

    assert response.status_code == 400


# Caso 1: 1 carácter
def test_1_char():
    positive_assert(get_kit_body("a"))


# Caso 2: 511 caracteres
def test_511_char():
    positive_assert(get_kit_body("a" * 511))


# Caso 3: nombre vacío
def test_empty_name():
    negative_assert_code_400(get_kit_body(""))


# Caso 4: 512 caracteres
def test_512_char():
    negative_assert_code_400(get_kit_body("a" * 512))


# Caso 5: caracteres especiales permitidos
def test_special_chars():
    positive_assert(get_kit_body("\"№%@,"))


# Caso 6: espacios permitidos
def test_spaces():
    positive_assert(get_kit_body(" A Aaa "))


# Caso 7: números permitidos
def test_numbers():
    positive_assert(get_kit_body("123"))


# Caso 8: parámetro name ausente
def test_no_name():
    kit_body = data.kit_body.copy()
    del kit_body["name"]

    negative_assert_code_400(kit_body)


# Caso 9: tipo incorrecto
def test_wrong_type():
    kit_body = data.kit_body.copy()
    kit_body["name"] = 123

    negative_assert_code_400(kit_body)