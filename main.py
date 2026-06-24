import telebot
from telebot import types

TOKEN = "8508598804:AAHcIz1oD-OntAmn68qtfk1mURDpkvTf4aM"
ADMIN_ID = 8926052749
bot = telebot.TeleBot(TOKEN)

# የተጠቃሚዎችን የሂደት ሁኔታ (State) መቆጣጠሪያ መዝገብ
user_states = {}

# ለሁሉም አገልግሎቶች የሚሆኑ የጽሁፍ ማከማቻዎች (ከ5-6 መስመር በላይ የተረዘሙ)
TEXTS = {
    'welcome': (
        "👋 Welcome to AK DEVELOP ORDER CENTER!\n"
        "🇪🇹 እንኳን ወደ AK DEVELOP ማዘዣ ማእከል በሰላም መጡ!\n\n"
        "✨ We offer premium Website, Bot, Mobile Application development, and digital marketing promotion services.\n"
        "✨ ጥራት ያላቸው የዌብሳይት፣ የቴሌግራም ቦት፣ የሞባይል መተግበሪያዎች እና የሶሻል ሚዲያ ማስተዋወቅ ስራዎችን እንሰራለን::\n\n"
        "🌐 Please select your preferred language below to proceed with your order.\n"
        "🌐 እባክዎ ትዕዛዝዎን ለመቀጠል ከታች የሚፈልጉትን ቋንቋ ይምረጡ::"
    ),
    'am': {
        'main_menu': (
            "🏢 እንኳን ወደ ዋናው የማውጫ ገጽ በሰላም መጡ!\n"
            "እዚህ AK DEVELOP ORDER CENTER ውስጥ የእርስዎን የቢዝነስ ህልም እውን የሚያደርጉ ዘመናዊ መፍትሄዎችን እናቀርባለን::\n"
            "ከታች ካሉት አማራጮች ውስጥ የሚፈልጉትን የአገልግሎት አይነት በመምረጥ ዝርዝር መጠይቆችን መሙላት ይችላሉ::\n"
            "ቡድናችን ጥራቱን የጠበቀ ስራ በታማኝነት እና በፍጥነት አጠናቆ ለእናንተ ለማስረከብ ሁልጊዜ ዝግጁ ነው::\n"
            "እባክዎ አንዱን የአገልግሎት ቁልፍ በመጫን ፍላጎትዎን ያሳውቁን::"
        ),
        'about_us': (
            "📖 ስለ እኛ (About AK DEVELOP)\n\n"
            "📍 አንደኛ አንቀጽ፡ AK DEVELOP በዲጂታል አለም ውስጥ የላቀ ስም እና እውቅና ያተረፈ ድርጅት ሲሆን፣ ዋና አላማችንም የተለያዩ ተቋማት እና ግለሰቦች የራሳቸውን የቴክኖሎጂ አሻራ እንዲያሳርፉ መርዳት ነው:: ለአመታት ባካበትነው ልምድ በርካታ ስኬታማ ፕሮጀክቶችን አጠናቀናል::\n\n"
            "📍 ሁለተኛ አንቀጽ፡ በዌብሳይት ዲዛይን ዘርፍ እጅግ ዘመናዊ፣ ፈጣን እና ለተጠቃሚ ምቹ የሆኑ ገጾችን እንሰራለን:: እስካሁን ከሰራናቸው ታላላቅ የዌብሳይት ስራዎቻችን መካከል እንደ tattly.com ፣ beardbrand.com እና kulala.co.uk ያሉ አለምአቀፍ ደረጃቸውን የጠበቁ ምርጥ ገጾች ይገኙበታል::\n\n"
            "📍 ሶስተኛ አንቀጽ፡ በቴሌግራም ቦት ልማት ረገድ ደንበኞቻችን ስራቸውን እንዲያቀልሉ የሚያደርጉ በርካታ አውቶሜትድ ሲስተሞችን ገንብተናል:: ለምሳሌ ያህል @aanimestikers_bot እና @preton_drop_bot የተባሉ በሚሊዮን የሚቆጠሩ ተጠቃሚዎች ያሏቸውን ቦቶች በተሳካ ሁኔታ ሰርተናል::\n\n"
            "📍 አራተኛ አንቀጽ፡ በተጨማሪም መዝናኛዎችን እና የፎቶ ማስተካከያ አፕሊኬሽኖችን በማበልጸግ ረገድ ሰፊ ልምድ አለን:: ለዚህም ማረጋገጫ የሚሆኑት @AddisBingoBot እና የሰዎችን ፎቶ ጥራት የሚጨምረው @restoration_photo_bot ተጠቃሽ ስራዎቻችን ናቸው::\n\n"
            "📍 አምስተኛ አንቀጽ፡ የእኛ ልዩ መለያ ለደንበኞቻችን የምንሰጠው ዘላቂ ድጋፍ እና አስተማማኝነት ነው:: በስራችን ላይ መሳተፍ ወይም መረጃዎችን በቅርብ መከታተል ከፈለጉ @AK_DEVELOP3HUB የተባለውን ይፋዊ ቻናላችንን መቀላቀል ይችላሉ:: ሁሌም ከምርጥ ጥራት ጋር እንቆማለን!"
        ),
        'feedback_prompt': (
            "✍️ የእርስዎ አስተያየት ለእኛ ትልቅ ዋጋ አለው!\n"
            "እባክዎ ለድርጅታችን AK DEVELOP ያለዎትን ማንኛውንም አይነት ገንቢ አስተያየት፣ ጥቆማ ወይም ቅሬታ በዚህ መስመር ይጻፉልን::\n"
            "የሚጽፉት እያንዳንዱ መልዕክት የአገልግሎታችንን ጥራት ይበልጥ እንድናሻሽል ትልቅ እገዛ ያደርግልናል::\n"
            "መልዕክትዎን እንደጨረሱ በቀጥታ በጽሁፍ ይላኩልን::"
        ),
        'other_prompt': (
            "📝 እባክዎ የሚፈልጉትን ልዩ የፕሮጀክት አይነት በዝርዝር ይጻፉልን!\n"
            "ከዝርዝሩ ውስጥ የእርስዎን ፍላጎት የሚያሟላ አማራጭ ካላገኙ፣ እዚህ ቦታ ላይ የሚሰሩትን ስራ ዝርዝር መግለጫ መጻፍ ይችላሉ::\n"
            "የፕሮጀክቱን አላማ፣ ምን ምን ነገሮችን ማካተት እንዳለበት እና አጠቃላይ ይዘቱን በሰፊው አስረድተው ይላኩልን::\n"
            "ጽፈው ሲጨርሱ መልዕክቱን ይላኩ፤ ሲስተሙ በቀጥታ ይቀበለዋል::"
        ),
        'success_order': (
            "🎉 እንኳን ደስ አለዎት! የእርስዎ ትዕዛዝ በተሳካ ሁኔታ ተመዝግቧል!\n"
            "ያስገቡት ዝርዝር መረጃ እና ፍላጎት በAK DEVELOP ORDER CENTER አስተዳዳሪዎች ዘንድ ደርሷል::\n"
            "በቀጣይ ሰዓታት ውስጥ የቴክኒክ ባለሙያዎቻችን ያስገቡትን የቴሌግራም አድራሻ በመጠቀም በቀጥታ ያነጋግሩዎታል::\n"
            "ስለ መረጡን እና በላቀ እምነትዎ እጅግ በጣም እናመሰግናለን:: አሁን ወደ ዋናው ገጽ ይመለሳሉ::"
        ),
        'username_prompt': "📍 እባክዎ የእርስዎን ትክክለኛ የቴሌግራም የተጠቃሚ ስም (Telegram Username) ያለምንም ስህተት '@' በመጨመር ይጻፉልን::",
        'add_more_prompt': "➕ ከተጠቀሱት ጥያቄዎች በተጨማሪ በፕሮጀክቱ ላይ እንዲካተት ወይም እንዲጨመር የሚፈልጉት ነገር (ለምሳሌ የፕሮጀክቱ ስም ወዘተ) ካለ እባክዎ እዚህ ያብራሩልን::",
        'confirm_desc': "\n\n🤔 ይህ የመረጡት የአገልግሎት አይነት የእርስዎን ፍላጎት ሙሉ በሙሉ ያሟላል? እባክዎ 'አዎ' ወይም 'አይደለም' በማለት ያረጋግጡ::",
    },
    'en': {
        'main_menu': (
            "🏢 Welcome to the Main Menu of AK DEVELOP ORDER CENTER!\n"
            "Here, we transform your digital dreams into powerful, modern technology solutions tailored for your business.\n"
            "Please select any of our core services from the modern inline buttons displayed below to start structuring your request.\n"
            "Our dedicated team is highly committed to delivering premium quality, absolute security, and ultra-fast deployment.\n"
            "Click on any service button below to seamlessly trigger the comprehensive workflow system."
        ),
        'about_us': (
            "📖 About Us (AK DEVELOP Profile)\n\n"
            "📍 Paragraph 1: AK DEVELOP is a premier, forward-thinking technology agency specialized in building high-end digital solutions for modern businesses. We empower brands around the globe by constructing reliable digital products that drive maximum user growth.\n\n"
            "📍 Paragraph 2: In web development, we construct fully responsive, pixel-perfect, and conversions-optimized websites. Our highly notable real-world structural portfolio includes industry masterpieces such as tattly.com, beardbrand.com, and kulala.co.uk.\n\n"
            "📍 Paragraph 3: Regarding automated software systems, we specialize in high-traffic Telegram bots with millions of global sub-users. We engineered robust automation architectures like @aanimestikers_bot and @preton_drop_bot with absolute uptime.\n\n"
            "📍 Paragraph 4: Furthermore, our expert deployment framework extends to immersive applications and AI photo enhancers. Our proven track record features interactive applications such as @AddisBingoBot and the advanced quality restorer @restoration_photo_bot.\n\n"
            "📍 Paragraph 5: What sets AK DEVELOP apart is our ultimate emphasis on continuous support, agile scaling, and deep technical engineering. To follow our recent product launches, join our official hub at @AK_DEVELOP3HUB. Your growth is our core mission!"
        ),
        'feedback_prompt': (
            "✍️ Your valuable feedback drives our technical innovation!\n"
            "Please take a brief moment to write your honest experience, recommendations, or complaints regarding our services here.\n"
            "Every single constructive submission is processed directly by our executive management to elevate our operational delivery.\n"
            "Type your feedback response completely in text format and click send now."
        ),
        'other_prompt': (
            "📝 Please describe your custom project structural requirements in full detail!\n"
            "If your specific unique product idea is not listed among our standard options, use this prompt to write down its exact functionality.\n"
            "Explain the ultimate goal, target user base, design structure, and every expected automated feature.\n"
            "Send your detailed description text, and our central processing module will log it."
        ),
        'success_order': (
            "🎉 Congratulations! Your formal order has been compiled and accepted successfully!\n"
            "The multi-layered project parameters have been accurately transmitted into the AK DEVELOP internal administrative system.\n"
            "Our senior developer team will verify your specifications and communicate with you directly using your provided username.\n"
            "Thank you for choosing AK DEVELOP as your core technology collaborator. Returning to the main dashboard menu."
        ),
        'username_prompt': "📍 Please type your authentic Telegram Username accurately, ensuring it includes the standard '@' prefix symbol.",
        'add_more_prompt': "➕ In addition to the structured questions answered, is there any custom element or specific project name you want to add? Please write it here.",
        'confirm_desc': "\n\n🤔 Does this specific detailed description align perfectly with your project vision? Please confirm with 'Yes' or 'No'.",
    }
}

