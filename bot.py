import telebot

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    # Create an inline keyboard markup
    keyboard = telebot.types.InlineKeyboardMarkup()
    hi_button = telebot.types.InlineKeyboardButton(text="Hi", callback_data="hi_button")
    keyboard.add(hi_button)

    # Send the welcome message with inline keyboard
    bot.send_message(message.chat.id, 'Hi! Click the button below to greet me.', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "hi_button")
def handle_hi_button_click(call):
    bot.send_message(call.message.chat.id, "Hi there! How can I help you today?")

bot.polling()
