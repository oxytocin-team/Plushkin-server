import requests
r = requests.post('http://127.0.0.1:8000/core/get_token/', json={"username": "qwer", "password": "qwer"})
print(r.status_code)
print(r.json())
mytoken = r.json()['token']

print('\n\n')

r = requests.get('http://127.0.0.1:8000/core/users/')
print(r.status_code)
print(r.text)

print('\n\n')

print(mytoken)
r = requests.get('http://127.0.0.1:8000/core/users/', headers={'Authorization': 'Token {}'.format(mytoken)})
print(r.status_code)
print(r.text)
