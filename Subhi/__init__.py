from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, MONGO_URI, LOG_GROUP_ID, BIO, BLACKLIST_CHAT, HELP_PIC, ALIVE_PIC, HANDLER
import time

startTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

def get_uptime(x):
    z = get_readable_time(int(x-startTime))
    return z

grt = get_readable_time

if not API_ID:
   print("ERROR: API_ID not found ⚠️")   

if not API_HASH:
   print("ERROR: API_HASH not found ⚠️")

if not BOT_TOKEN:
   print("ERROR: BOT_TOKEN not found ⚠️")

if not STRING_SESSION:
   print("ERROR: STRING_SESSION not found ⚠️")

if not MONGO_URI:
   print("ERROR: MONGO_URI not found ⚠️")

if not LOG_GROUP_ID:
   print("ERROR: LOG_GROUP_ID not found ⚠️")
  
API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN
STRING_SESSION = STRING_SESSION
LOG_GROUP_ID = LOG_GROUP_ID
MONGO_URI = MONGO_URI
BIO = BIO
BLACKLIST_CHAT = BLACKLIST_CHAT
ALIVE_PIC = ALIVE_PIC
HELP_PIC = HELP_PIC
HANDLER = HANDLER
