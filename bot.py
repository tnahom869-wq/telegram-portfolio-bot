import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔴 የቦት ቶከን
BOT_TOKEN = os.getenv("BOT_TOKEN", "8801548850:AAFG2WMsUoEqFxgBwQbLNF_dCOsIF0a5dBY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 1. ቋንቋ መምረጫ Buttons
lang_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data="lang_en")],
    [InlineKeyboardButton(text="🌳 Afaan Oromoo", callback_data="lang_om")],
    [InlineKeyboardButton(text="🇪🇹 አማርኛ", callback_data="lang_am")]
])

# 2. ዋናው Menu (Service Buttons)
def get_main_menu(lang="am"):
    btn_video = "🎬 Video Editing"
    btn_graphic = "🎨 Graphic Design"
    btn_web = "💻 Website Developing"
    btn_social = "📱 Social Media Management"
    btn_prompt = "🤖 Prompt Engineering"
    btn_contact = "📞 Contact Me"

    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=btn_video, callback_data="srv_video")],
        [InlineKeyboardButton(text=btn_graphic, callback_data="srv_graphic")],
        [InlineKeyboardButton(text=btn_web, callback_data="srv_web")],
        [InlineKeyboardButton(text=btn_social, callback_data="srv_social")],
        [InlineKeyboardButton(text=btn_prompt, callback_data="srv_prompt")],
        [InlineKeyboardButton(text=btn_contact, callback_data="srv_contact")]
    ])

# 3. የአገልግሎት ማሳያ (Portfolio & Choose Buttons)
def get_service_menu(service_type):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👁 View My Portfolio", callback_data=f"port_{service_type}")],
        [InlineKeyboardButton(text="✅ I Choose This", callback_data="srv_contact")],
        [InlineKeyboardButton(text="🔙 ወደ ዋና ገጽ", callback_data="back_main")]
    ])

# 4. የቪዲዮ ኤዲቲንግ ሊንኮች Buttons
video_portfolio_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎬 ቪዲዮ ፕሮጀክት 1 (ይመልከቱ)", url="https://t.me/NAMINET00/77")],
    [InlineKeyboardButton(text="🎬 ቪዲዮ ፕሮጀክት 2 (ይመልከቱ)", url="https://t.me/NAMINET00/78")],
    [InlineKeyboardButton(text="✅ ይህንን አገልግሎት እፈልጋለሁ", callback_data="srv_contact")],
    [InlineKeyboardButton(text="🔙 ተመለስ", callback_data="srv_video")]
])

# 5. የግራፊክ ዲዛይን ሊንኮች Buttons (5ቱ ሊንኮች)
graphic_portfolio_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎨 ዲዛይን 1", url="https://t.me/NAMINET00/71")],
    [InlineKeyboardButton(text="🎨 ዲዛይን 2", url="https://t.me/NAMINET00/69")],
    [InlineKeyboardButton(text="🎨 ዲዛይን 3", url="https://t.me/NAMINET00/54")],
    [InlineKeyboardButton(text="🎨 ዲዛይን 4", url="https://t.me/NAMINET00/35")],
    [InlineKeyboardButton(text="🎨 ዲዛይን 5", url="https://t.me/NAMINET00/15")],
    [InlineKeyboardButton(text="✅ ይህንን አገልግሎት እፈልጋለሁ", callback_data="srv_contact")],
    [InlineKeyboardButton(text="🔙 ተመለስ", callback_data="srv_graphic")]
])

# /start ሲባል የሚመጣው
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "✨ **Welcome to Nahom Digital Work** ✨\n\n"
        "እንኳን በሰላም ወደ Nahom Digital Work በሰላም መጣችሁ!\n"
        "እባክዎ ቋንቋ ይምረጡ / Please select your preferred language:"
    )
    await message.answer(text, reply_markup=lang_keyboard, parse_mode="Markdown")

# ቋንቋ ሲመረጥ
@dp.callback_query(F.data.startswith("lang_"))
async def handle_lang(callback: types.CallbackQuery):
    lang = callback.data.split("_")[1]
    
    welcome_text = "በድጋሚ እንኳን በሰላም መጣችሁ!\n\n" if lang == "am" else "Welcome Again!\n\n"
    
    text = (
        f"👋 **{welcome_text}**"
        "እኔ **ናሆም ተስፋዬ (Nahom Tesfaye)** እባላለሁ።\n"
        "• Video Editor\n"
        "• Graphic Designer\n"
        "• Website Developer\n"
        "• Social Media Manager\n"
        "• Prompt Engineer ነኝ።\n\n"
        "📌 **ለዚህ ስራ ለመስራት እና የእናንተን ካምፓኒ አንድ ደረጃ ከፍ ለማድረግ ስለመጣችሁ እናመሰግናለን።**\n"
        "✔ ድርጅቶን በዘመናዊ ዲጂታል ቴክኖሎጂ እናሳድጋለን።\n"
        "✔ ጥራት ያላቸው ማስታወቂያዎችንና ቪዲዮዎችን እንሰራለን።\n"
        "✔ ዘመናዊ ድረ-ገጾችን እና የ AI ሲስተሞችን እንገነባለን።\n\n"
        "🚀 _\"ስራዎትን... ድርጅቶን ዲጂታል ለማድረግ ዝግጁ ነን!\"_\n\n"
        "የሚፈልጉትን አገልግሎት ከታች ይምረጡ 👇"
    )
    await callback.message.edit_text(text, reply_markup=get_main_menu(lang), parse_mode="Markdown")

# ዋና ገጽ መመለሻ
@dp.callback_query(F.data == "back_main")
async def back_to_main(callback: types.CallbackQuery):
    text = "🚀 **Nahom Digital Work ዋና ማውጫ**\n\nየሚፈልጉትን አገልግሎት ይምረጡ፡"
    await callback.message.edit_text(text, reply_markup=get_main_menu("am"), parse_mode="Markdown")

# Video Editing ሲነካ
@dp.callback_query(F.data == "srv_video")
async def srv_video(callback: types.CallbackQuery):
    text = (
        "🎬 **Video Editing Service**\n\n"
        "ፕሮፌሽናል የቪዲዮ ኤዲቲንግ፣ ማስታወቂያዎች፣ ሪልስ እና ዩቲዩብ ቪዲዮዎችን በጥራት እንሰራለን።\n\n"
        "ስራዎቼን ማየት ይፈልጋሉ ወይስ አገልግሎቱን መምረጥ?"
    )
    await callback.message.edit_text(text, reply_markup=get_service_menu("video"), parse_mode="Markdown")

# Graphic Design ሲነካ
@dp.callback_query(F.data == "srv_graphic")
async def srv_graphic(callback: types.CallbackQuery):
    text = (
        "🎨 **Graphic Design Service**\n\n"
        "ማራኪ ፖስተሮች፣ ሎጎ፣ ባነሮች እና የብራንዲንግ ስራዎችን እንሰራለን።\n\n"
        "ስራዎቼን ማየት ይፈልጋሉ ወይስ አገልግሎቱን መምረጥ?"
    )
    await callback.message.edit_text(text, reply_markup=get_service_menu("graphic"), parse_mode="Markdown")

# ሌሎቹ አገልግሎቶች (Website, Social Media, Prompt)
@dp.callback_query(F.data.in_(["srv_web", "srv_social", "srv_prompt"]))
async def srv_others(callback: types.CallbackQuery):
    srv_names = {
        "srv_web": "💻 Website Developing",
        "srv_social": "📱 Social Media Management",
        "srv_prompt": "🤖 Prompt Engineering"
    }
    srv_name = srv_names[callback.data]
    text = f"✨ **{srv_name}**\n\nይህንን አገልግሎት ለመጀመር እና ለማዘዝ ከታች ያለውን ይጫኑ፡"
    await callback.message.edit_text(text, reply_markup=get_service_menu("other"), parse_mode="Markdown")

# Portfolio ማሳያ (Video)
@dp.callback_query(F.data == "port_video")
async def port_video(callback: types.CallbackQuery):
    text = (
        "🎬 **የቪዲዮ ኤዲቲንግ ስራዎች ማሳያ (Portfolio)** 🎬\n\n"
        "ከታች ያሉትን ሊንኮች በመጫን በቴሌግራም ቻናሌ የተሰሩ ስራዎችን መመልከት ትችላላችሁ 👇"
    )
    await callback.message.edit_text(text, reply_markup=video_portfolio_kb, parse_mode="Markdown")

# Portfolio ማሳያ (Graphic Design)
@dp.callback_query(F.data == "port_graphic")
async def port_graphic(callback: types.CallbackQuery):
    text = (
        "🎨 **የግራፊክ ዲዛይን ስራዎች ማሳያ (Portfolio)** 🎨\n\n"
        "የተሰሩ 5ቱን ምርጥ ዲዛይኖች ከታች ያሉትን በተኖች በመጫን ይመልከቱ 👇"
    )
    await callback.message.edit_text(text, reply_markup=graphic_portfolio_kb, parse_mode="Markdown")

# Contact Me ገጽ
@dp.callback_query(F.data == "srv_contact")
async def srv_contact(callback: types.CallbackQuery):
    text = (
        "📞 **ያግኙኝ / Contact Me**\n\n"
        "ስራ ለማሰራት፣ ለማማከር ወይም አብረን ለመስራት በሚከተሉት አድራሻዎች በቀጥታ ልታገኙኝ ትችላላችሁ፡\n\n"
        "✈️ **Telegram:** @NahomOn\n"
        "📞 **Phone:** `0900003230`\n"
        "✉️ **Email:** `tnahom869@gmail.com`\n\n"
        "መልእክትዎን በቴሌግራም ቢያስቀምጡልኝ በፍጥነት እመልሳለሁ!"
    )
    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 ቀጥታ ቴሌግራም ላይ አናግረኝ", url="https://t.me/NahomOn")],
        [InlineKeyboardButton(text="🔙 ወደ ዋና ገጽ ተመለስ", callback_data="back_main")]
    ])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")

async def main():
    print("🚀 ቦቱ ስራ ጀምሯል...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
