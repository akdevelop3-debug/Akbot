import os
import threading
import telebot
from telebot import types
from flask import Flask
import requests
from bs4 import BeautifulSoup

# 1. ሬንደር እንዳይተኛ ፍላስክ ሰርቨር ማዘጋጀት
app = Flask('')

@app.route('/')
def home():
    return "AK DEVELOP ORDER CENTER BOT IS ALIVE!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# 2. ከሬንደር ኢንቫይሮመንት ላይ ምስጢራዊ ቁልፎችን መሳብ
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")

bot = telebot.TeleBot(BOT_TOKEN)

# የተጠቃሚዎችን የሂደት ሁኔታ መመዝገቢያ (Memory)
user_states = {}

# 3. የሁለቱ ቋንቋዎች የጽሑፍ ማውጫ (UI Texts)
TEXTS = {
    'am': {
        'welcome': "👋 እንኳን ወደ AK DEVELOP ማዘዣ ማዕከል በደህና መጡ! እባክዎ ቋንቋ ይምረጡ፦",
        'main_menu_txt': "🗂️ ዋና ማውጫ፦ ምን ማዘዝ ይፈልጋሉ? ከታች ያሉትን በተኖች ይጠቀሙ::",
        'username_prompt': "🔗 እባክዎ የአካውንቱን ሊንክ ወይም የተጠቃሚ ስም (Username) ያስገቡልን፦",
        'success_order': "🎉 ትዕዛዝዎ በተሳካ ሁኔታ ተመዝግቧል! አድሚኖቻችን በቅርቡ ያነጋግሩዎታል:: 😊",
        'feedback_prompt': "✍️ እባክዎ የሎትኝን አስተያየት ወይም ቅሬታ እዚህ ይጻፉልን፦",
        'tg_contact_prompt': "🆔 እባክዎ እርስዎን የምናገኝበትን የራስዎን የቴሌግራም ዩዘርኔም (ምሳሌ፦ @username) ያስገቡ፦",
        'choose_plat': "📱 እባክዎ የሶሻል ሚዲያ ፕላትፎርም ይምረጡ፦"
    },
    'en': {
        'welcome': "👋 Welcome to AK DEVELOP Order Center! Please choose a language:",
        'main_menu_txt': "🗂️ Main Menu: What would you like to order? Use the buttons below.",
        'username_prompt': "🔗 Please enter the account link or username:",
        'success_order': "🎉 Your order has been successfully logged! Our team will contact you shortly. 😊",
        'feedback_prompt': "✍️ Please write your feedback or complaint here:",
        'tg_contact_prompt': "🆔 Please enter your personal Telegram username so we can contact you (e.g., @username):",
        'choose_plat': "📱 Please select a social media platform:"
    }
}

# --- ⚙️ የኪቦርድ በተኖች መገንቢያዎች ---

def get_lang_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("አማርኛ 🇪🇹", callback_data="lang_am"),
        types.InlineKeyboardButton("English 🇬🇧", callback_data="lang_en")
    )
    return markup

def get_main_keyboard(lang):
    # 🌟 ማሻሻያ፦ ከጽሑፍ መጻፊያው ስር ውብ እና እጥፍጥፍ ያለ ኪቦርድ መሥራት
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if lang == 'am':
        btn1 = types.KeyboardButton("📱 ሶሻል ሚዲያ ማስተዋወቅ")
        btn2 = types.KeyboardButton("🔄 ፕሮሞሽን እና ሪሴል")
        btn3 = types.KeyboardButton("✍️ አስተያየት ለመስጠት")
    else:
        btn1 = types.KeyboardButton("📱 Social Media Promotion")
        btn2 = types.KeyboardButton("🔄 Promotion & Resell")
        btn3 = types.KeyboardButton("✍️ Give Feedback")
    markup.add(btn1, btn2)
    markup.add(btn3)
    return markup

def get_platform_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("Telegram ✈️", callback_data="plat_telegram"),
        types.InlineKeyboardButton("TikTok 🎵", callback_data="plat_tiktok"),
        types.InlineKeyboardButton("Instagram 📸", callback_data="plat_instagram"),
        types.InlineKeyboardButton("YouTube 📺", callback_data="plat_youtube")
    )
    return markup