# የአገልግሎቶች ዝርዝር መግለጫዎች እና የተከታታይ ጥያቄዎች ማውጫ
SERVICES_DATA = {
    'website': {
        'types': ['E-commerce Website', 'Portfolio Website', 'Business Website', 'Landing Page'],
        'am_desc': {
            'E-commerce Website': "🛍️ የኢኮሜርስ ዌብሳይት፡ ምርቶችዎን በአለምአቀፍ ደረጃ ለገበያ የሚያቀርቡበት፣ ሙሉ የሽያጭ ሲስተም፣ የክፍያ አማራጮች እና የዕቃ መቆጣጠሪያ ማውጫ ያለው እጅግ ዘመናዊ የዲጂታል ሱቅ መድረክ ነው::",
            'Portfolio Website': "💼 የፖርትፎሊዮ ዌብሳይት፡ የእርስዎን ሙያ፣ ክህሎት፣ ስራዎች እና ግላዊ ማረጋገጫዎች ለቀጣሪዎች ወይም ለደንበኞች በሚማርክ ሁኔታ የሚያስተዋውቁበት ፕሮፌሽናል ገጽ ነው::",
            'Business Website': "🏢 የቢዝነስ ዌብሳይት፡ ስለ ድርጅትዎ አገልግሎቶች፣ አድራሻ፣ አላማ እና ተልዕኮ ሰፊ መረጃ በመስጠት የድርጅትዎን አመኔታ እና የደንበኞችን ቁጥር በከፍተኛ ደረጃ የሚያሳድግ ሲስተም ነው::",
            'Landing Page': "🎯 ላንዲንግ ፔጅ፡ የተወሰኑ ምርቶችን ወይም አዳዲስ ክስተቶችን በአንድ ገጽ ላይ ብቻ በማሳየት ደንበኞች ፈጣን ውሳኔ እንዲሰጡ የሚያደርግ ውጤታማ የግብይት ገጽ ነው::"
        },
        'en_desc': {
            'E-commerce Website': "🛍️ E-commerce Website: A premium modern digital storefront engineered with automated shopping carts, dynamic secure payment gateways, and real-time inventory management tracking tools.",
            'Portfolio Website': "💼 Portfolio Website: A visually stunning professional digital resume designed to display your unique skillsets, past projects, and milestones to worldwide clients.",
            'Business Website': "🏢 Business Website: An corporate information gateway constructed to present your brand services, operational location, core values, and exponentially boost brand authority.",
            'Landing Page': "🎯 Landing Page: A highly optimized conversion-focused single page structured perfectly to grab immediate client traffic and drive specific user actions."
        },
        'questions_am': [
            "1. የዌብሳይቱ ዋና አላማ ወይም የሚሸጠው ምርት/አገልግሎት ምንድን ነው?",
            "2. በዌብሳይቱ ላይ ምን አይነት የከፈያ መንገዶች (ለምሳሌ፡ Telebirr, CBE) እንዲካተቱ ይፈልጋሉ?",
            "3. ለዌብሳይቱ የተመረጠ የተለየ የከለር ወይም የዲዛይን ምርጫ አለዎት?",
            "4. ዌብሳይቱ በስንት ቋንቋዎች እንዲሰራ ይፈልጋሉ? (ለምሳሌ፡ አማርኛ እና እንግሊዝኛ)",
            "5. ፕሮጀክቱ በስንት ቀናት ውስጥ ተጠናቆ እንዲረከብ ይፈልጋሉ?"
        ],
        'questions_en': [
            "1. What is the primary objective or core product/service of this website?",
            "2. What specific payment systems (e.g., Telebirr, CBE) should be integrated?",
            "3. Do you have a preferred color scheme or distinct visual brand identity?",
            "4. How many languages should the website actively support? (e.g., English & Amharic)",
            "5. What is your expected timeframe or deadline for complete project delivery?"
        ]
    },
    'bot': {
        'types': ['Store/Shop Bot', 'Entertainment Bot', 'Utility/Tool Bot', 'Crypto/Airdrop Bot'],
        'am_desc': {
            'Store/Shop Bot': "🛒 የሱቅ መቆጣጠሪያ ቦት፡ ደንበኞች በቴሌግራም ሳይወጡ ምርቶችን መርጠው እንዲያዙ፣ አውቶሜትድ ክፍያ እንዲፈጽሙ እና ትዕዛዝ እንዲያስተላልፉ የሚያደርግ የንግድ ረዳት ነው::",
            'Entertainment Bot': "🎮 የመዝናኛ ቦት፡ የተለያዩ ጨዋታዎችን፣ ጥያቄና መልሶችን፣ ሙዚቃዎችን እና አዝናኝ ሚዲያዎችን ለተጠቃሚዎች በማቅረብ ሰፊ ተከታታይ የሚያፈራ የቦት አይነት ነው::",
            'Utility/Tool Bot': "🛠️ የዩቲሊቲ ቦት፡ የፎቶ ጥራት መጨመርን፣ ፋይል ኮንቨርት ማድረግን፣ ፒዲኤፍ ማስተካከልን እና ሌሎች በርካታ ጠቃሚ ስራዎችን በራስ-ሰር የሚሰራ መሳሪያ ነው::",
            'Crypto/Airdrop Bot': "🪙 የክሪፕቶ/ኤርድሮፕ ቦት፡ ተጠቃሚዎች የተወሰኑ ተግባራትን (ታስኮችን) በመስራት ነጥብ ወይም ክሪፕቶ እንዲሰበስቡ የሚያደርግ የሰርኩሌሽን ሲስተም ነው::"
        },
        'en_desc': {
            'Store/Shop Bot': "🛒 Store/Shop Bot: An automated retail bot structured inside Telegram to catalog physical products, manage instant checkouts, and process client billing info seamlessly.",
            'Entertainment Bot': "🎮 Entertainment Bot: An interactive media bot designed with integrated text games, custom trivia networks, and audio-visual streaming capabilities for heavy user retention.",
            'Utility/Tool Bot': "🛠️ Utility/Tool Bot: A productivity tool automated to perform operational activities like image compression, complex file format conversion, and multi-format data scraping.",
            'Crypto/Airdrop Bot': "🪙 Crypto/Airdrop Bot: A customized distribution program configured to track social tasks, process verification milestones, and manage internal balance reward points."
        },
        'questions_am': [
            "1. ቦቱ በቀን ምን ያህል ተጠቃሚዎችን ያስተናግዳል ተብሎ ይጠበቃል?",
            "2. ቦቱ ላይ እንዲካተቱ የሚፈልጓቸው ዋና ዋና ሜኑዎች እና በተኖች ምን ምን ናቸው?",
            "3. ቦቱ መረጃዎችን የሚያስቀምጥበት የተለየ የዳታቤዝ (Database) ፍላጎት አለዎት?",
            "4. ለቦቱ ተጠቃሚዎች አውቶሜትድ መልዕክት መላኪያ (Broadcasting) ሲስተም ያስፈልገዋል?",
            "5. ቦቱ ከሌሎች የሶሻል ሚዲያ ቻናሎች ጋር እንዲገናኝ ይፈልጋሉ?"
        ],
        'questions_en': [
            "1. What is the projected daily active user volume that this bot will securely handle?",
            "2. What are the core layout command buttons and custom sub-menus to feature?",
            "3. Do you have any specific preferred secure cloud database management infrastructure?",
            "4. Is an advanced automated message broadcasting panel required for administration?",
            "5. Should this specific bot cross-interact with external social media APIs or channels?"
        ]
    },
    'app': {
        'types': ['Android App', 'iOS App', 'Cross-Platform App', 'Web App'],
        'am_desc': {
            'Android App': "🤖 የአንድሮይድ አፕ፡ በፕሌይ ስቶር ላይ የሚጫን፣ ለአንድሮይድ ስልኮች ብቻ ተለይቶ በከፍተኛ ፍጥነት እና ጥራት የሚሰራ መተግበሪያ ነው::",
            'iOS App': "🍏 የiOS አፕ፡ በአፕል ስቶር ላይ የሚጋራ፣ ለአይፎን ስልኮች ልዩ ጥበቃ እና ውበት ተደርጎለት የሚበለጽግ የላቀ መተግበሪያ ነው::",
            'Cross-Platform App': "📱 ክሮስ-ፕላትፎርም አፕ፡ በአንድ ኮድ ተጽፎ በአንድ ጊዜ በሁለቱም (በአንድሮይድም በiOSም) ስልኮች ላይ ያለምንም እንከን መስራት የሚችል ዘመናዊ አፕ ነው::",
            'Web App': "🌐 ዌብ አፕ፡ በብሮውዘር ላይ የሚከፈት ግን ልክ እንደ ስልክ አፕሊኬሽን በጣም ፈጣን የሆኑ ውስብስብ ስራዎችን የሚሰራ የሲስተም መተግበሪያ ነው::"
        },
        'en_desc': {
            'Android App': "🤖 Android App: A high-performance native application engineered using industry-standard SDKs, completely optimized for Google Play Store deployment.",
            'iOS App': "🍏 iOS App: An elite secure application architecture developed natively to adhere to strict Apple App Store distribution guidelines and fluid design languages.",
            'Cross-Platform App': "📱 Cross-Platform App: A single-codebase solution written to function flawlessly on both Android and iOS devices simultaneously, reducing financial setup overhead.",
            'Web App': "🌐 Web App: A highly interactive browser-based software application offering fluid desktop-like capabilities without requiring app store installation."
        },
        'questions_am': [
            "1. የመተግበሪያው (አፑ) ዋና የቢዝነስ ሞዴል ወይም አጠቃቀም ምንድን ነው?",
            "2. አፑ ተጠቃሚዎች አካውንት መክፈቻ (Login/Sign Up) ሲስተም እንዲኖረው ይፈልጋሉ?",
            "3. አፑ ከመስመር ውጭ (Offline) መስራት የሚችሉባቸው ክፍሎች እንዲኖሩት ይፈልጋሉ?",
            "4. ለአፑ የኖቲፊኬሽን (Push Notification) መላኪያ ሲስተም እንዲገጠምለት ይፈልጋሉ?",
            "5. አፑን ወደፊት ወደ ማርኬት ለማውጣት ያሰቡት በየትኛው ፕላትፎርም ላይ ነው?"
        ],
        'questions_en': [
            "1. What is the fundamental utility model or active business loop of the mobile application?",
            "2. Does the system require secure custom user profile authentication (Login/Sign Up)?",
            "3. Should certain framework models function offline without internet access?",
            "4. Do you need a push notification delivery system implemented to alert users?",
            "5. Which app storefront market is your immediate target for official launch?"
        ]
    }
}


