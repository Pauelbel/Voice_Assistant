import sys
import voice

import webbrowser


try:
	import requests		
except:
	pass

def weather():
	'''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
	try:
		params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		voice.speak(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
	except:
		voice.speak('Произошла ошибка при попытке запроса к ресурсу API, проверь код')



def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.youtube.com', new=2)


def offBot():
	'''Отключает бота'''
	voice.speak('Желаю тебе хорошего и продуктивного дня!')
	sys.exit()


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass