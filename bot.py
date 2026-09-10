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

# ==========================================
# RENDER KEEP-ALIVE WEB SERVER
# ==========================================
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Nahom Digital Work Bot is active and running!")

    def log_message(self, format, *args):
        return

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

# ==========================================
# REUSABLE BUTTONS
# ==========================================
def back_button():
    return [InlineKeyboardButton("⬅️ ወደ ዋናው ገጽ ተመለስ", callback_data="main_menu")]

# ==========================================
# MAIN MENU
# ==========================================
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🔴 Video Editing", callback_data="video_editing")],
        [InlineKeyboardButton("🩵 Graphic Design", callback_data="graphic_design")],
        [InlineKeyboardButton("🍷 Website Developing", callback_data="website_dev")],
        [InlineKeyboardButton("💛 Social Media Management", callback_data="social_media")],
        [InlineKeyboardButton("💚 Prompt Engineering / አማካሪ", callback_data="prompt_eng")],
        [InlineKeyboardButton("☎️ ያናግሩኝ (Contact Me)", callback_data="contact_me")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ==========================================
# START COMMAND
# ==========================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "✨ **Welcome to Nahom Digital Work** ✨\n\n"
        "ስራዎትን ዲጂታል በማድረግ ካሉበት ደረጃ አንድ እርምጃ ከፍ ይበሉ!\n\n"
        "👉 **ስራዎትን ዲጂታል ያድርጉ**\n\n"
        "ከታች ካሉት አገልግሎቶች የሚፈልጉትን ይምረጡ፦"
    )
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=main_menu_keyboard(), parse_mode="Markdown")

# ==========================================
# BUTTON CLICK HANDLERS
# ==========================================
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # ወደ ዋናው ገጽ
    if data == "main_menu":
        welcome_text = (
            "✨ **Welcome to Nahom Digital Work** ✨\n\n"
            "ስራዎትን ዲጂታል በማድረግ ካሉበት ደረጃ አንድ እርምጃ ከፍ ይበሉ!\n\n"
            "👉 **ስራዎትን ዲጂታል ያድርጉ**\n\n"
            "ከታች ካሉት አገልግሎቶች የሚፈልጉትን ይምረጡ፦"
        )
        await query.edit_message_text(welcome_text, reply_markup=main_menu_keyboard(), parse_mode="Markdown")

    # 1. VIDEO EDITING
    elif data == "video_editing":
        text = (
            "🎬 **Video Editing Service**\n\n"
            "ጥራት ያላቸውና ማራኪ የቪዲዮ ኤዲቲንግ ስራዎች።\n\n"
            "የሰነዷቸውን ቪዲዮዎች ለማየት ከታች ያሉትን ሊንኮች ይጫኑ፦"
        )
        keyboard = [
            # ሊንኮቹን በራስህ የቴሌግራም/ቪዲዮ ሊንክ መቀየር ትችላለህ
            [InlineKeyboardButton("👉 የመጀመሪያውን ቪዲዮ ይመልከቱ (Video 1)", url="https://t.me/nahomon")],
            [InlineKeyboardButton("👉 ሁለተኛውን ቪዲዮ ይመልከቱ (Video 2)", url="https://t.me/nahomon")],
            [InlineKeyboardButton("✅ I Choose This One (ይህን መርጫለሁ)", callback_data="contact_me")],
            back_button(),
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 2. GRAPHIC DESIGN
    elif data == "graphic_design":
        text = (
            "🎨 **Graphic Design Service**\n\n"
            "ማራኪና ዘመናዊ የግራፊክስ ዲዛይን ስራዎች።\n\n"
            "የተሰሩ 5 የዲዛይን ናሙናዎችን ለማየት ከታች ያሉትን ሊንኮች ይጎብኙ፦"
        )
        keyboard = [
            # የፎቶዎችህን ሊንክ እዚህ ጋር መተካት ትችላለህ
            [InlineKeyboardButton("🖼️ የዲዛይን ስራ 1 ይመልከቱ", url="https://t.me/nahomon")],
            [InlineKeyboardButton("🖼️ የዲዛይን ስራ 2 ይመልከቱ", url="https://t.me/nahomon")],
            [InlineKeyboardButton("🖼️ የዲዛይን ስራ 3 ይመልከቱ", url="https://t.me/nahomon")],
            [InlineKeyboardButton("🖼️ የዲዛይን ስራ 4 ይመልከቱ", url="https://t.me/nahomon")],
            [InlineKeyboardButton("🖼️ የዲዛይን ስራ 5 ይመልከቱ", url="https://t.me/nahomon")],
            [InlineKeyboardButton("✅ I Choose This One (ይህን መርጫለሁ)", callback_data="contact_me")],
            back_button(),
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 3. WEBSITE DEVELOPING
    elif data == "website_dev":
        text = (
            "💻 **Website Developing Service**\n\n"
            "ዘመናዊ፣ ፈጣን እና ለስልክ ምቹ የሆኑ ድረ-ገጾችን እንገነባለን።\n\n"
            "የተሰሩ የዌብሳይት ፕሮጀክቶችን ከታች ይመልከቱ፦"
        )
        keyboard = [
            [InlineKeyboardButton("🌐 View Web Portfolio", url="https://t.me/nahomon")],
            [InlineKeyboardButton("✅ I Choose This One (ይህን መርጫለሁ)", callback_data="contact_me")],
            back_button(),
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 4. SOCIAL MEDIA MANAGEMENT
    elif data == "social_media":
        text = (
            "💛 **Social Media Management**\n\n"
            "የማህበራዊ ሚዲያ ገጾችዎን ማሳደግ፣ ይዘት ማዘጋጀት እና ማስተዳደር።"
        )
        keyboard = [
            [InlineKeyboardButton("✅ I Choose This One (ይህን መርጫለሁ)", callback_data="contact_me")],
            back_button(),
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 5. PROMPT ENGINEERING / አማካሪ
    elif data == "prompt_eng":
        text = (
            "💚 **Prompt Engineering & AI አማካሪ**\n\n"
            "አርቴፊሻል ኢንተለጀንስን (AI) ለስራዎ በመጠቀም ምርታማነትን ማሳደግ።"
        )
        keyboard = [
            [InlineKeyboardButton("✅ I Choose This One (ይህን መርጫለሁ)", callback_data="contact_me")],
            back_button(),
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 6. CONTACT ME
    elif data == "contact_me":
        contact_text = (
            "☎️ **ያናግሩኝ / Contact Information**\n\n"
            "ስራዎን አብረን ለመጀመር በሚከተሉት አድራሻዎች ያግኙኝ፦\n\n"
            "👤 **Telegram:** @nahomon\n"
            "📞 **ስልክ ቁጥር:** `0900003232`\n"
            "📧 **ኢሜይል:** `tnahom869@gmail.com`\n\n"
            "መልእክትዎን ያስቀምጡ፤ በፍጥነት ምላሽ እሰጣለሁ!"
        )
        keyboard = [
            [InlineKeyboardButton("💬 በቴሌግራም መልእክት ይላኩ", url="https://t.me/nahomon")],
            back_button(),
        ]
        await query.edit_message_text(contact_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("BOT_TOKEN አልተገኘም! እባክዎ Render ላይ BOT_TOKEN መኖሩን ያረጋግጡ።")

    # Render ነፃ ሰርቨር እንዳይዘጋ ዌብ ሰርቨር ማስጀመር
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()

    # ቦቱን ማስነሳት
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Nahom Digital Work Bot በስኬት እየሰራ ነው...")
    app.run_polling()
