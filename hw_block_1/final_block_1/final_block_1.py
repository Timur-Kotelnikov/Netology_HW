import requests
import time
import json

with open('tokens.txt') as tokens:
    yandex_token = tokens.readline().strip()
    vk_token = tokens.readline().strip()


class VK:
    def __init__(self, user_id):
        self.user_id = user_id
        self.token = vk_token

    def get_photo_list(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.user_id, 'album_id': 'profile', 'photo_sizes': '1', 'extended': '1',
                  'access_token': self.token, 'v': '5.131'}
        profile_photos = requests.get(url=url, params=params).json()['response']['items']
        profile_photos_likes = list()
        size_list = ['s', 'm', 'o', 'p', 'q', 'r', 'x', 'y', 'z', 'w']
        final_list = list()
        for photo in profile_photos:
            profile_photos_likes.append(photo['likes']['count'])
        for photo in profile_photos:
            photo_copies_sizes = list()
            photo_info = dict()
            for photo_copies in photo['sizes']:
                photo_copies_sizes.append(photo_copies['type'])
            for size in size_list:
                if size in photo_copies_sizes:
                    if profile_photos_likes.count(photo['likes']['count']) > 1:
                        photo_info['file_name'] = str(photo['likes']['count']) + ' likes' + ' Date = ' + time.ctime(
                            photo['date']).replace(':', '-') + '.jpg'
                        photo_info['size'] = size
                    else:
                        photo_info['file_name'] = str(photo['likes']['count']) + ' likes.jpg'
                        photo_info['size'] = size
            final_list.append(photo_info)
        return final_list

    def get_photo_dict(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.user_id, 'album_id': 'profile', 'photo_sizes': '1', 'extended': '1',
                  'access_token': self.token, 'v': '5.131'}
        profile_photos = requests.get(url=url, params=params).json()['response']['items']
        profile_photos_dict = dict()
        profile_photos_likes = list()
        size_list = ['w', 'z', 'y', 'x', 'r', 'q', 'p', 'o', 'm', 's']
        for photo in profile_photos:
            profile_photos_likes.append(photo['likes']['count'])
        for photo in profile_photos:
            photo_copies_sizes = list()
            for photo_copies in photo['sizes']:
                photo_copies_sizes.append(photo_copies['type'])
                for i in range(0, len(size_list)):
                    if size_list[i] in photo_copies_sizes and not set(size_list[:i]).intersection(photo_copies_sizes):
                        if photo_copies['type'] == size_list[i]:
                            if profile_photos_likes.count(photo['likes']['count']) > 1:
                                profile_photos_dict[str(photo['likes']['count']) + ' likes' + ' Date = ' + time.ctime(
                                    photo['date']).replace(':', '-') + '.jpg'] = photo_copies['url']
                            else:
                                profile_photos_dict[str(photo['likes']['count']) + ' likes.jpg'] = photo_copies['url']
        return profile_photos_dict

    def get_json_file(self):
        with open(f'{self.user_id}.json', 'w') as f:
            json.dump(self.get_photo_list(), f, ensure_ascii=False)


class YandexDisk:
    def __init__(self):
        self.token = yandex_token

    def get_headers(self):
        return {'Content-Type': 'application/json', f'Authorization': f'OAuth {self.token}'}

    def new_folder(self, folder_name):
        params = {'path': folder_name}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers=self.get_headers(),
                                params=params)
        return response.json()

    def upload_photo(self, some_name, some_url):
        params = {'url': some_url, 'path': some_name}
        response = requests.post(url='https://cloud-api.yandex.net/v1/disk/resources/upload', params=params,
                                 headers=self.get_headers())
        response.raise_for_status()

    def upload_all_photos(self, some_dict, user_id):
        count = 0
        for k, v in some_dict.items():
            count += 1
            self.upload_photo(some_name=f'/{user_id}/{k}', some_url=v)
            print(f'Foto {k} is in cloud! Progress = {count}/{len(some_dict) + 1}')

    def all_in_one(self, person):
        self.new_folder(person.user_id)
        self.upload_all_photos(person.get_photo_dict(), person.user_id)
        person.get_json_file()
        print(f'Created file {person.user_id}.json! Progress = '
              f'{len(person.get_photo_dict()) + 1}/{len(person.get_photo_dict()) + 1}')
