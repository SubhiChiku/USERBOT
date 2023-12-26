from os import getenv

# API_IDS ~ my.telegram.org
API_ID = int(getenv("API_ID", "")) # API_ID get it from my.telegram.org
API_HASH = getenv("API_HASH", "") # API_HASH get ut from my.telegram.org

# SESSIONS ~ python3 session.py
STRING_SESSION = getenv("STRING_SESSION", "") # SESSION get it by run cmd "python3 session.py" in heroku consol or locally 
BOT_TOKEN = getenv("BOT_TOKEN","") # BOT_TOKEN get it from @BotFather Bot on telegram

# DATABASES ~ mongodb.com
MONGO_URI = getenv("MONGO_URI", "") # MONGO_DB_URL get it from mongodb.com

# LOGGGERS ~ telegram private group
LOG_GROUP_ID = getenv("LOG_GROUP_ID", "") # LOG_GROUP_ID get it by creating private group on telegram and fill here that's group id
    
# HANDLER ~ use ( .,-,!,+,-) any symbol like this...
HANDLER = getenv("HANDLER", "") # HANDLER choose your bot command handler
if not HANDLER:
    HANDLER = "!"
    
# IMAGES ~ telegram link of pic
ALIVE_PIC = getenv("ALIVE_PIC", "") # ALIVE_PIC a pic link for alive command in bot
if not ALIVE_PIC:
    ALIVE_PIC = "https://telegra.ph/file/a9efe0eb8f543daae94e5.jpg"
    
HELP_PIC = getenv("HELP_PIC", "") # HELP_PIC a pic link for help commad in bot
if not HELP_PIC:
    HELP_PIC = "https://telegra.ph/file/b963883b6bf71be07ae0e.jpg"
    
# BLACKLISTED CHATS ~ ( not necessary )
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", "") # BLACKLISTED CHATS your telegram group id ( not necessary )
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1002084534383]

# BIO ~ any message in any font for bio ( not necessary )
BIO = getenv("BIO", "〆 яαввιтχ υѕєявσт υѕєя 〆") # BIO for clone and revert commands

# PM_PERMIT ~ pic 
PM_PIC = getenv("PM_PIC","")
if not PM_PIC:
    PM_PIC = "https://telegra.ph/file/42f76db81c5d905e321b1.jpg"
