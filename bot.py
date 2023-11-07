import telebot
import os
from PIL import Image

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: message.content_type == 'photo')
def handle_image(message):
    # Get the file ID of the image
    file_id = message.photo[-1].file_id

    # Download the image file
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Save the downloaded image temporarily
    temp_image_path = f'temp_{file_id}.jpg'
    with open(temp_image_path, 'wb') as f:
        f.write(downloaded_file)

    # Upscale the image using Pillow
    upscaled_image_path = f'upscaled_{file_id}.jpg'
    upscale_image(temp_image_path, upscaled_image_path)

    # Send the upscaled image to the chat
    with open(upscaled_image_path, 'rb') as f:
        bot.send_photo(message.chat.id, f, caption="Upscaled Image")

    # Delete temporary files
    os.remove(temp_image_path)
    os.remove(upscaled_image_path)

def upscale_image(input_path, output_path):
    # Open the image
    original_image = Image.open(input_path)

    # Upscale the image by a factor of 2 using nearest neighbor interpolation
    upscaled_image = original_image.resize((original_image.width * 2, original_image.height * 2), Image.NEAREST)

    # Save the upscaled image
    upscaled_image.save(output_path)

bot.polling()
