import telebot
import urllib.request

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

def download_media(media_link, media_type, bot, chat_id):
    # Check if the media exists
    try:
        with urllib.request.urlopen(media_link) as response:
            if response.status == 200:
                # Send the media to the chat
                if media_type == 'image':
                    bot.send_photo(chat_id, response.read())
                elif media_type == 'video':
                    bot.send_video(chat_id, response.read())
            else:
                # Notify the user that the media could not be downloaded
                bot.send_message(chat_id, f'Failed to download the {media_type}.')
    except urllib.error.URLError:
        # Handle network errors
        bot.send_message(chat_id, f'Failed to download the {media_type}.')

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
            download_media(media_link, media_type, bot, message.chat.id)
        else:
            # If it's not a recognized media link, handle it as a regular message
            bot.send_message(message.chat.id, 'Please send an image or video link.')

    # Additional functionality
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Hello! I am a bot that can download images and videos.')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'To download an image or video, simply send me the link.')

bot.polling()