# ረዳት ተግባር - የተጠቃሚውን ቋንቋ ለማረጋገጥ
def check_lang(message):
    uid = message.chat.id
    if uid not in user_states or 'lang' not in user_states[uid]:
        bot.send_message(uid, TEXTS['welcome'], reply_markup=get_lang_keyboard())
        return False
    return True

# ረዳት ተግባር - የቋንቋ መምረጫ ቁልፍ
def get_lang_keyboard():
    kb = types.InlineKeyboardMarkup()
    kb.row(types.InlineKeyboardButton("አማርኛ 🇪🇹", callback_data="setlang_am"),
           types.InlineKeyboardButton("English 🇬🇧", callback_data="setlang_en"))
    return kb

# ረዳት ተግባር - ዋና ማውጫ ቁልፍ
def get_main_keyboard(lang):
    kb = types.InlineKeyboardMarkup(row_width=1)
    if lang == 'am':
        kb.add(
            types.InlineKeyboardButton("🌐 ዌብሳይት ለመስራት (Website Creation)", callback_data="menu_website"),
            types.InlineKeyboardButton("🤖 ቦት ለመስራት (Bot Creation)", callback_data="menu_bot"),
            types.InlineKeyboardButton("📱 አፕ ለመስራት (App Creation)", callback_data="menu_app"),
            types.InlineKeyboardButton("📈 ማስተዋወቅና መሸጥ (Promotion & Resell)", callback_data="menu_promo"),
            types.InlineKeyboardButton("📊 ሶሻል ሚዲያ ማናጅመንት (Social Media Management)", callback_data="menu_mgmt"),
            types.InlineKeyboardButton("ℹ️ ስለ እኛ (About Us)", callback_data="menu_about"),
            types.InlineKeyboardButton("✍️ አስተያየት ለመስጠት (Feedback)", callback_data="menu_feedback")
        )
    else:
        kb.add(
            types.InlineKeyboardButton("🌐 Website Creation", callback_data="menu_website"),
            types.InlineKeyboardButton("🤖 Bot Creation", callback_data="menu_bot"),
            types.InlineKeyboardButton("📱 App Creation", callback_data="menu_app"),
            types.InlineKeyboardButton("📈 Promotion and Resell", callback_data="menu_promo"),
            types.InlineKeyboardButton("📊 Social Media Management", callback_data="menu_mgmt"),
            types.InlineKeyboardButton("ℹ️ About Us", callback_data="menu_about"),
            types.InlineKeyboardButton("✍️ Feedback", callback_data="menu_feedback")
        )
    return kb


