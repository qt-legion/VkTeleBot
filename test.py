import vk_api.vk_api, telebot, sys
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = str(sys.argv[1])
vk = vk_api.VkApi(token = str(token))
api = vk.get_api()
longpoll = VkBotLongPoll(vk, "203206891")

Teletoken = str(sys.argv[2])
Telbot = telebot.TeleBot(str(Teletoken))

def write_msg(id, text):
    vk.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

def main():
    Tele = Telbot.send_message("429162266","Jenkins pipeline test message")
    Vk = write_msg("224304301","Jenkins pipeline test message")
    print(Vk)

if __name__ == '__main__':
    main()