def check_lang(message):
    uid = message.chat.id
    if uid not in user_states or 'lang' not in user_states[uid]:
        user_states[uid] = {'lang': 'am', 'state': ''}
        bot.send_message(uid, TEXTS['am']['welcome'], reply_markup=get_lang_keyboard())
        return False
    return True

# --- 🔍 የሶሻል ሚዲያ መረጃ መበዝበዣ (Web Scraping) ---

def fetch_social_profile(platform, target):
    url = target.strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        clean_name = target.replace('@', '').strip()
        if platform == 'tiktok':
            url = f"https://www.tiktok.com/@{clean_name}"
        elif platform == 'instagram':
            url = f"https://www.instagram.com/{clean_name}/"
        elif platform == 'youtube':
            url = f"https://www.youtube.com/@{clean_name}"
        else:
            return None, None, None

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        res = requests.get(url, headers=headers, timeout=7)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            og_title = soup.find("meta", property="og:title")
            og_desc = soup.find("meta", property="og:description")
            og_image = soup.find("meta", property="og:image")
            
            title = og_title["content"] if og_title else (soup.title.string if soup.title else "Social Account")
            desc = og_desc["content"] if og_desc else "No bio available."
            image_url = og_image["content"] if og_image else None
            
            return title.strip(), desc.strip(), image_url
    except Exception:
        pass
    return None, None, None

# --- 🚀 የቦቱ መልዕክት ተቀባዮች (Handlers) ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    uid = message.chat.id
    user_states[uid] = {'lang': 'am', 'state': ''}
    bot.send_message(uid, TEXTS['am']['welcome'], reply_markup=get_lang_keyboard())

@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def set_language(call):
    uid = call.message.chat.id
    lang = call.data.split('_')[1]
    user_states[uid] = {'lang': lang, 'state': ''}
    bot.delete_message(uid, call.message.message_id)
    bot.send_message(uid, TEXTS[lang]['main_menu_txt'], reply_markup=get_main_keyboard(lang))

@bot.message_handler(func=lambda m: m.text in ["📱 ሶሻል ሚዲያ ማስተዋወቅ", "📱 Social Media Promotion", "🔄 ፕሮሞሽን እና ሪሴል", "🔄 Promotion & Resell"])
def route_services(message):
    if not check_lang(message): return
    uid = message.chat.id
    lang = user_states[uid]['lang']
    
    user_states[uid]['service'] = 'Promotion' if "ማስተዋወቅ" in message.text or "Promotion" in message.text else 'Resell'
    bot.send_message(uid, TEXTS[lang]['choose_plat'], reply_markup=get_platform_keyboard())

@bot.message_handler(func=lambda m: m.text in ["✍️ አስተያየት ለመስጠት", "✍️ Give Feedback"])
def route_feedback(message):
    if not check_lang(message): return
    uid = message.chat.id
    lang = user_states[uid]['lang']
    user_states[uid]['state'] = 'waiting_feedback'
    bot.send_message(uid, TEXTS[lang]['feedback_prompt'])

@bot.callback_query_handler(func=lambda call: call.data.startswith('plat_'))
def set_platform(call):
    uid = call.message.chat.id
    platform = call.data.split('_')[1]
    user_states[uid]['platform'] = platform
    user_states[uid]['state'] = 'waiting_username_lookup'
    lang = user_states[uid]['lang']
    bot.delete_message(uid, call.message.message_id)
    bot.send_message(uid, TEXTS[lang]['username_prompt'])

@bot.callback_query_handler(func=lambda call: call.data.startswith('verifyacc_'))
def verify_account(call):
    uid = call.message.chat.id
    action = call.data.split('_')[1]
    lang = user_states[uid]['lang']
    bot.delete_message(uid, call.message.message_id)
    
    if action == 'yes':
        user_states[uid]['state'] = 'waiting_tg_username'
        bot.send_message(uid, TEXTS[lang]['tg_contact_prompt'])
    else:
        user_states[uid]['state'] = ''
        bot.send_message(uid, TEXTS[lang]['main_menu_txt'], reply_markup=get_main_keyboard(lang))

