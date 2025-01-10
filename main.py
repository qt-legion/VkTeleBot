from sympy import content
import vk_api.vk_api, telebot, threading, random, time, os, sys, pyglet, urllib.request, requests, json, PIL, glob

from pyrogram import Client, filters
from PIL import Image
from random import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

file = open(os.path.join(sys.path[0], 'txts/token.txt'), 'r')
token = file.readline()
file.close()

vk = vk_api.VkApi(token = str(token))
api = vk.get_api()
file = open(os.path.join(sys.path[0], 'txts/somewhatthing.txt'), 'r')
somewhatthing = file.readline()
file.close()
longpoll = VkBotLongPoll(vk, str(somewhatthing))

file = open(os.path.join(sys.path[0], 'txts/Teletoken.txt'), 'r')
Teletoken = file.readline()
file.close()
Telbot = telebot.TeleBot(str(Teletoken))

file = open(os.path.join(sys.path[0], 'txts/Admin_id.txt'), 'r')
TeleId = str(file.readline())
file.close()
file = open(os.path.join(sys.path[0], 'txts/Chan_id.txt'), 'r')
ChanId = []
for i in file:
    ChanId.append(str(i))
file.close()
ids = 0

def bd_update(bd):
    file = open(os.path.join(sys.path[0], 'database.json'), "w")
    new = json.dumps(bd)
    new = json.loads(str(new))
    json.dump(new, file, indent = 4)
    file.close()
    Telbot.send_message(TeleId, "Database file updated...")

def printBD(bd):
    for i in bd['ids']:
        Telbot.send_message(TeleId, "ID: " + "/" + i + "\nName: " + get_name(int(i)))

def get_name(from_user):
    user = vk.method("users.get", {"user_ids": from_user})
    name = user[0]['first_name'] +  ' ' + user[0]['last_name']
    return name

def get_title(chat_id):
    if chat_id == 1:
        return "Хантеры"
    elif chat_id == 2:
        return "Test"
    elif chat_id == 5:
        return "Сохры недохацкеров"
    elif chat_id == 4:
        return "Недохацкеры"

def get_res_photo(i):
    return len(i['sizes']) - 1

def get_res_vid(i):
    return len(i['image']) - 1

