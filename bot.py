from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('77419d30a059875e54864324fe7c4272', config_dict)
# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot("1510403688:AAFrDpYCsMRcrUIYWYr8UhPlsFijttcEvPk", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place( message.text )
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура в районе " + str(int(temp)) + "\n\n"

	if temp <0:
		answer += "Достаточно свежо, лучше одется потеплее"
	elif temp <10:
		answer += "Хоть на улице и плюс, но в шортах ходить еще рано =D"
	elif temp <20:
		answer += "Шорты уже купили?"
	else:
		answer += "Капец, где можно купить карманный кондиционер?"

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )