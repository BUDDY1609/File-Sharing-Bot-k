#(Β©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>π¨βπ» Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n\nπ Language : <code>Python3</code>\n\nπ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n\nπ‘ Κα΄sα΄α΄α΄ α΄Ι΄ : Koyeb\n\nπ’ α΄α΄α΄α΄α΄α΄s α΄Κα΄Ι΄Ι΄α΄Κ : <a href=https://t.me/tgnvs>α΄ΚΙͺα΄α΄ Κα΄Κα΄</a>\n\nπ α΄ α΄ΚsΙͺα΄Ι΄ : α΄  4.0\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('β€ Donation ', url='https://upier.vercel.app/pay/tgnvs@axisbank')
                    ],[
                        InlineKeyboardButton('γ½οΈ ππ₯πππ©ππ¨', url='https://t.me/tgnvs'),
                        InlineKeyboardButton('π¬ ππ€π«ππ πΎπππ£π£ππ‘', url='https://t.me/nvsmovielink')
                    ],[
                        InlineKeyboardButton("π Close", callback_data = "close")
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
