import telebot
from telebot import types
from keyboa import Button
from keyboa import Keyboa

token = '6196632156:AAHrs7JnnkIrCxihPE5aPtTz-c9UD_KU1nI'

bot = telebot.TeleBot(token)
months = ['dec','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov']
d_month = None
d_day = None
@bot.message_handler(['date'])
def take_date(message):
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_yes = types.InlineKeyboardButton('Yes', callback_data='yes')
    btn_no = types.InlineKeyboardButton('No', callback_data='no')
    markup.add(btn_yes,btn_no)
    bot.send_message(message.chat.id, f'Would you like to set date? {message.text}', reply_markup=markup)

@bot.callback_query_handler(func=lambda message: True)
def cb(message):
    global d_month
    global d_day
    if message.data == 'yes':
        markup = Keyboa(items=months,items_in_row=3)
        bot.send_message(message.message.chat.id, 'You selected Yes!')
        bot.send_message(message.message.chat.id, 'Set the month', reply_markup=markup())
        bot.delete_message(message.message.chat.id, message.message.message_id)
    elif message.data == 'no':
        bot.send_message(message.message.chat.id, 'You selected No!')
        bot.delete_message(message.message.chat.id, message.message.message_id)
    
    elif message.data in months:
        if message.data == 'feb':
            day_count = 30
        elif message.data in ['apr','jun','sep','nov']:
            day_count = 31
        else:
            day_count = 32
        
        d_month = message.data
        markup = Keyboa(items=list(range(1,day_count)), items_in_row=7)
        bot.send_message(message.message.chat.id, f'You set {message.data}\nSet the day!', reply_markup=markup())
        bot.delete_message(message.message.chat.id, message.message.message_id)
    elif int(message.data) in list(range(1,31)):
        
        d_day = message.data
        bot.send_message(message.message.chat.id, f'You set {d_day}-{d_month}')
        bot.delete_message(message.message.chat.id, message.message.message_id)

bot.infinity_polling()


