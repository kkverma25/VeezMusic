# (C) 2021 VeezMusic-Project

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀʟʟᴏᴡᴤ ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜᴤɪᴄ ᴏɴ ɢʀᴏᴜᴘᴤ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ɴᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ'ᴤ ᴠᴏɪᴄᴇ ᴄʜᴀᴛᴤ!**
💡 **Ḟïṅḋ öüẗ äḷḷ ẗḧë Ḅöẗ'ṡċöṁṁäṅḋṡ äṅḋ ḧöẅ ẗḧëÿ ẅöṛḳ ḅÿ ċḷïċḳïṅġ öṅ ẗḧë**
🔖 **𝐓𝐨 𝐤𝐧𝐨𝐰𝐡𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐜𝐥𝐢𝐜𝐤 𝐨𝐧 𝐭𝐡𝐞❓ 𝐁𝐚𝐬𝐢𝐜 𝐆𝐮𝐢𝐝𝐞 𝐛𝐮𝐭𝐭𝐨𝐧!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("𝐁𝐚𝐬𝐢𝐜", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="cbcmds"),
                    InlineKeyboardButton("𝐎𝐖𝐍𝐄𝐑", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                      "𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞", url="https://github.com/kkverma25/VeezMusic"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 𝐁𝐚𝐬𝐢𝐜 𝐂𝐦𝐝", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐂𝐦𝐝", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 𝐀𝐝𝐦𝐢𝐧 𝐜𝐦𝐝", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 𝐒𝐮𝐝𝐨 𝐜𝐦𝐝", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 𝐎𝐰𝐧𝐞𝐫 𝐜𝐦𝐝", callback_data="cbowner")],
                [InlineKeyboardButton("🔙 𝐆𝐨 𝐁𝐚𝐜𝐤", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the basic commands**

🎧 [ VOICE CHAT PLAY CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the advanced commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the admin commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **after promoting me, type /reload in group to update the admin list.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the video chat first before start to play music.**

📌 **if the userbot not joined to video chat, make sure if the video chat already turned on, or type /leave then type /join again.**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📚 Command List", callback_data="cbhelp")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 **this is the feature information:**
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cblocal"),
                    InlineKeyboardButton("📕 Advanced Cmd", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("📘 Admin Cmd", callback_data="cblamp"),
                    InlineKeyboardButton("📗 Sudo Cmd", callback_data="cblab"),
                ],
                [InlineKeyboardButton("📙 Owner Cmd", callback_data="cbmoon")],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **after promoting me, type /reload in group to update the admin list.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the video chat first before start to play music.**

📌 **if the userbot not joined to video chat, make sure if the video chat already turned on, or type /leave then type /join again.**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the basic commands**

🎧 [ VOICE CHAT PLAY CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the advanced commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the admin commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):
    
    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Command Syntax", callback_data="cmdsyntax")
            ],[
                InlineKeyboardButton("🗑 Close", callback_data="close")
            ]
        ]
    )
    
    nofound = "😕 **couldn't find song you requested**\n\n» **please provide the correct song name or include the artist's name as well**"
    
    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdsyntax"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Command Syntax** to play music on **Voice Chat:**

• `/play (query)` - for playing music via youtube
• `/ytp (query)` - for playing music directly via youtube

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cmdhome")]]
        ),
    )