def get_event(event, mssag, chat):
    try:
        try:
            if (event['is_cropped'] == True):
                event1 = vk.method('messages.getById', {'message_ids': event['id']})
                get_event(event1['items'][0], mssag, chat)
                return
        except BaseException as err:
            if ("is_cropped" in str(err)): pass
        if chat != 0:
            Id = ChanId
            mssag += "Chat: " + chat
        else:
            Id = TeleId
            mssag += "ID: /" + str(event['from_id'])
        mssag += "\nName: " + str(get_name(str(event['from_id']))) + "\n"
        if str(event['text']) != "": mssag = mssag + "Text: " + str(event['text']) + "\n"
        if event['attachments'] != []:
            for i in event['attachments']:
                if i['type'] == 'photo':
                    url = i["photo"]["sizes"][int(get_res_photo(i["photo"]))]['url']
                    urllib.request.urlretrieve(url, "/home/qtk/workspace/" + "doc")
                    file = open("/home/qtk/workspace/" + "doc", 'rb')
                    if chat != 0:
                        for k in range (len(Id)):
                            if k == 0: Telbot.send_photo(Id[k], file, caption = mssag)
                            elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_photo(Id[k], file, caption = mssag)
                    else: Telbot.send_photo(Id, file, caption = mssag)
                    file.close()
                    os.system("rm " + "/home/qtk/workspace/" + "doc")
                elif i['type'] == 'video':
                    url = i["video"]["image"][int(get_res_vid(i["video"]))]['url']
                    urllib.request.urlretrieve(url, "/home/qtk/workspace/" + "doc")
                    file = open("/home/qtk/workspace/" + "doc", 'rb')
                    if chat != 0:
                        for k in range (len(Id)):
                            if k == 0: Telbot.send_video(Id[k], file, caption = mssag)
                            elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_video(Id[k], file, caption = mssag)
                    else: Telbot.send_video(Id, file, caption = mssag)
                    file.close()
                    os.system("rm " + "/home/qtk/workspace/" + "doc")
                elif i['type'] == "audio_message":
                    url = i['audio_message']['link_ogg']
                    urllib.request.urlretrieve(url, "/home/qtk/workspace/" + "doc")
                    file = open("/home/qtk/workspace/" + "doc", 'rb')
                    if chat != 0:
                        for k in range (len(Id)):
                            if k == 0: Telbot.send_audio(Id[k], file, caption = mssag)
                            elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_audio(Id[k], file, caption = mssag)
                    else: Telbot.send_audio(Id, file, caption = mssag)
                    file.close()
                    os.system("rm " + "/home/qtk/workspace/" + "doc")
                elif i['type'] == "doc":
                    if i['doc']['title'] != "": mssag += "Doc name: " + str(i['doc']['title'])[:-4]
                    url = i['doc']['url']
                    extens = i['doc']['ext']
                    urllib.request.urlretrieve(url, "/home/qtk/workspace/" + str(i['doc']['title'])[:-4] + "." + extens)
                    file = open("/home/qtk/workspace/" + str(i['doc']['title'])[:-4] + "." + extens, 'rb')
                    if chat != 0:
                        for k in range (len(Id)):
                            if k == 0: Telbot.send_document(Id[k], file, caption = mssag)
                            elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_document(Id[k], file, caption = mssag)
                    else: Telbot.send_document(Id, file, caption = mssag)
                    file.close()
                    os.system("rm " + "/home/qtk/workspace/" + str(i['doc']['title'])[:-4] + "." + extens)
                    mssag = mssag.replace("Doc name: " + str(i['doc']['title'])[:-4], '', 1)
                elif i['type'] == 'sticker':
                    url = i["sticker"]["images"][int(len(i['sticker']['images']) - 1)]['url']
                    urllib.request.urlretrieve(url, "/home/qtk/workspace/" + "doc")
                    file = open("/home/qtk/workspace/" + "doc", 'rb')
                    if chat != 0:
                        for k in range (len(Id)):
                            if k == 0: Telbot.send_photo(Id[k], file, caption = mssag)
                            elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_photo(Id[k], file, caption = mssag)
                    else: Telbot.send_photo(Id, file, caption = mssag)
                    file.close()
                    os.system("rm " + "/home/qtk/workspace/" + "doc")
                elif i['type'] == 'wall':
                    if (str(i['wall']['text'])) != "": mssag += "\nWall text:\n" + str(i['wall']['text'])
                    for j in i['wall']['attachments']:
                        if j['type'] == 'photo':
                            url = j["photo"]["sizes"][int(get_res_photo(j["photo"]))]['url']
                            urllib.request.urlretrieve(url, "/home/qtk/workspace/" + "doc")
                            file = open("/home/qtk/workspace/" + "doc", 'rb')
                            if chat != 0:
                                for k in range (len(Id)):
                                    if k == 0: Telbot.send_photo(Id[k], file, caption = mssag)
                                    elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_photo(Id[k], file, caption = mssag)
                            else: Telbot.send_photo(Id, file, caption = mssag)
                            file.close()
                            os.system("rm " + "/home/qtk/workspace/" + "doc")
                        elif j['type'] == 'video':
                            url = j["video"]["image"][int(get_res_vid(j["video"]))]['url']
                            urllib.request.urlretrieve(url, "/home/qtk/workspace/" + "doc")
                            file = open("/home/qtk/workspace/" + "doc", 'rb')
                            if chat != 0:
                                for k in range (len(Id)):
                                    if k == 0: Telbot.send_video(Id[k], file, caption = mssag)
                                    elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_video(Id[k], file, caption = mssag)
                            else: Telbot.send_video(Id, file, caption = mssag)
                            file.close()
                            os.system("rm " + "/home/qtk/workspace/" + "doc")
                        elif i['type'] == "doc":
                            url = i['doc']['url']
                            extens = i['doc']['ext']
                            urllib.request.urlretrieve(url, "/home/qtk/workspace/" + str(i['doc']['title'])[:-4] + "." + extens)
                            file = open("/home/qtk/workspace/" + str(i['doc']['title'])[:-4] + "." + extens, 'rb')
                            if chat != 0:
                                for k in range (len(Id)):
                                    if k == 0: Telbot.send_document(Id[k], file, caption = mssag)
                                    elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_document(Id[k], file, caption = mssag)
                            else: Telbot.send_document(Id, file, caption = mssag)
                            file.close()
                            os.system("rm " + "/home/qtk/workspace/" + str(i['doc']['title'])[:-4] + "." + extens)
        else:
            if chat != 0:
                for k in range (len(Id)):
                    if k == 0: Telbot.send_message(Id[k], mssag)
                    elif k != 0 and (chat == "Сохры недохацкеров" or chat == "Недохацкеры"): Telbot.send_message(Id[k], mssag)
            else: Telbot.send_message(Id, mssag)

        try:
            if event['fwd_messages']:
                for i in event['fwd_messages']:
                    mssg = "Forwarded:\n"
                    get_event(i, mssg, chat)
        except BaseException as err:
            if ('fwd_messages' in str(err)):
                pass
        try:
            if event['reply_message']:
                mssg = "Replyed:\n"
                get_event(event['reply_message'], mssg, chat)
        except BaseException as err:
            if ('reply_message' in str(err)):
                pass

    except BaseException as err:
        if ("timed out" in str(err) or "Temporary failure" in str(err)):
            time.sleep(2)
            mssag = ""
            get_event(event, mssag, chat)
            pass
        elif ("find end of the entity" in str(err) or "Too Many Requests" in str(err)):
            pass
        else:
            Telbot.send_message(TeleId, "Error while getting event:\n" + str(err))

