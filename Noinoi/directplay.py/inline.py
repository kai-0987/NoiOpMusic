from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton,
from pyrogram.types import InlineKeyboardMarkup,
from pyrogram.types import CallbackQuery,



BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⏸", callback_data="pause"),
            InlineKeyboardButton("▶️", callback_data="resume"),
            InlineKeyboardButton("⏹", callback_data="stop"),
            InlineKeyboardButton("🔇", callback_data="mute"),
            InlineKeyboardButton("🔊", callback_data="unmute")
        ],
        [
            InlineKeyboardButton("🗑 Close", callback_data="close")
        ]
    ]
)