# START ትዕዛዝ መስመር
@bot.message_handler(commands=['start'])
def start_cmd(message):
    uid = message.chat.id
    user_states[uid] = {}  # ስቴቱን ማጽዳት
    bot.send_message(uid, TEXTS['welcome'], reply_markup=get_lang_keyboard())


# የ CALLBACK DATAዎችን መቆጣጠሪያ
@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    uid = call.message.chat.id
    data = call.data

    # ቋንቋ መምረጥ
    if data.startswith("setlang_"):
        lang = data.split("_")[1]
        user_states[uid] = {'lang': lang}
        bot.answer_callback_query(call.id)
        bot.send_message(uid, TEXTS[lang]['main_menu'], reply_markup=get_main_keyboard(lang))
        return

    # ቋንቋ መመረጡን ማረጋገጥ
    if uid not in user_states or 'lang' not in user_states[uid]:
        bot.answer_callback_query(call.id, "Please select language first / እባክዎ መጀመሪያ ቋንቋ ይምረጡ")
        bot.send_message(uid, TEXTS['welcome'], reply_markup=get_lang_keyboard())
        return

    lang = user_states[uid]['lang']

    # ወደ ዋና ማውጫ መመለሻ (Back)
    if data == "back_to_main":
        user_states[uid] = {'lang': lang}  # ስቴቱን ዳግም ማስጀመር
        bot.answer_callback_query(call.id)
        bot.send_message(uid, TEXTS[lang]['main_menu'], reply_markup=get_main_keyboard(lang))
        return

    # ስለ እኛ እና አስተያየት
    if data == "menu_about":
        bot.answer_callback_query(call.id)
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("⬅️ Back" if lang=='en' else "⬅️ ወደ ዋናው ማውጫ", callback_data="back_to_main"))
        bot.send_message(uid, TEXTS[lang]['about_us'], reply_markup=kb, disable_web_page_preview=True)
        return

    if data == "menu_feedback":
        bot.answer_callback_query(call.id)
        user_states[uid]['state'] = 'waiting_feedback'
        bot.send_message(uid, TEXTS[lang]['feedback_prompt'])
        return

    # የዌብሳይት፣ ቦት፣ አፕ ምርጫዎች ማሳያ
    if data in ["menu_website", "menu_bot", "menu_app"]:
        bot.answer_callback_query(call.id)
        service_key = data.split("_")[1]
        user_states[uid]['service'] = service_key
        
        kb = types.InlineKeyboardMarkup(row_width=1)
        for t in SERVICES_DATA[service_key]['types']:
            kb.add(types.InlineKeyboardButton(t, callback_data=f"selecttype_{t}"))
        
        kb.add(types.InlineKeyboardButton("Other" if lang=='en' else "ሌላ (Other)", callback_data="selecttype_Other"))
        kb.add(types.InlineKeyboardButton("⬅️ Back" if lang=='en' else "⬅️ ወደ ዋናው ማውጫ", callback_data="back_to_main"))
        
        title = service_key.upper()
        msg_text = f"🛠️ Select the type of {title} you want to build:\n🛠️ እባክዎ እንዲሰራ የሚፈልጉትን የ{title} አይነት ይምረጡ:" if lang=='en' else f"🛠️ ለመስራት የፈለጉትን የ {title} አይነት ከታች ካሉት አማራጮች ይምረጡ:"
        bot.send_message(uid, msg_text, reply_markup=kb)
        return

    # ንዑስ አገልግሎት መምረጥ (E-commerce, Portfolio ወዘተ)
    if data.startswith("selecttype_"):
        bot.answer_callback_query(call.id)
        chosen_type = data.split("_")[1]
        user_states[uid]['sub_type'] = chosen_type
        service_key = user_states[uid]['service']

        if chosen_type == "Other":
            user_states[uid]['state'] = 'waiting_other_desc'
            bot.send_message(uid, TEXTS[lang]['other_prompt'])
        else:
            # መግለጫውን አውጥቶ ማሳየት
            desc = SERVICES_DATA[service_key]['en_desc'][chosen_type] if lang == 'en' else SERVICES_DATA[service_key]['am_desc'][chosen_type]
            full_msg = desc + TEXTS[lang]['confirm_desc']
            
            kb = types.InlineKeyboardMarkup()
            kb.row(types.InlineKeyboardButton("Yes" if lang=='en' else "አዎ (Yes)", callback_data="confirmtype_yes"),
                   types.InlineKeyboardButton("No" if lang=='en' else "አይደለም (No)", callback_data="confirmtype_no"))
            bot.send_message(uid, full_msg, reply_markup=kb)
        return

    # የተመረጠውን አይነት ማረጋገጫ (Yes / No)
    if data.startswith("confirmtype_"):
        bot.answer_callback_query(call.id)
        status = data.split("_")[1]
        service_key = user_states[uid]['service']
        
        if status == "no":
            # ወደ ንዑስ ማውጫው መመለስ
            kb = types.InlineKeyboardMarkup(row_width=1)
            for t in SERVICES_DATA[service_key]['types']:
                kb.add(types.InlineKeyboardButton(t, callback_data=f"selecttype_{t}"))
            kb.add(types.InlineKeyboardButton("Other" if lang=='en' else "ሌላ (Other)", callback_data="selecttype_Other"))
            kb.add(types.InlineKeyboardButton("⬅️ Back" if lang=='en' else "⬅️ ወደ ዋናው ማውጫ", callback_data="back_to_main"))
            bot.send_message(uid, "🔄 Selection canceled. Please choose again:" if lang=='en' else "🔄 ምርጫው ተሰርዟል:: እባክዎ ድጋሚ ይምረጡ:", reply_markup=kb)
        else:
            # ጥያቄዎችን መጀመር
            user_states[uid]['step'] = 0
            user_states[uid]['answers'] = []
            user_states[uid]['state'] = 'asking_questions'
            ask_next_question(uid)
        return

    # PROMOTION & RESELL
    if data == "menu_promo":
        bot.answer_callback_query(call.id)
        kb = types.InlineKeyboardMarkup()
        if lang == 'am':
            kb.row(types.InlineKeyboardButton("📢 ፕሮሞሽን (Promotion)", callback_data="sub_promo_action"),
                   types.InlineKeyboardButton("🔄 ዳግም መሸጥ (Resell)", callback_data="sub_resell_action"))
            kb.add(types.InlineKeyboardButton("⬅️ ወደ ዋናው ማውጫ", callback_data="back_to_main"))
            msg = "📈 እባክዎ ማካሄድ የፈለጉትን የንግድ አይነት ይምረጡ:\nፕሮሞሽን ወይም የሶሻል ሚዲያ አካውንቶችን/ቁሳቁሶችን መልሶ መሸጥ::"
        else:
            kb.row(types.InlineKeyboardButton("📢 Promotion", callback_data="sub_promo_action"),
                   types.InlineKeyboardButton("🔄 Resell", callback_data="sub_resell_action"))
            kb.add(types.InlineKeyboardButton("⬅️ Back to Main", callback_data="back_to_main"))
            msg = "📈 Please select the operational wing you want to access:\nEither direct promotion channels or asset reselling markets."
        bot.send_message(uid, msg, reply_markup=kb)
        return

    if data == "sub_promo_action":
        bot.answer_callback_query(call.id)
        user_states[uid]['service'] = 'promotion'
        user_states[uid]['step'] = 0
        user_states[uid]['answers'] = []
        user_states[uid]['state'] = 'asking_questions'
        ask_next_question(uid)
        return

    if data == "sub_resell_action":
        bot.answer_callback_query(call.id)
        kb = types.InlineKeyboardMarkup()
        if lang == 'am':
            kb.row(types.InlineKeyboardButton("📦 እቃዎች/ቁሳቁሶች (Material)", callback_data="resell_material"),
                   types.InlineKeyboardButton("🌐 አካውንቶች (Account)", callback_data="resell_account"))
            kb.add(types.InlineKeyboardButton("⬅️ ወደ ኋላ ተመለስ", callback_data="menu_promo"))
            msg = "🔄 በዳግም መሸጥ (Resell) አገልግሎት ውስጥ ምን አይነት እቃ ማቅረብ ይፈልጋሉ?\nእባክዎ ከታች የቁሳቁስ ወይም የሶሻል ሚዲያ አካውንት በተንን ይምረጡ::"
        else:
            kb.row(types.InlineKeyboardButton("📦 Material", callback_data="resell_material"),
                   types.InlineKeyboardButton("🌐 Account", callback_data="resell_account"))
            kb.add(types.InlineKeyboardButton("⬅️ Back", callback_data="menu_promo"))
            msg = "🔄 Inside the Resell environment, what target asset class are you trading?\nPlease select physical materials or digital accounts below."
        bot.send_message(uid, msg, reply_markup=kb)
        return

    if data == "resell_material":
        bot.answer_callback_query(call.id)
        user_states[uid]['service'] = 'resell_material'
        user_states[uid]['step'] = 0
        user_states[uid]['answers'] = []
        user_states[uid]['state'] = 'asking_questions'
        ask_next_question(uid)
        return

    if data == "resell_account":
        bot.answer_callback_query(call.id)
        user_states[uid]['service'] = 'resell_account'
        show_social_platforms(uid, lang)
        return

    # SOCIAL MEDIA MANAGEMENT
    if data == "menu_mgmt":
        bot.answer_callback_query(call.id)
        user_states[uid]['service'] = 'management'
        show_social_platforms(uid, lang)
        return

    # ሶሻል ሚዲያ ፕላትፎርም መረጣ
    if data.startswith("plat_"):
        bot.answer_callback_query(call.id)
        platform = data.split("_")[1]
        user_states[uid]['platform'] = platform

        if platform == "other":
            user_states[uid]['state'] = 'waiting_custom_platform'
            msg = "📱 Please specify your custom social media platform by typing command format (e.g. /whatsapp, /imo, /linkedin):" if lang=='en' else "📱 እባክዎ የሚጠቀሙትን የሶሻል ሚዲያ አይነት በትዕዛዝ መልክ ይጻፉልን (ምሳሌ፡ /whatsapp, /imo, /linkedin):"
            bot.send_message(uid, msg)
        else:
            ask_account_category(uid, lang)
        return

    # የአካውንት አይነት (Group, Channel, Personal)
    if data.startswith("acctype_"):
        bot.answer_callback_query(call.id)
        acc_type = data.split("_")[1]
        user_states[uid]['account_type'] = acc_type
        user_states[uid]['state'] = 'waiting_username_lookup'
        
        msg = f"🔍 Please enter the public target Username/Link of your {acc_type} asset now:" if lang=='en' else f"🔍 እባክዎ የሚሸጡትን የ{acc_type} ትክክለኛ ሊንክ ወይም የተጠቃሚ ስም (Username) ያስገቡ:"
        bot.send_message(uid, msg)
        return

    # የአካውንት ፍተሻ ማረጋገጫ (Yes / No)
    if data.startswith("verifyacc_"):
        bot.answer_callback_query(call.id)
        status = data.split("_")[1]
        if status == "no":
            show_social_platforms(uid, lang)
        else:
            # ጥያቄዎችን መጀመር
            user_states[uid]['step'] = 0
            user_states[uid]['answers'] = []
            user_states[uid]['state'] = 'asking_questions'
            ask_next_question(uid)
        return


