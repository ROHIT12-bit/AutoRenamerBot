from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config
from helper.database import Botskingdom

async def not_subscribed(_, client, message):
    await Botskingdom.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)
        if user.status == enums.ChatMemberStatus.BANNED:
            return True
        return False
    except UserNotParticipant:
        return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):

    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •",
                url=f"https://t.me/{Config.FORCE_SUB}"
            )
        ]
    ]

    text = (
        "<b>Yᴏᴜ Bᴀᴋᴋᴀᴀ...!!</b>\n\n"
        "<blockquote>Jᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍʏ ʙᴏᴛ.\n"
        "ᴏᴛʜᴇʀᴡɪsᴇ Yᴏᴜ ᴀʀᴇ ɪɴ ʙɪɢ sʜɪᴛ...!!</blockquote>"
    )

    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)

        if user.status == enums.ChatMemberStatus.BANNED:
            return await message.reply_text("Sorry, you are banned from using this bot.")

        buttons.append([
            InlineKeyboardButton(
                text="Cʟɪᴄᴋ ʜᴇʀᴇ",
                url="https://t.me/bot_kingdoms_auto_renamerbot?start=true"
            )
        ])

    except UserNotParticipant:

        if Config.FSUB_PIC:
            return await message.reply_photo(
                photo=Config.FSUB_PIC,
                caption=text,
                reply_markup=InlineKeyboardMarkup(buttons)
            )

        return await message.reply_text(
            "Yᴏᴜ Bᴀᴋᴋᴀᴀ...!!\nJᴏɪɴ ᴘʟᴇᴀsᴇ...",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