@bot.message_handler(func=lambda m: True, content_types=['text'])
def handle_text_inputs(message):
    uid = message.chat.id
    text = message.text

    if not check_lang(message): return

    lang = user_states[uid]['lang']
    state = user_states[uid].get('state', '')

    if state == 'waiting_feedback':
        bot.send_message(ADMIN_ID, f"✍️ NEW FEEDBACK:\n\nUser ID: {uid}\nContent: {text}")
        user_states[uid] = {'lang': lang}
        bot.send_message(uid, TEXTS[lang]['success_order'], reply_markup=get_main_keyboard(lang))
        return

    if state == 'waiting_username_lookup':
        target_handle = text.strip()
        user_states[uid]['target_username'] = target_handle
        platform = user_states[uid].get('platform', 'other')
        
        parsed_name = f"{platform.upper()} Account"
        parsed_bio = "Checking links..."
        
        if platform == 'telegram':
            clean_handle = target_handle.replace('https://t.me/', '').replace('http://t.me/', '').replace('@', '').strip()
            try:
                chat_info = bot.get_chat(f"@{clean_handle}")
                parsed_name = chat_info.title if chat_info.title else f"{chat_info.first_name or ''}"
                parsed_bio = chat_info.description if chat_info.description else "No bio found"
                if chat_info.photo:
                    file_info = bot.get_file(chat_info.photo.big_file_id)
                    downloaded_file = bot.download_file(file_info.file_path)
                    bot.send_photo(uid, downloaded_file, caption="📸 Telegram Profile Image!")
            except Exception:
                parsed_name = f"Telegram (@{clean_handle})"
                parsed_bio = "Channel/Group saved manually."
        else:
            # 🌟 ማሻሻያ፦ የሌሎች ሶሻል ሚዲያዎችን መረጃ ገጽ ሰብሮ መጎተት
            scraped_title, scraped_desc, scraped_img = fetch_social_profile(platform, target_handle)
            if scraped_title:
                parsed_name = scraped_title
                parsed_bio = scraped_desc
                if scraped_img:
                    try:
                        bot.send_photo(uid, scraped_img, caption=f"📸 {platform.upper()} Live Preview!")
                    except Exception: pass
            else:
                parsed_name = f"{platform.upper()} Client Account"
                parsed_bio = "Link saved securely. Manual review pending." if lang=='en' else "ሊንኩ በደህንነት ተመዝግቧል:: ትዕዛዙ ሲሰራ በእጅ ይረጋገጣል::"

        info_panel = (
            f"⚙️ ACCOUNT CONFIRMATION DATA:\n\n👤 Name/Title: {parsed_name}\n🔗 Link: {target_handle}\n📝 Bio: {parsed_bio}\n\n🤔 Correct?"
        ) if lang == 'en' else (
            f"⚙️ የአካውንት ማረጋገጫ መረጃ ፓነል:\n\n👤 ስም/ርዕስ: {parsed_name}\n🔗 ሊንክ: {target_handle}\n📝 ባዮ: {parsed_bio}\n\n🤔 ይህ መረጃ ትክክለኛ አካውንትዎ መሆኑን ያረጋግጣሉ?"
        )
        
        kb = types.InlineKeyboardMarkup()
        kb.row(types.InlineKeyboardButton("Yes" if lang=='en' else "አዎ (Yes)", callback_data="verifyacc_yes"),
               types.InlineKeyboardButton("No" if lang=='en' else "አይደለም (No)", callback_data="verifyacc_no"))
        bot.send_message(uid, info_panel, reply_markup=kb)
        return

    if state == 'waiting_tg_username':
        user_states[uid]['tg_username'] = text
        srv = user_states[uid].get('service', 'N/A').upper()
        tg_user = user_states[uid]['tg_username']
        tgt = user_states[uid].get('target_username', 'N/A')
        plat = user_states[uid].get('platform', 'N/A')

        admin_report = (
            f"📥 🔥 NEW INBOUND ORDER [{srv}] 🔥\n\n"
            f"👤 Client User ID: {uid}\n"
            f"🆔 Telegram Contact: {tg_user}\n"
            f"📱 Platform: {plat.upper()}\n"
            f"🔗 Target Asset: {tgt}\n"
        )
        bot.send_message(ADMIN_ID, admin_report)
        user_states[uid] = {'lang': lang}
        bot.send_message(uid, TEXTS[lang]['success_order'], reply_markup=get_main_keyboard(lang))
        return

if __name__ == '__main__':
    print("Starting Flask Web Server on Free Tier...")
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    print("AK DEVELOP ORDER CENTER BOT running safely...")
    bot.infinity_polling()