# ሶሻል ሚዲያ ፕላትፎርሞችን ማሳያ ቁልፍ
def show_social_platforms(uid, lang):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("Telegram ✈️", callback_data="plat_telegram"),
        types.InlineKeyboardButton("TikTok 🎵", callback_data="plat_tiktok"),
        types.InlineKeyboardButton("Instagram 📸", callback_data="plat_instagram"),
        types.InlineKeyboardButton("YouTube 📺", callback_data="plat_youtube"),
        types.InlineKeyboardButton("Other 🌐", callback_data="plat_other")
    )
    kb.add(types.InlineKeyboardButton("⬅️ Back" if lang=='en' else "⬅️ ወደ ኋላ ተመለስ", callback_data="back_to_main"))
    msg = "📱 Select the primary Social Media platform engine involved in this operation:" if lang=='en' else "📱 እባክዎ የሚፈልጉትን የሶሻል ሚዲያ ፕላትፎርም አይነት ከታች ካሉት አማራጮች ውስጥ ይምረጡ:"
    bot.send_message(uid, msg, reply_markup=kb)

# የአካውንት አይነት መምረጫ (Group, Channel, Personal Account)
def ask_account_category(uid, lang):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("Group 👥", callback_data="acctype_Group"),
        types.InlineKeyboardButton("Channel 📢", callback_data="acctype_Channel"),
        types.InlineKeyboardButton("Personal Account 👤", callback_data="acctype_Personal")
    )
    kb.add(types.InlineKeyboardButton("⬅️ Back" if lang=='en' else "⬅️ ወደ ኋላ ተመለስ", callback_data="back_to_main"))
    msg = "📂 Select the specific structure category of the target digital asset:" if lang=='en' else "📂 እባክዎ የሚሸጠውን ዲጂታል አካውንት አወቃቀር ወይም አይነት ይምረጡ:"
    bot.send_message(uid, msg, reply_markup=kb)


