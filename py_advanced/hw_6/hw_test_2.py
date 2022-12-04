import requests

with open('/home/timur/Documents/Python/HW/Netology_hw_nogit/hw_python/py_advanced/hw_6/tokens.txt') as tokens:
    yandex_token = tokens.readline().strip()


class YandexDisk:
    def __init__(self):
        self.token = yandex_token

    def get_headers(self):
        return {'Content-Type': 'application/json', f'Authorization': f'OAuth {self.token}'}

    def new_folder(self, folder_name):
        params = {'path': folder_name}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers=self.get_headers(),
                                params=params)
        return response.status_code

    def check_folder(self, folder_name):
        params = {'path': folder_name}
        response = requests.get(url='https://cloud-api.yandex.net/v1/disk/resources', headers=self.get_headers(), params=params)
        return response.status_code


me = YandexDisk()

