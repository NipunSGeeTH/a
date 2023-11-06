import telebot
import requests

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message contains a link
    if 'http' in message.text:
        # Extract the link from the message
        link = message.text.split(' ')[0]

        # Download the file from the link
        response = requests.get(link, stream=True)
        file_name = link.split('/')[-1]

        # Check if the file exists
        if response.status_code == 200:
            # Upload the file to Telegram
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)

            # Send the uploaded file to the chat
            bot.send_document(message.chat.id, open(file_name, 'rb'))
        else:
            # Notify the user that the file could not be downloaded
            bot.send_message(message.chat.id, 'Failed to download the file.')

bot.polling()
