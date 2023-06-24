import requests

#response = requests.post('http://127.0.0.1:5000/adv', json={'title': 'WTS gold', 'text': '9999 $'})
#response = requests.get('http://127.0.0.1:5000/adv')
response = requests.delete('http://127.0.0.1:5000/adv/11')

print(response.status_code)
print(response.text)
