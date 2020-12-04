import time,vk_api,colorama,datetime,os
from vk_api.longpoll import VkLongPoll, VkEventType, datetime
import random
colorama.init()

menu1 = [
"""
     \033[31m          БУДЬ АККУРАТНЕЙ!
                  
                  
     МНЕ ПОФИГ __   easyvk2.0   /
\033[36m         ╲    (_()             /
     ` + ╲__/  ||       ╲__/  /
    '(*).(xx)  /)       (oo)
    + ╲╲//~~╲╲// \033[36m      //~~╲╲
       ╲/╲__/╲/\033[33m   _____╲╲__//________\033[33m
      \033[36m   |/╲|  \033[33m  |owner: @chmotie    |\033[33m
  \033[36m _____ |||| ___\033[33m|group: @scripts_xxx|\033[33m
\033[36m  ______(_)(_)___\033[33m|___________________|\033[33m
\033[32m                     
1)Накрутка комментарий
2)Накрутка SMS
3)Накрутка постов
4)Авто-Статус
5)Удаление все друзей на странице
6)Спам постов на страницах людей
7)Создание беседы, со всеми друзьями
8)Рассылка сообщений друзьям
9)Парсер стикеров
10)Следущая cтраница
11)Накрутка друзей [BETA VERSION]
12)Бан страницы 
"""]
print(menu1[0])
vibor = input("->")

def commentaries():
  token = input("Token ->")
  user_id = input("Цифровой ид ->")
  post_id = input("Пост ид ->")
  text = input("Текст комментария ->")
  kolvo = 0
  vk_session = vk_api.VkApi(token=token)
  vk = vk_session.get_api()
  while True:
    try:
        vk.wall.createComment(owner_id=user_id,post_id=post_id,message=text)
        kolvo += 1
        time.sleep(1.5)
    except vk_api.exceptions.Captcha:
        print("[!]Капча")
        continue
    except vk_api.exceptions.ApiError:
        print("[!]Ошибка, возможно не верный токен/user_id/post_id")
    else: 
        print(f"Комментарий отправился! \n{kolvo}")

def sms():
    token = input("Token ->")
    user_id = input("Цифровой ID пользователя, который будет в беседе ->")
    kolvo = 0
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    while True:
        try:
            vk.messages.createChat(user_ids=user_id,title="Chmotie nakrutka ot Boga")
            kolvo += 1
            time.sleep(20)
        except vk_api.exceptions.Captcha:
           print("[!]Капча")
           continue
        except vk_api.exceptions.ApiError:
           print("[!]Ошибка, вероятно неправильный токен/user_id")
        else:
            print(f"Беседа создалась! \n{kolvo}")

def post():
    token = input("Token ->")
    user_id = input("ID страницы, на которой будет оставляться пост ->")
    text = input("Text поста ->")
    kolvo = 0
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    while True:
       try:
           vk.wall.post(owner_id=user_id,message=text)
           kolvo += 1
           time.sleep(2)
       except vk_api.exceptions.Captcha:
           print("[!]Капча")
           continue
       except vk_api.exceptions.ApiError:
           print("[!]Вероятно,неправильный Токен/user id")
           continue
       else:
           print(f"Пост отправлен! \n{kolvo}")

def auto():
    token = input("token ->")
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    ban = vk.account.getBanned(offset=0,count=200)['count']
    onlines = len(vk.friends.getOnline())
    while True:
        try: 
            print("Через 60 секунд, статус должен выстовиться!")
            time.sleep(60)
            vk.status.set(text="☢ Онлайн ✅ Друзья онлайн: " + str(onlines) + " 🚫 ЧС: " + str(ban) + " 🕑 Время " + str(datetime.strftime(datetime.now(), "%D, %H:%M")))
            print("Статус выставлен!")
        except vk_api.exceptions.Captcha:
           print("[!]Капча")
           continue
        except vk_api.exceptions.ApiError:
            print("[!]Вероятно, неправильный токен!")
            continue

def delete():
    token = input("Token ->")
    OWNER_ID = input("ID цифровой ->")
    count = 0
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    adds =  vk.friends.get()['items']
    while True:
        for iw in adds:
            try:
                vk.friends.delete(user_id=iw)
                time.sleep(1.5)
                print("Удален человек:vk.com/id" + str(iw))
            except vk_api.exceptions.Captcha:
                print("[!]Капча")
                continue
            except vk_api.exceptions.ApiError:
                print("[!]Вероятно, неправильный токен/ID")
                continue

def spams():
    os.system('python spamwall.py')

def spammerbeseda():
    token = input("token ->")
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    frww = vk.friends.get()['items']
    try:
        print("[!]Беседа создалась!")
        vk.messages.createChat(user_ids=frww,title='chmotietop')
    except vk_api.exceptions.ApiError:
        print("[!]Вероятно неправильный токен, или лимит")
      
def rassilka():
    Token = input("Token ->")
    text = input("Text ->")
    vk_session = vk_api.VkApi(token=Token)
    vk = vk_session.get_api()
    friends = vk.friends.get()['items']
    for i in friends:
        try:
            vk.messages.send(message=text,user_id=i,random_id=0)
        except vk_api.exceptions.ApiError:
            print("[!]Вероятно , неправильный токен. Или же лимит")

def friends():
    token = input("Token ->")
    vk_session = vk_api.VkApi(token)
    vk = vk_session.get_api()
    with open('pars.txt') as f:
        ids = f.read().splitlines()
    for ww in ids:
        try:
            print("Пошла накрутка друзей...")
            vk.friends.add(user_id=ww)
            time.sleep(30)
        except vk_api.exceptions.ApiError:
            print("[!]Вероятно неправильный токен, или лимит.")
            continue
        except vk_api.exceptions.Captcha:
            print("[!]Captcha")
            continue

#def ban():

if vibor == "1":
  ommentaries()

if vibor == "2":
  sms()

if vibor == "3":
  post()

if vibor == "4":
  auto()

if vibor == "5":
  delete()

if vibor == "6":
    spams()

if vibor == "7":
    spammerbeseda()

if vibor == "8":
    rassilka()

if vibor == "9":
    print("[!]В разработке, в слеедущих обновлениях добавят!")

if vibor == "10":
    print(menu2[0])
    input("->")
if vibor == "11":
    friends()
if vibor == "12":
    ban()
else:
    print("[!]Выбрана неверная опция")
