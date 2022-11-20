#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👨‍💻 Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n\n📚 Language : <code>Python3</code>\n\n📝 Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n\n📡 ʜᴏsᴛᴇᴅ ᴏɴ : Koyeb\n\n📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/tgnvs>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n🌟 ᴠᴇʀsɪᴏɴ : ᴠ 4.0\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('❤ Donation ', url='https://upier.vercel.app/pay/tgnvs@axisbank')
                    ],[
                        InlineKeyboardButton('〽️ 𝙐𝙥𝙙𝙖𝙩𝙚𝙨', url='https://t.me/tgnvs'),
                        InlineKeyboardButton('🎬 𝙈𝙤𝙫𝙞𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡', url='https://t.me/nvsmovielink')
                    ],[
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
