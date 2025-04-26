import telebot
import os
import json

# Токен бота из переменной окружения
TOKEN = os.getenv('8100338546:AAGc8L9G13by2oO_OTVGK2aIe0x3HgS6a70')

bot = telebot.TeleBot(8100338546:AAGc8L9G13by2oO_OTVGK2aIe0x3HgS6a70)

# Имя файла для хранения данных
DATA_FILE = 'data.json'

# Функция для загрузки данных
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"income": 0, "expense": 0}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Функция для сохранения данных
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

# Команда старт
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот учёта доходов и расходов.\n\nКоманды:\n/add_income сумма — добавить доход\n/add_expense сумма — добавить расход\n/report — посмотреть отчет")

# Добавление дохода
@bot.message_handler(commands=['add_income'])
def add_income(message):
    try:
        amount = int(message.text.split()[1])
        data = load_data()
        data['income'] += amount
        save_data(data)
        bot.send_message(message.chat.id, f"Доход +{amount} записан!")
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Ошибка! Напиши так: /add_income 1000")

# Добавление расхода
@bot.message_handler(commands=['add_expense'])
def add_expense(message):
    try:
        amount = int(message.text.split()[1])
        data = load_data()
        data['expense'] += amount
        save_data(data)
        bot.send_message(message.chat.id, f"Расход -{amount} записан!")
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Ошибка! Напиши так: /add_expense 500")

# Показать отчет
@bot.message_handler(commands=['report'])
def report(message):
    data = load_data()
    income = data.get('income', 0)
    expense = data.get('expense', 0)
    profit = income - expense
    bot.send_message(message.chat.id, f"Отчёт:\n\nДоход: {income}\nРасход: {expense}\nПрибыль: {profit}")

bot.polling()
