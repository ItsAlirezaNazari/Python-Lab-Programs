import telebot
from telebot import types
import random

bot = telebot.TeleBot("5354607051:AAG7qE1eqUliTS_ApM8FFfzunU6Uoex5zi8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello " + message.from_user.first_name + " ❤️")

attempts = 0
@bot.message_handler(commands=['game'])
def game(message):
	bot.reply_to(message, "Start game, Enter a number 10-20:")
	computer_number = random.randint(10, 20)
	# markup = types.ReplyKeyboardMarkup(row_width=2)
	# itembtn1 = types.KeyboardButton('a')
	# markup.add(itembtn1)
	# bot.send_message(message.chat.id , "Choose one letter:", reply_markup=markup)

	@bot.message_handler(content_types=['text'])
	def check_game(message):
		user_number = int(message.text)
		global attempts
		attempts += 1

		if user_number == computer_number:
			bot.reply_to(message, "Tabrikkkk!! ❤")
			bot.send_message(message.chat.id, "Your attempts:" + str(attempts) + "\nEnd of Game, Come back soon 😉")
		elif user_number < computer_number:
			bot.reply_to(message, "Boro bala ⬆")
		elif user_number > computer_number:
			bot.reply_to(message, "Boro paeen ⬇")




bot.infinity_polling()