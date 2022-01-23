import youtube
import requests
import random
import telebot
import config
from telebot import types
headerss = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'api.telegram.org',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
def ex_id(id):
    result = False
    file = open('users.txt', 'r')
    for line in file:
        if line.strip() == id:
            result = True
    file.close()
    return result

bot = telebot.TeleBot('Token')

#audio

wav = types.InlineKeyboardButton(text='WAV', callback_data='WAV')
ogg = types.InlineKeyboardButton(text='OGG', callback_data='OGG')
opus = types.InlineKeyboardButton(text='OPUS', callback_data='OPUS')
flac = types.InlineKeyboardButton(text='FLAC', callback_data='FLAC')
aac = types.InlineKeyboardButton(text='AAC', callback_data='AAC')
webm = types.InlineKeyboardButton(text='WEBM', callback_data='WEBM')
m4a = types.InlineKeyboardButton(text='M4A', callback_data='M4A')
mp3 = types.InlineKeyboardButton(text='MP3', callback_data='MP3')

#video 

mp4_360P = types.InlineKeyboardButton(text='360P', callback_data='360')
mp4_480P = types.InlineKeyboardButton(text='480P', callback_data='480')
mp4_720P = types.InlineKeyboardButton(text='720P', callback_data='720')
mp4_1080P = types.InlineKeyboardButton(text='1080P', callback_data='1080')
mp4_1440P = types.InlineKeyboardButton(text='1440P', callback_data='1440P')
mp4_4K = types.InlineKeyboardButton(text='4K', callback_data='4K')
mp4_8K = types.InlineKeyboardButton(text='8K', callback_data='8K')


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        id = message.from_user.id
        req = requests.get(f'https://api.telegram.org/bot1511452974:AAFDJ3t0h_ocgGdrurJtN_oZmcVRUhIKTyk/getChatMember?chat_id=@rickpro3&user_id={id}', headers=headerss)
        s = str(req.json()['result']['status'])
        if s == 'left':
            bot.send_message(message.chat.id, text='@rickpro3\nSubscribe to use the bot\n/start')
        else:
            idu = message.from_user.id
            f = open('users.txt', 'a')
            if (not ex_id(str(idu))):
                usern = message.from_user.username
                f.write(f"{idu}\n")
                f.close()
            name = message.from_user.first_name
            bot.send_message(message.chat.id,text=f'هلا حبيبي {name}🤍,\nارسل فيديو لتنزيله بجميع الصيغ .')
@bot.message_handler(func=lambda m:True)
def get_url(message):
    global url
    url = message.text
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.row_width = 2
    markup_inline.add(wav,ogg,opus,flac,aac,webm,m4a,mp3,mp4_360P,mp4_480P,mp4_720P,mp4_1080P,mp4_1440P,mp4_4K,mp4_8K)
    bot.send_message(message.chat.id,text='اختر احد الصيغ الاتيه : 👇',reply_markup=markup_inline)
@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    #audio callback

    if call.data == 'WAV':
        WAV(call.message)
    if call.data == 'OGG':
        OGG(call.message)

    if call.data == 'OPUS':
        OPUS(call.message)
        
    if call.data == 'FLAC':
        FLAC(call.message)

    if call.data == 'AAC':
        AAC(call.message)

    if call.data == 'WEBM':
        WEBM(call.message)

    if call.data == 'MP3':
        MP3(call.message)

    #video

    if call.data == '360':
        Mp4_360P(call.message)

    if call.data == '480':
        Mp4_480P(call.message)

    if call.data == '720':
        Mp4_720P(call.message)

    if call.data == '1080':
        Mp4_1080P(call.message)

    if call.data == '1440P':
        Mp4_1440P(call.message)

    if call.data == '4K':
        Mp4_4K(call.message)

    if call.data == '8k':
        Mp4_8K(call.message)

@bot.message_handler(func=lambda m: True)
def WAV(message):

    response = youtube.download(url=url, format='wav')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_voice(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def OGG(message):
    response = youtube.download(url=url, format='OGG')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_voice(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def OPUS(message):
    response = youtube.download(url=url, format='OPUS')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_voice(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def FLAC(message):
    response = youtube.download(url=url, format='FLAC')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_voice(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def AAC(message):
    response = youtube.download(url=url, format='AAC')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_voice(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def WEBM(message):
    response = youtube.download(url=url, format='WEBM')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_voice(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def MP3(message):
    response = youtube.download(url=url, format='MP3')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_voice(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def Mp4_360P(message):
    response = youtube.download(url=url, format=360)
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_video(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def Mp4_480P(message):
    response = youtube.download(url=url, format=480)
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_video(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')


def Mp4_720P(message):
    response = youtube.download(url=url, format=720)
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_video(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')


def Mp4_1080P(message):
    response = youtube.download(url=url, format=1080)
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_video(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def Mp4_1440P(message):
    response = youtube.download(url=url, format=1440)
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_video(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def Mp4_4K(message):
    response = youtube.download(url=url, format='4k')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_video(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

def Mp4_8K(message):
    response = youtube.download(url=url, format='8k')
    title = response['Title']
    Download_url = response['Download Url']
    Status = response['Status']

    download = requests.get(Download_url).content
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_video(message.chat.id,download,caption=f'العنوان :  : {title}\nالتحميل : 1000\nحاله التنزيل : {Status}')

bot.infinity_polling(True)
