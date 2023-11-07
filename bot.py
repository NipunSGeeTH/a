import telebot
import requests

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message contains a supported media link (image or video)
    if 'http' in message.text:
        media_link = message.text

        # Determine the media type (image or video)
        if media_link.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            media_type = 'image'
        elif media_link.endswith(('.mp4', '.avi', '.mov', '.webm')):
            media_type = 'video'
        else:
            media_type = None

        # Send the appropriate media if the type is recognized
        if media_type:
            # Download the media from the link
            response = requests.get(media_link, stream=True)

            # Check if the media exists
            if response.status_code == 200:
                # Send the media to the chat
                if media_type == 'image':
                    bot.send_photo(message.chat.id, response.raw.read())
                elif media_type == 'video':
                    bot.send_video(message.chat.id, response.raw.read())
            else:
                # Notify the user that the media could not be downloaded
                bot.send_message(message.chat.id, f'Failed to download the {media_type}.')
        else:
            # If it's not a recognized media link, handle it as a regular message
            bot.send_message(message.chat.id, 'Please send an image or video link.')

bot.polling()
