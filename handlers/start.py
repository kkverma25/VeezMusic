from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀʟʟᴏᴡᴤ ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜᴤɪᴄ ᴏɴ ɢʀᴏᴜᴘᴤ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ɴᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ'ᴤ ᴠᴏɪᴄᴇ ᴄʜᴀᴛᴤ!!**

💡 ** Ḟïṅḋ öüẗ äḷḷ ẗḧë Ḅöẗ'ṡċöṁṁäṅḋṡ äṅḋ ḧöẅ ẗḧëÿ ẅöṛḳ ḅÿ ċḷïċḳïṅġ öṅ ẗḧë » 📚 Commands button!**

🔖 **𝐓𝐨 𝐤𝐧𝐨𝐰𝐡𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐜𝐥𝐢𝐜𝐤 𝐨𝐧 𝐭𝐡𝐞❓ 𝐁𝐚𝐬𝐢𝐜 𝐆𝐮𝐢𝐝𝐞 𝐛𝐮𝐭𝐭𝐨𝐧  » !**"""
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒", callback_data="cbcmds"),
                    InlineKeyboardButton("𝐎𝐖𝐍𝐄𝐑", url=f"https://t.me/YOUR_DEVIL_DAD"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 𝐎𝐟𝐟𝐢𝐢𝐚𝐥 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄", url="https://github.com/kkverma25/VeezMusic"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start_group(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "𝐂𝐇𝐀𝐍𝐍𝐋𝐄", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/your_devil_dad)\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing music on your Group voice chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Hello** {message.from_user.mention()} !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="❓ Basic Guide", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
