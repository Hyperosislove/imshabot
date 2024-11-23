from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

# Your bot token from BotFather
BOT_TOKEN = "8034325126:AAFjZaM61RaGrOuxSS0jW-UMHjRNHQ_M65Q"
API_ID = 29882735  # Replace with your actual API ID
API_HASH = "2c1d54d7179a8c1b0ce2d4ace0cbd715"  # Replace with your actual API Hash

# Bot client
bot = Client("video_link_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Function to create inline keyboard with buttons
def create_keyboard():
    buttons = [
        [InlineKeyboardButton("PART1 🔞", url="https://t.me/PAWSOG_bot/PAWS?startapp=2CCfBLTA")],
        [InlineKeyboardButton("PART2 🔞", url="https://t.me/PAWSOG_bot/PAWS?startapp=2CCfBLTA")],
        [InlineKeyboardButton("PART3 🔞", url="https://t.me/PAWSOG_bot/PAWS?startapp=2CCfBLTA")],
        [InlineKeyboardButton("PART4 🔞", url="https://t.me/PAWSOG_bot/PAWS?startapp=2CCfBLTA")],
        [InlineKeyboardButton("PART5 🔞", url="https://t.me/PAWSOG_bot/PAWS?startapp=2CCfBLTA")],
        [InlineKeyboardButton("PART6 🔞", url="https://t.me/PAWSOG_bot/PAWS?startapp=2CCfBLTA")],
        [InlineKeyboardButton("PART7 🔞", url="https://t.me/PAWSOG_bot/PAWS?startapp=2CCfBLTA")]
    ]
    return InlineKeyboardMarkup(buttons)

@bot.on_message(filters.command("start"))
async def start(client, message):
    text = (
        "**Imsha Rehman❤️** ka full video available hai! Click karein aur full video dekhein, sabhi parts available hain 😘🔥🔥🥵🫦🍑\n\n"
        "👇👇👇👇👇👇👇👇👇👇\n\n"
        "**عِمشہ رحمان** ke sabhi parts dekhne ke liye in buttons par click karein 😘🔥🔥🥵🫦🍑\n\n"
        "👇👇👇👇👇👇👇👇👇👇"
    )
    await message.reply(text, reply_markup=create_keyboard())

@bot.on_message(filters.command("menu"))
async def menu(client, message):
    await message.reply("Menu:\n/start - Start the bot")

if __name__ == "__main__":
    bot.run()