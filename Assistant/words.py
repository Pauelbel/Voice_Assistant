''' Имя бота и его производные '''
TRIGGERS = {
    'шура','шорочка'}



'''
Тренировочная модель для матрицы ИИ
    - Значение ключа начинается с названя функции
    - passive в значении ключа - заглушка (ничего не делает и говорит то, что указано в значении ключа)
'''

data_set = {
# Браузер
'открой браузер':       'browser Открываю браузер',
'браузер':              'browser Открываю браузер',

# Проверить жив ли бот
'как у тебя дела':      'passive не переживай, работаю в фоновом режиме',

# Завершить работу асистента 
'отключись':            'offBot отключаюсь',


}