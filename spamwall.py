import random
import time
import requests

login = input("Введите номер:")
password = input("Введите пароль:")
message = input("Введите текст поста:")

s = requests.post(
   	f'https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username={login}&password={password}').json()
token = s["access_token"]
kolvo = 0

with open("user.txt","r") as lox:
	sosi = lox.read().splitlines()

while True:
	try:
		for i in sosi:
			wall = requests.get('https://api.vk.com/method/wall.post'
 								f'?owner_id={i}'
 								f'&message={message}'
 								f'&access_token={token}&v=5.124').json()
			if 'response' in wall:
				print(f'Отправлен пост! \n'f'User_id={i} \n'f'Текст поста={message} \n'f'Отправлено постов={kolvo + 1}')
				kolvo += 1
			if 'error' in wall:
				if wall.get('error').get('error_code') == 214:
					print("[!]Ошибка, видимо у пользовотеля закрыт профиль, или же лимит!")

				elif wall.get('error').get('error_code') == 9:
					print("[!]Ошибка,FLOOD CONTROL!, Попробуйте позже!")
			if kolvo > len(sosi) -1:
				print(kolvo)
				kolvo = 0
	except Exception as err:
		print("[!]Произошла ошибка...")
		