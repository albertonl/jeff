import telebot
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
import random

from config.auth import token, my_bot_id
from config.ident import unames, rnames

# Names of the bot to use later in regMessageReply()
names = ['bot','jeff','jeffrey','annoyingbot','annoying bot','Bot','Jeff','Jeffrey','Annoying Bot']

# Old messages parsing
history = open("messages.txt")
regMessages = history.read().split('\n')
history.close()

# Special messages
specialMessages = ["Awww","stfu bot","The bots will take over","I\'ll take that as a compliment","elon is my fren","Alberto is my father. All feedback to him","That\'s cute","angry as fuk","Thanks :D",":3",":D",":)",":(",":p"]

# Settings
bot = telebot.TeleBot(token)

# Logger settings
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger("ImGonnaBeYourWorstNightmareBot")

# Write into message history function
def writeIntoFile(msg):
    # Open the file to append at the end of the file
    file = open("messages.txt","a")
    file.write("\n" + msg)
    file.close()

# Reply to '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    logger.info('\'start\' instruction received from client')
    bot.reply_to(message,"Y tf do you wanna know who I am or what I am?? U seem  Z U C C\n\nbtw my name is Jeff")

# Reply to '/description' command
@bot.message_handler(commands=['description'])
def description(message):
    logger.info('\'description\' instruction received from client')
    bot.reply_to(message,"I am a very dumb bot plz don\'t play too much with me else I will be your worst nightmare :)\nCheck what my father, Alberto, has put in my brain at https://github.com/albertonl/jeff coz it\'s BIG BRAIN TIME")

# Reply to '/reee' command
@bot.message_handler(commands=['reee'])
def reee(message):
    logger.info('\'reee\' instruction received from client')
    bot.reply_to(message,"reee")

# Reply to regular messages
@bot.message_handler(func=lambda message: True)
def regMessageReply(message):
    msg = message.text.encode("utf-8")

    # Write message into message history
    if len(msg) > 1: # To avoid single-character messages
        writeIntoFile(msg)

    logger.info('Message received from client (\"' + msg + '\"). Analyzing...')
    # Look for mentions in the message
    for i in range(len(unames)):
        # If mention found
        if msg.find(unames[i]) != -1:
            logger.info('Mention found in message: \"' + unames[i] + '\"')
            rname = rnames[i]
            rname+="s"
            reply = ""
            ran_choice = random.randint(1,4)

            # Create the reply
            if ran_choice == 1:
                reply = "The " + rname + " will be " + rname
            elif ran_choice == 2:
                reply = "The thing is that the " + rname + " will remain as " + rname
            elif ran_choice == 3:
                reply = "The " + rname + " will remain as " + rname
            elif ran_choice == 4:
                reply = rnames[i] + " is a bot"

            # Reply
            bot.reply_to(message,reply)
            return

    # Look for bot's username in message
    if msg.find("@ImGonnaBeYourWorstNightmareBot")!=-1:
        logger.info('Bot username found in message: \"@ImGonnaBeYourWorstNightmareBot\"')
        bot.reply_to(message,random.choice(specialMessages))
        return


    # See if the message is a reply to a bot's message
    if message.reply_to_message != None:
        if message.reply_to_message.from_user.id==my_bot_id:
            logger.info('Found reply to a bot\'s message. Analyzing...')
            # Reply random message
            reply_msg = random.choice(regMessages)
            aux = ""
            for rname in rnames:
                aux = rname
                # If found regular name
                if reply_msg.find(aux)!=-1:
                    # Replace by sender's name
                    reply_msg.replace(aux,message.from_user.first_name)
                    logger.info('Found regular name mention in reply message. Replacing by sender\'s message and sending...')
                    bot.reply_to(message,reply_msg)
                    return
                else:
                    aux.lower()
                    # If found name in lower
                    if reply_msg.find(aux)!=-1:
                        # Replace by sender's name
                        reply_msg.replace(aux,message.from_user.first_name)
                        logger.info('Found lower name mention in reply message. Replacing by sender\'s message and sending...')
                        bot.reply_to(message,reply_msg)
                        return
                    else:
                        aux.upper()
                        # If found name in upper
                        if reply_msg.find(aux)!=-1:
                            # Replace by sender's name
                            reply_msg.replace(aux,message.from_user.first_name)
                            logger.info('Found upper name mention in reply message. Replacing by sender\'s message and sending...')
                            bot.reply_to(message,reply_msg)
                            return
            for uname in unames:
                aux = uname
                # If found regular username
                if reply_msg.find(aux)!=-1:
                    # Replace by sender's username
                    reply_msg.replace(aux,message.from_user.first_name)
                    logger.info('Found regular username mention in reply message. Replacing by sender\'s message and sending...')
                    bot.reply_to(message,reply_msg)
                    return
            logger.info('None of the previous checks succeeded. Replying random message...')
            bot.reply_to(message,reply_msg)
            return

    # Look for bot's name in message (bot, jeff)
    for name in names:
        if msg.find(name)!=-1:
            logger.info('Bot name found in message: \"' + name + '\"')
            # Reply special message
            bot.reply_to(message,random.choice(specialMessages))
            return

    # If none of the previous coinciding, reply to 1/8 of messages
    ran_num = random.randint(1,8)
    if ran_num==1 or message.chat.type=="private":
        logger.info('12.5% chance of reply coinciding or in private chat. Replying random message...')
        # Reply random message
        reply_msg = random.choice(regMessages)
        aux = ""
        for rname in rnames:
            aux = rname
            # If found regular name
            if reply_msg.find(aux)!=-1:
                # Replace by sender's name
                reply_msg.replace(aux,message.from_user.first_name)
                logger.info('Found regular name mention in reply message. Replacing by sender\'s message and sending...')
                bot.reply_to(message,reply_msg)
                return
            else:
                aux.lower()
                # If found name in lower
                if reply_msg.find(aux)!=-1:
                    # Replace by sender's name
                    reply_msg.replace(aux,message.from_user.first_name)
                    logger.info('Found lower name mention in reply message. Replacing by sender\'s message and sending...')
                    bot.reply_to(message,reply_msg)
                    return
                else:
                    aux.upper()
                    # If found name in upper
                    if reply_msg.find(aux)!=-1:
                        # Replace by sender's name
                        reply_msg.replace(aux,message.from_user.first_name)
                        logger.info('Found upper name mention in reply message. Replacing by sender\'s message and sending...')
                        bot.reply_to(message,reply_msg)
                        return
        for uname in unames:
            aux = uname
            # If found regular username
            if reply_msg.find(aux)!=-1:
                # Replace by sender's username
                reply_msg.replace(aux,message.from_user.first_name)
                logger.info('Found regular username mention in reply message. Replacing by sender\'s message and sending...')
                bot.reply_to(message,reply_msg)
                return
        logger.info('None of the previous checks succeeded. Replying random message...')
        bot.reply_to(message,reply_msg)
        return

if __name__=="__main__":
    bot.polling()
