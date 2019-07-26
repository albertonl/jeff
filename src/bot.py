import telebot
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
import random

from config.auth import token
from config.ident import unames, rnames

# Names of the bot to use later in regMessageReply()
names = ['bot','jeff','jeffrey','annoyingbot','annoying bot']

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
    bot.reply_to(message,"I am a very dumb bot plz don\'t play too much with me else I will be your worst nightmare :)\nCheck what my father, Alberto, has put in my brain at https://github.com/albertonl/annoyingBot coz it\'s BIG BRAIN TIME")

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

    # Look for bot name in message
    if msg.find("@ImGonnaBeYourWorstNightmareBot")!=-1:
        logger.info('Bot username found in message: \"@ImGonnaBeYourWorstNightmareBot\"')
        bot.reply_to(message,random.choice(specialMessages))
        return

    msg.lower()
    for name in names:
        if msg.find(name)!=-1:
            logger.info('Bot name found in message: \"' + name + '\"')
            # Reply special message
            bot.reply_to(message,random.choice(specialMessages))
            return

    # If no name found, reply to 1/5 of messages
    ran_num = random.randint(1,5)
    if ran_num==1:
        logger.info('No bot name found in message. 20% chance of reply coinciding. Replying random message...')
        # Reply random message
        bot.reply_to(message,random.choice(regMessages))
        return

if __name__=="__main__":
    bot.polling()
