import telebot
import sympy as sp

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

# Define callback data patterns
NUMBER_PATTERN = r"number_(\d)"
OPERATOR_PATTERN = r"operator_([\+\-\*\/])"
PARENTHESIS_PATTERN = r"parenthesis_(\(\))"

# Define inline keyboard buttons
number_buttons = [
    [telebot.types.InlineKeyboardButton(text=str(i), callback_data=f"number_{i}") for i in range(1, 10)],
    [telebot.types.InlineKeyboardButton(text="0", callback_data="number_0")],
]

operator_buttons = [
    [telebot.types.InlineKeyboardButton(text="+", callback_data="operator_+")],
    [telebot.types.InlineKeyboardButton(text="-", callback_data="operator_-")],
    [telebot.types.InlineKeyboardButton(text="*", callback_data="operator_*")],
    [telebot.types.InlineKeyboardButton(text="/", callback_data="operator_/")],
]

parenthesis_buttons = [
    [telebot.types.InlineKeyboardButton(text="(", callback_data="parenthesis_(")],
    [telebot.types.InlineKeyboardButton(text=")", callback_data="parenthesis_)")],
]

# Combine buttons into a single keyboard
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.add(*number_buttons)
keyboard.add(*operator_buttons)
keyboard.add(*parenthesis_buttons)

# Define initial message
initial_message = "Enter a mathematical expression:"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Send the initial message with inline keyboard
    bot.send_message(message.chat.id, initial_message, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Get the callback data
    callback_data = call.data

    # Process the callback data based on its pattern
    if re.match(NUMBER_PATTERN, callback_data):
        # Append the number to the current expression
        current_expression += callback_data.split("_")[1]
    elif re