# ተከታታይ ጥያቄዎችን የመጠየቂያ ሞጁል
def ask_next_question(uid):
    lang = user_states[uid]['lang']
    service = user_states[uid]['service']
    step = user_states[uid]['step']

    # ለእያንዳንዱ አገልግሎት 5 የተለያዩ ጥያቄዎች ዝርዝር
    questions = []
    if service in ['website', 'bot', 'app']:
        questions = SERVICES_DATA[service]['questions_en'] if lang == 'en' else SERVICES_DATA[service]['questions_am']
    elif service == 'promotion':
        questions = [
            "1. What exactly is the product, event, or channel entity you want to promote?" if lang=='en' else "1. ለማስተዋወቅ (Promote) የፈለጉት እቃ፣ ቻናል ወይስ የንግድ ድርጅት ነው?",
            "2. Which targeting mechanism or strategic methodology do you prefer us to utilize?" if lang=='en' else "2. ማስታወቂያው በምን አይነት መንገድ (በተንቀሳቃሽ ምስል፣ በጽሁፍ ወዘተ) እንዲሰራ ይፈልጋሉ?",
            "3. What is the precise financial budget scale allocated for this campaign run?" if lang=='en' else "3. ለዚህ የማስተዋወቅ ስራ የመደቡት አጠቃላይ የበጀት መጠን ምን ያህል ነው?",
            "4. Who represents your ultimate localized target market or niche audience sector?" if lang=='en' else "4. ማስታወቂያው እንዲደርስላቸው የሚፈልጓቸው ዋና የህብረተሰብ ክፍሎች እነማን ናቸው?",
            "5. What is the active runtime duration sequence requested for the promotion schedule?" if lang=='en' else "5. ማስታወቂያው ለስንት ቀናት በቋሚነት እንዲሰራ ወይም እንዲቀጥል ይፈልጋሉ?"
        ]
    elif service == 'resell_material':
        questions = [
            "1. What is the absolute full design name and category classification of the item?" if lang=='en' else "1. ለመሸጥ ያሰቡት እቃ ወይም ቁሳቁስ ትክክለኛ ስም እና አይነት ምንድን ነው?",
            "2. What is the exact physical operational condition or lifetime metric of the asset?" if lang=='en' else "2. የእቃው አሁናዊ ሁኔታ (አዲስ፣ በጥቂቱ ያገለገለ ወዘተ) ምን ይመስላል?",
            "3. What is the structural retail value or minimal base wholesale pricing set?" if lang=='en' else "3. እቃውን ለመሸጥ ያሰቡት መነሻ ወይም የመጨረሻ ዋጋ ስንት ነው?",
            "4. Are there complete delivery channels available or pickup point restrictions present?" if lang=='en' else "4. እቃውን ለገዢው የሚያስረክቡበት የትራንስፖርት ወይም የማረከቢያ መንገድ አለዎት?",
            "5. What are the key premium functional features that add high market appeal?" if lang=='en' else "5. እቃው ካሉት ጠቀሜታዎች መካከል ዋና ዋና የምንላቸውን በዝርዝር ቢገልጹልን?"
        ]
    elif service == 'resell_account':
        questions = [
            "1. What is the current active member base or authentic follower headcount metric?" if lang=='en' else "1. የአካውንቱ አጠቃላይ አባላት (Members/Followers) ብዛት ምን ያህል ነው?",
            "2. What is the organic user interaction level or computational view average rate?" if lang=='en' else "2. የአካውንቱ የእይታ ፍጥነት (Post Views/Engagement) አማካይ ውጤት ምን ይመስላል?",
            "3. What was the core niche subject or focal content topic hosted historically?" if lang=='en' else "3. በአካውንቱ ላይ በብዛት የሚለቀቁት የይዘት አይነቶች (Content Type) ምን ነበሩ?",
            "4. What is the total financial capital pricing targeted for this structural transfer?" if lang=='en' else "4. አካውንቱን ለመሸጥ የወሰኑት የመጨረሻው የዋጋ መጠን ስንት ነው?",
            "5. What is the ultimate foundational reason triggering this system asset sale?" if lang=='en' else "5. ይህንን አካውንት ለመሸጥ የፈለጉበት ዋና ምክንያት ምንድን ነው?"
        ]
    elif service == 'management':
        questions = [
            "1. What is the precise contract runtime duration sequence requested for active setup?" if lang=='en' else "1. የሶሻል ሚዲያ ማናጅመንት ስራው ለምን ያህል ጊዜ (ለምሳሌ፡ ለ1 ወር፣ ለ6 ወር) እንዲቆይ ይፈልጋሉ?",
            "2. How many high-quality graphic posts or media distributions are needed weekly?" if lang=='en' else "2. በሳምንት ውስጥ በአማካይ ስንት የጽሁፍ እና የፎቶ ይዘቶች እንዲፖስቱ ይፈልጋሉ?",
            "3. Is live client support comment response oversight required within standard hours?" if lang=='en' else "3. በኮሜንት እና በውስጥ መስመር ለሚመጡ ደንበኞች ምላሽ የመስጠት ስራ ይካተት?",
            "4. What is your ultimate goal? Growth hacking, community support, or direct sales conversions?" if lang=='en' else "4. ከማናጅመንቱ የሚጠብቁት ዋናው ውጤት (የፎሎወር መጨመር ወይስ ሽያጭ ማሳደግ) ምንድን ነው?",
            "5. What are your clear content guidelines or visual theme limitations to monitor?" if lang=='en' else "5. በይዘት ዝግጅት ወቅት ሰራተኞቻችን እንዲከተሏቸው የሚፈልጓቸው ልዩ ህጎች አሉ?"
        ]

    if step < len(questions):
        bot.send_message(uid, questions[step])
    else:
        # ጥያቄዎቹ ሲያልቁ ተጨማሪ መረጃ መጠየቅ
        user_states[uid]['state'] = 'waiting_additional_info'
        bot.send_message(uid, TEXTS[lang]['add_more_prompt'])


