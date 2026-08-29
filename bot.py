import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


# =========================
# SIMPLE RENDER WEB SERVER
# =========================

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Telegram Portfolio Bot is running!")

    def log_message(self, format, *args):
        return


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


# =========================
# MAIN MENU
# =========================

def main_menu():
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

    return InlineKeyboardMarkup(keyboard)


# =========================
# START COMMAND
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Nahom's Digital Portfolio!\n\n"
        "Choose an option below:",
        reply_markup=main_menu()
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
            "🎨 My Portfolio\n\nSelect a category:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # VIDEO EDITING
    elif query.data == "video_editing":

        await query.edit_message_text(
            "🎬 Video Editing Portfolio\n\n"
            "📹 My video editing projects will appear here.\n\n"
            "Video files will be added soon!"
        )

    # GRAPHIC DESIGN
    elif query.data == "graphic_design":

        await query.edit_message_text(
            "🎨 Graphic Design Portfolio\n\n"
            "🖼️ My graphic design projects will appear here."
        )

    # WEBSITE DEVELOPMENT
    elif query.data == "website_development":

        await query.edit_message_text(
            "💻 Website Development Portfolio\n\n"
            "🌐 My website projects will appear here."
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

    # CONTACT ME
    elif query.data == "contact":

        await query.edit_message_text(
            "📞 Contact Me\n\n"
            "Name: Nahom\n"
            "Telegram: @nahomon\n"
            "Phone: 0900023230"
        )

    # BACK TO MAIN MENU
    elif query.data == "main_menu":

        await query.edit_message_text(
            "👋 Welcome to Nahom's Digital Portfolio!\n\n"
            "Choose an option below:",
            reply_markup=main_menu()
        )


# =========================
# RUN BOT
# =========================

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")


# Start Render health check server
web_thread = threading.Thread(
    target=run_web_server,
    daemon=True
)

web_thread.start()


# Start Telegram bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Telegram Portfolio Bot is running...")

app.run_polling()
