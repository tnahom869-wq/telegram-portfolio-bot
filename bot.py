import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


# =========================
# MAIN MENU
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🎨 View My Portfolio",
                callback_data="portfolio"
            )
        ],
        [
            InlineKeyboardButton(
                "👤 About Me",
                callback_data="about"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 Contact Me",
                callback_data="contact"
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to Nahom's Digital Portfolio!\n\n"
        "Choose an option below:",
        reply_markup=reply_markup
    )


# =========================
# BUTTON HANDLER
# =========================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    # PORTFOLIO MENU
    if query.data == "portfolio":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🎬 Video Editing",
                    callback_data="video_editing"
                )
            ],
            [
                InlineKeyboardButton(
                    "🎨 Graphic Design",
                    callback_data="graphic_design"
                )
            ],
            [
                InlineKeyboardButton(
                    "💻 Website Development",
                    callback_data="website_development"
                )
            ],
            [
                InlineKeyboardButton(
                    "🤖 Prompt Engineering",
                    callback_data="prompt_engineering"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Back to Main Menu",
                    callback_data="main_menu"
                )
            ],
        ]

        await query.edit_message_text(
            "🎨 My Portfolio\n\n"
            "Select a category:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # VIDEO EDITING
    elif query.data == "video_editing":

        await query.edit_message_text(
            "🎬 Video Editing Portfolio\n\n"
            "My video editing projects will appear here.\n\n"
            "📹 Video 1\n"
            "📹 Video 2\n"
            "📹 Video 3\n\n"
            "More projects coming soon!"
        )


    # GRAPHIC DESIGN
    elif query.data == "graphic_design":

        await query.edit_message_text(
            "🎨 Graphic Design Portfolio\n\n"
            "My graphic design projects will appear here.\n\n"
            "🖼️ Social Media Design\n"
            "🖼️ Poster Design\n"
            "🖼️ Branding Design"
        )


    # WEBSITE DEVELOPMENT
    elif query.data == "website_development":

        await query.edit_message_text(
            "💻 Website Development Portfolio\n\n"
            "My website projects will appear here.\n\n"
            "🌐 Website Project 1\n"
            "🌐 Website Project 2"
        )


    # PROMPT ENGINEERING
    elif query.data == "prompt_engineering":

        await query.edit_message_text(
            "🤖 Prompt Engineering Portfolio\n\n"
            "My AI and Prompt Engineering projects will appear here."
        )


    # ABOUT ME
    elif query.data == "about":

        await query.edit_message_text(
            "👤 About Me\n\n"
            "Hello! My name is Nahom.\n\n"
            "🎬 Video Editor\n"
            "🎨 Graphic Designer\n"
            "💻 Website Developer\n"
            "🤖 Prompt Engineer\n\n"
            "Welcome to my professional digital portfolio!"
        )


    # CONTACT
    elif query.data == "contact":

        await query.edit_message_text(
            "📞 Contact Me\n\n"
            "Telegram: @YOUR_USERNAME\n"
            "Phone: +251 XXX XXX XXX"
        )


    # BACK TO MAIN MENU
    elif query.data == "main_menu":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🎨 View My Portfolio",
                    callback_data="portfolio"
                )
            ],
            [
                InlineKeyboardButton(
                    "👤 About Me",
                    callback_data="about"
                )
            ],
            [
                InlineKeyboardButton(
                    "📞 Contact Me",
                    callback_data="contact"
                )
            ],
        ]

        await query.edit_message_text(
            "👋 Welcome to Nahom's Digital Portfolio!\n\n"
            "Choose an option below:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# =========================
# RUN BOT
# =========================

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running...")

app.run_polling()