def get_history(event):
    mssg = ""
    try:
        for i in reversed(event['items']):
            get_event(i, mssg, chat = 0)
    except BaseException as err:
        Telbot.send_message(TeleId, "Error while getting chat history:\n" + str(err))

def write_msg(id, text):
    vk.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})
def send_attach(id, messg, attach):
    vk.method('messages.send', {'user_id' : id, 'message': messg, 'attachment': attach, 'random_id': 0})

def init_Vk():
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    mssg = ""
                    if event.from_user:
                        #Database autoupdate:
                        if str(event.object['message']['from_id']) not in bd['ids']:
                            bd['ids'].append(str(event.object['message']['from_id']))
                            Telbot.send_message(TeleId, "New contact added: " + get_name(str(event.object['message']['from_id'])))
                            bd_update(bd)
                                    
                        #Events:
                        chat = 0
                        threading.Thread(target = get_event, args=(event.object['message'], mssg, chat,)).start()
                                                        
                    elif event.from_chat:
                        chat = str(get_title(event.chat_id))
                        threading.Thread(target  = get_event, args=(event.object['message'], mssg, chat,)).start()

        except BaseException as err:
            if "HTTPSConnectionPool" in str(err):
                time.sleep(5)
                pass

def init_Tele():
    while True:
        try:
            @Telbot.message_handler(content_types=["text"])
            def handle_text(message):

                if (str(message.from_user.id) == str(TeleId)):
                    if (message.text == "/help"):
                        t = threading.Thread(target = printBD(bd))
                        t.start()
                        
                    elif (message.text == "/status"):
                        Telbot.send_message(TeleId, "All systems normal...\nPID: " + str(os.getpid()))

                    elif (message.text == "/update"):
                        try:
                            t = threading.Thread(target = bd_update(bd))
                            t.start()
                            t.join()
                            Telbot.send_message(TeleId, "Database updated")
                        except BaseException as err:
                            Telbot.send_message(TeleId, "Error while updating database:\n" + str(err))
                    
                    elif ("/add " in message.text):
                        i = str(message.text)
                        i = i.replace('/add ', '', 1)
                        try:
                            bd_update(bd)
                            Telbot.send_message(TeleId, "Added to database...")
                        except BaseException as err: Telbot.send_message(TeleId, "Error while adding to database:\n" + str(err))
                        
                    elif ("/history " in message.text):
                        i = str(message.text)
                        i = i.replace('/history ', '', 1)
                        try:
                            id = i[0:9]
                            colvo = i[10:]
                            event = vk.method('messages.getHistory', {'user_id' : id, 'count' : colvo})
                            t = threading.Thread(target = get_history(event))

                        except BaseException as err:
                            Telbot.send_message(TeleId, "Error wile starting history dump:\n" + str(err))

                    elif (message.text == "/stop"):
                        Telbot.send_message(TeleId, "Stopping process...")
                        os.system("sudo kill " + str(os.getpid()))

                    elif (str(message.text)[0] == "/" and str(message.text)[1] != "/"):
                        try:
                            global ids
                            i = str(message.text)
                            i = i.replace('/', '', 1)
                            ids = int(i)
                            Telbot.send_message(TeleId, "Reciever specified: " + get_name(ids))
                        except BaseException as err:
                            Telbot.send_message(TeleId, "Error occured while setting reciever id:\n" + str(err))

                    elif (str(message.text)[0] != "/"):
                        try:
                            write_msg(ids, message.text)
                        except BaseException as err:
                            if "telegram" in str(err):
                                time.sleep(5)
                            else: Telbot.send_message(TeleId, "Error occured while sending message:\n" + str(err))

            @Telbot.message_handler(content_types=["sticker"])
            def handle_docs_audio(message):
                if (str(message.from_user.id) == str(TeleId)):
                    name = str(Telbot.get_file(message.sticker.file_id).file_path)
                    url = "http://api.telegram.org/file/bot5241034302:AAGctdn4nzpgX0srmueUkYxSU_YlmodU9Nw/" + name
                    try: 
                        urllib.request.urlretrieve(url, "/home/qtk/workspace/VkBot/temp/" + name)
                    except BaseException as err: Telbot.send_message(TeleId, "Error while downloading sticker:\n" + str(err))
                    try:
                        result = json.loads(requests.post(api.docs.getMessagesUploadServer(type='doc', peer_id=ids)['upload_url'], files={'file': open('/home/qtk/workspace/VkBot/temp/' + name, 'rb')}).text)
                        jsonAnswer = api.docs.save(file=result['file'], title='title', tags=[])
                        if message.caption: messg = str(message.caption)
                        else: messg = ""
                        send_attach(ids, messg, f"doc{jsonAnswer['doc']['owner_id']}_{jsonAnswer['doc']['id']}")
                        os.system("rm /home/qtk/workspace/VkBot/temp/" + name)
                    except BaseException as err: Telbot.send_message(TeleId, "Error while sending sticker:\n" + str(err))
            
            @Telbot.message_handler(content_types=["document"])
            def handle_docs_audio(message):
                if (str(message.from_user.id) == str(TeleId)):
                    name = str(Telbot.get_file(message.document.file_id).file_path)
                    url = "http://api.telegram.org/file/bot5241034302:AAGctdn4nzpgX0srmueUkYxSU_YlmodU9Nw/" + name
                    try: 
                        urllib.request.urlretrieve(url, "/home/qtk/workspace/VkBot/temp/" + name)
                    except BaseException as err: Telbot.send_message(TeleId, "Error while downloading doc:\n" + str(err))
                    try:
                        result = json.loads(requests.post(api.docs.getMessagesUploadServer(type='doc', peer_id=ids)['upload_url'], files={'file': open('/home/qtk/workspace/VkBot/temp/' + name, 'rb')}).text)
                        jsonAnswer = api.docs.save(file=result['file'], title='title', tags=[])
                        if message.caption: messg = str(message.caption)
                        else: messg = ""
                        send_attach(ids, messg, f"doc{jsonAnswer['doc']['owner_id']}_{jsonAnswer['doc']['id']}")
                        os.system("rm /home/qtk/workspace/VkBot/temp/" + name)
                    except BaseException as err: Telbot.send_message(TeleId, "Error while sending doc:\n" + str(err))

            @Telbot.message_handler(content_types=["photo"])
            def handle_docs_audio(message):
                if (str(message.from_user.id) == str(TeleId)):
                    name = str(Telbot.get_file(message.photo[len(message.photo) - 1].file_id).file_path)
                    url = "http://api.telegram.org/file/bot5241034302:AAGctdn4nzpgX0srmueUkYxSU_YlmodU9Nw/" + name
                    try: 
                        urllib.request.urlretrieve(url, "/home/qtk/workspace/VkBot/temp/" + name)
                    except BaseException as err: Telbot.send_message(TeleId, "Error while downloading photo:\n" + str(err))
                    try:
                        result = json.loads(requests.post(api.docs.getMessagesUploadServer(type='doc', peer_id=ids)['upload_url'], files={'file': open('/home/qtk/workspace/VkBot/temp/' + name, 'rb')}).text)
                        jsonAnswer = api.docs.save(file=result['file'], title='title', tags=[])
                        if message.caption: messg = str(message.caption)
                        else: messg = ""
                        send_attach(ids, messg, f"doc{jsonAnswer['doc']['owner_id']}_{jsonAnswer['doc']['id']}")
                        os.system("rm /home/qtk/workspace/VkBot/temp/" + name)
                    except BaseException as err: Telbot.send_message(TeleId, "Error while sending photo:\n" + str(err))

            Telbot.polling(none_stop=True, interval = 0, timeout = 60)
            
        except BaseException as err:
            if ("Read timed out" in str(err)):
                time.sleep(5)
                pass

def main():
    try:
        file = open(os.path.join(sys.path[0], 'database.json'), "r")
        global bd
        bd = json.load(file)
        file.close()
    except BaseException as err:
        Telbot.send_message(TeleId, "Error while opening database:\n" + str(err))

    t2 = threading.Thread( target=init_Tele )
    t1 = threading.Thread( target=init_Vk )
    t1.start()
    t2.start()
    Telbot.send_message(TeleId, "Daemon active...\nBridge established...")
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
