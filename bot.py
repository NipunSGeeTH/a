import telebot
import requests

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message contains an image link
    if 'http' in message.text and message.text.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Extract the image link from the message
        image_link = message.text

        # Download the image from the link
        response = requests.get(image_link, stream=True)

        # Check if the image exists
        if response.status_code == 200:
            # Send the image to the chat
            bot.send_photo(message.chat.id, response.raw.read())
        else:
            # Notify the user that the image could not be downloaded
            bot.send_message(message.chat.id, 'Failed to download the image.')
    else:
        # If it's not an image link, handle it as a regular message
        bot.send_message(message.chat.id, 'Please send an image link.')

bot.polling()
