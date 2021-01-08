#coding:utf-8

from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

chatbot = ChatBot('Training demo')
trainer = ListTrainer(chatbot)
trainer.train([
    '你好',
    '很高兴认识你',
    '你叫什么名字',
    '我叫xxx'
])

print (chatbot.get_response('你好？'))
print (chatbot.get_response('你叫什么名字？'))

# chatbot = ChatBot('Charlie',
#                   #trainer='charrerbot.trainers.ChatterBotCorpusTraier'
#                    )

bot = Bot()
my_friend = ensure_one(bot.search('name'))

@bot.register(my_friend, except_self=True)
def reply_msg(msg):
    print ('1', msg.text)
    response = chatbot.get_response(msg.text)
    msg.reply(response)

embed()