# የጽሁፍ መልዕክቶችን (TEXT INPUTS) የመቆጣጠሪያ ዋና ክፍል
@bot.message_handler(func=lambda m: True, content_types=['text'])
def handle_text_inputs(message):
    uid = message.chat.id
    text = message.text

    if not check_lang(message):
        return

    lang = user_states[uid]['lang']
    state = user_states[uid].get('state', '')

    # የአስተያየት መቀበያ
    if state == 'waiting_feedback':
        bot.send_message(ADMIN_ID, f"✍️ NEW FEEDBACK RECEIVED:\n\nUser ID: {uid}\nContent: {text}")
        user_states[uid] = {'lang': lang}
        bot.send_message(uid, TEXTS[lang]['success_order'], reply_markup=get_main_keyboard(lang))
        return

    # የልዩ (Other) አገልግሎት ፍላጎት መግለጫ መቀበያ
    if state == 'waiting_other_desc':
        user_states[uid]['sub_type'] = f"Custom Request: {text}"
        user_states[uid]['state'] = 'waiting_tg_username'
        bot.send_message(uid, TEXTS[lang]['username_prompt'])
        return

    # ተከታታይ ጥያቄዎችን በየደረጃው መመዝገቢያ
    if state == 'asking_questions':
        user_states[uid]['answers'].append(text)
        user_states[uid]['step'] += 1
        ask_next_question(uid)
        return

    # ከተከታታይ ጥያቄዎች በኋላ ተጨማሪ ሀሳብ መቀበያ
    if state == 'waiting_additional_info':
        user_states[uid]['additional_info'] = text
        user_states[uid]['state'] = 'waiting_tg_username'
        bot.send_message(uid, TEXTS[lang]['username_prompt'])
        return

    # ልዩ የሶሻል ሚዲያ ስም መቀበያ (/whatsapp ወዘተ)
    if state == 'waiting_custom_platform':
        user_states[uid]['platform'] = text
        ask_account_category(uid, lang)
        return

    # የሶሻል ሚዲያ አካውንት መረጃዎችን ፈልጎ ማሳያ (Telegram Lookup Integration)
    if state == 'waiting_username_lookup':
        target_handle = text.strip()
        user_states[uid]['target_username'] = target_handle
        
        # የቴሌግራም መረጃዎችን በራስ-ሰር ለመውሰድ መሞከር
        parsed_name = target_handle
        parsed_bio = "N/A"
        has_photo = False
        
        if user_states[uid].get('platform') == 'telegram' or target_handle.startswith('@') or 't.me/' in target_handle:
            clean_handle = target_handle.replace('https://t.me/', '').replace('http://t.me/', '').replace('@', '')
            try:
                chat_info = bot.get_chat(f"@{clean_handle}")
                parsed_name = chat_info.title if chat_info.title else f"{chat_info.first_name or ''} {chat_info.last_name or ''}"
                parsed_bio = chat_info.description if chat_info.description else (chat_info.bio if chat_info.bio else "No bio found")
                if chat_info.photo:
                    has_photo = True
                    # የፊቱን ፕሮፋይል ፎቶ ለይቶ መላክ
                    file_info = bot.get_file(chat_info.photo.big_file_id)
                    downloaded_file = bot.download_file(file_info.file_path)
                    bot.send_photo(uid, downloaded_file, caption="📸 Account Profile Image Pulled Successfully!" if lang=='en' else "📸 የአካውንቱ መገለጫ ምስል በተሳካ ሁኔታ ተገኝቷል!")
            except Exception:
                pass # ስህተት ካለ ወደ ፎልባክ መረጃው ያልፋል
        
        info_panel = (
            f"⚙️ ACCOUNT CONFIRMATION DATA:\n\n"
            f"👤 Account Name: {parsed_name}\n"
            f"🔗 Target Handle: {target_handle}\n"
            f"📝 Description/Bio: {parsed_bio}\n\n"
            f"🤔 Is this targeted digital account completely correct?"
        ) if lang == 'en' else (
            f"⚙️ የአካውንት ማረጋገጫ መረጃ ፓነል:\n\n"
            f"👤 የአካውንት ስም: {parsed_name}\n"
            f"🔗 የተጠቃሚ ስም: {target_handle}\n"
            f"📝 መገለጫ/ባዮ: {parsed_bio}\n\n"
            f"🤔 ይህ ከላይ የመጣው አካውንት የእርስዎ ትክክለኛ አካውንት ነው?"
        )
        
        kb = types.InlineKeyboardMarkup()
        kb.row(types.InlineKeyboardButton("Yes" if lang=='en' else "አዎ (Yes)", callback_data="verifyacc_yes"),
               types.InlineKeyboardButton("No" if lang=='en' else "አይደለም (No)", callback_data="verifyacc_no"))
        bot.send_message(uid, info_panel, reply_markup=kb)
        return

    # መጨረሻ ላይ የቴሌግራም ዩዘርኔም መቀበያ እና ማጠቃለያውን ወደ አድሚን መላኪያ
    if state == 'waiting_tg_username':
        user_states[uid]['tg_username'] = text
        
        # ማጠቃለያ ሪፖርት ማመንጫ (ለአድሚን በተመረጠው ቋንቋ ብቻ የሚላክ)
        srv = user_states[uid].get('service', 'N/A').upper()
        sub_t = user_states[uid].get('sub_type', 'N/A')
        tg_user = user_states[uid]['tg_username']
        add_info = user_states[uid].get('additional_info', 'None')
        answers_list = user_states[uid].get('answers', [])
        
        formatted_answers = ""
        for idx, ans in enumerate(answers_list):
            formatted_answers += f"  🔹 Q{idx+1}: {ans}\n"

        if lang == 'en':
            admin_report = (
                f"📥 🔥 NEW INBOUND ORDER LOGGED [{srv}] 🔥\n\n"
                f"👤 Client User ID: {uid}\n"
                f"🆔 Provided Telegram Contact: {tg_user}\n"
                f"🛠️ Service Wing: {srv}\n"
                f"📂 Sub-Category Config: {sub_t}\n"
            )
            if user_states[uid].get('platform'):
                admin_report += f"📱 Target Platform: {user_states[uid]['platform']}\n"
            if user_states[uid].get('account_type'):
                admin_report += f"🗂️ Account Structure: {user_states[uid]['account_type']}\n"
            if user_states[uid].get('target_username'):
                admin_report += f"🔗 Asset Link/Handle: {user_states[uid]['target_username']}\n"
            
            admin_report += f"\n📊 COMPREHENSIVE QUESTIONNAIRE RESPONSES:\n{formatted_answers}\n"
            admin_report += f"➕ Additional Specification Notes:\n  {add_info}\n"
        else:
            admin_report = (
                f"📥 🔥 አዲስ የትዕዛዝ መዝገብ ደርሷል [{srv}] 🔥\n\n"
                f"👤 የደንበኛ መለያ ቁጥር: {uid}\n"
                f"🆔 የተቀመጠው የቴሌግራም አድራሻ: {tg_user}\n"
                f"🛠️ ዋና አገልግሎት ክፍል: {srv}\n"
                f"📂 ንዑስ የአገልግሎት አይነት: {sub_t}\n"
            )
            if user_states[uid].get('platform'):
                admin_report += f"📱 የተመረጠው ፕላትፎርም: {user_states[uid]['platform']}\n"
            if user_states[uid].get('account_type'):
                admin_report += f"🗂️ የአካውንት አወቃቀር: {user_states[uid]['account_type']}\n"
            if user_states[uid].get('target_username'):
                admin_report += f"🔗 የአካውንት ሊንክ/ዩዘርኔም: {user_states[uid]['target_username']}\n"
                
            admin_report += f"\n📊 ለቀረቡት መጠይቆች የተሰጡ ምላሾች:\n{formatted_answers}\n"
            admin_report += f"➕ ተጨማሪ የተካተቱ ማብራሪያዎች:\n  {add_info}\n"

        # ማጠቃለያውን ወደ ዋናው ባለቤት መላክ
        bot.send_message(ADMIN_ID, admin_report)
        
        # ለደንበኛው የስኬት መልዕክት ማሳየት እና ወደ ዋና ማውጫ መመለስ
        user_states[uid] = {'lang': lang}
        bot.send_message(uid, TEXTS[lang]['success_order'], reply_markup=get_main_keyboard(lang))
        return


# ቦቱን ማስጀመር (Long Polling Engine)
if __name__ == '__main__':
    print("AK DEVELOP ORDER CENTER BOT running safely...")
    bot.infinity_polling()
