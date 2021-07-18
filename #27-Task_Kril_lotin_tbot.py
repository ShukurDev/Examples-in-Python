from transliterate import to_cyrillic,to_latin
import telebot
TOKEN='1817362650:AAGIpvXId0cBlHAYNpUk8qB5Er4y9OsK2vE'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "ASSALLOMU ALLAYKUM,XUSH KELIBSIZ BOTIMIZGA"
    javob +="\n Matn kiriting: "
    bot.reply_to(message, javob)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    mgj=message.text
    javob = lambda mgj: to_cyrillic(mgj) if mgj.isascii() else to_latin(mgj)
 #   if mgj.isascii():
 #      javob = to_cyrillic(mgj)
  #  else:
   #     javob = to_latin(mgj)
    bot.reply_to(message, javob(mgj))

bot.polling()

#matn=input("Matn kiriting : ")

#if matn.isascii:
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))