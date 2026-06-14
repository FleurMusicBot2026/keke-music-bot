# keke-music-bot
kekemusicbot 
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.getenv("32729712"))
API_HASH = os.getenv("ba2d17f6fd71db636d1599ddc7f22248")
BOT_TOKEN = os.getenv("8614748181:AAGQmkrWfN5zQxFLT7fUWeHQe3DB4T9VSjs")

GROUP_LINK = "https://t.me/WereAllCrazyHere"
OWNER = "@kenox3"

app = Client("MusicBot", api_id=32729712, api_hash=ba2d17f6fd71db636d1599ddc7f22248, bot_token=8614748181:AAGQmkrWfN5zQxFLT7fUWeHQe3DB4T9VSjs)

# 🎵 /start (DM welcome)
@app.on_message(filters.private & filters.command("start"))
async def start(_, m: Message):

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎧 Join Group", url=https://t.me/WereAllCrazyHere)],
        [InlineKeyboardButton("👑 Owner Contact", url=f"https://t.me/{kenox3}")]
    ])

    await m.reply_text(
        f"""🎵 MUSIC BOT WELCOME 🎵

👋 Hello {m.from_user.first_name}

🎧 ဒီ bot က သီချင်းနားထောင်ဖို့ပါ

━━━━━━━━━━━━━━
📌 အသုံးပြုနည်း:
• Bot ကို Group ထဲထည့်ပါ
• Admin ပေးပါ
• /play song name

⚙️ VC ဖွင့်ထားရမယ်
━━━━━━━━━━━━━━
👑 Owner: @{kenox3}
""",
        reply_markup=keyboard
    )

# 👥 group added
@app.on_message(filters.new_chat_members)
async def added(_, m: Message):
    for u in m.new_chat_members:
        if u.is_self:
            await m.reply_text(
                f"""🤖 Thanks for adding me!

⚙️ Setup:
1️⃣ Admin ပေးပါ
2️⃣ Voice Chat ဖွင့်ပါ
3️⃣ /play song name

👑 Owner: @{kenox3}

📩 DM Owner: https://t.me/{kenox3}
"""
            )

# 🎵 play (demo)
@app.on_message(filters.group & filters.command("play"))
async def play(_, m: Message):
    if len(m.command) < 2:
        return await m.reply("❌ သီချင်းနာမည်ထည့်ပါ")

    song = m.text.split(None, 1)[1]

    await m.reply_text(f"🎧 Playing: {song}")

app.run()
