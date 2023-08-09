import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# response = post_new_user(data.user_body);
# print(response.json()) # просмотр ответа
def post_new_client_kit(kit_body):  # функция запроса на создание нового списка у определенного пользователя
    response = post_new_user(data.user_body)  # создаем переменную ответ и помещаем в нее ответ сервеиа при создании польз
    token = response.json()["authToken"]  # в переменную помещаем значение из ответа по ключу
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         # значение функции будет получено по адресу с приведенным телом и зоголовком ниже
                         json=kit_body,
                         headers={"Content-Type": "application/json", "Authorization": "Bearer " + token})
