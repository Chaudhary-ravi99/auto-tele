# Coded By : @qq_iq | Mr28 | Github : @JUSTSAIF

# Reinstall LIB
INPUT = input("[+] Install telebot LIB ? (Y/N) : ")
if (INPUT == "Y" or INPUT == "y"):
    PIP_inp = input("1- pip\n2- pip3 \n[!] use [1 or 2] ?: ")
    pip = "pip" if (PIP_inp == "1") else "pip3"
    print("[+] Installing telebot LIB ...")
    import subprocess
    subprocess.call(f"{pip} uninstall telebot", shell=True)
    subprocess.call(f"{pip} uninstall PyTelegramBotAPI", shell=True)
    subprocess.call(f"{pip} install pyTelegramBotAPI", shell=True)
    subprocess.call(f"{pip} install --upgrade pyTelegramBotAPI", shell=True)
    subprocess.call(f"{pip} install telebot", shell=True)
    print("[+] Done !")

from threading import Thread
import asyncio
from telethon import TelegramClient, events, sync
import telebot

# BOT Configurations 
API_ID = ''
API_HASH = ''
TELEGRAM_BOT = ''

# ==========================================================
ADMINS = [377011400] # ADMINS IDs
client = TelegramClient('session_name',API_ID,API_HASH)
client.start()
bot = telebot.TeleBot(TELEGRAM_BOT)
SLEEP = 30
isRuning = False

# Groups IDs [PRIMARY]
ConstGroups = {
    'group_id' : 'Group Name'
}

# Groups IDs [USER]
Groups = {
    'group_id' : 'Group Name'
}

# Messages
Messages = ["Test By Mr28"]

# OPTIONS
OPTIONS = {
    "START": "start",
    "Show & Manage Groups": "groups",
    "Show & Manage Messages": "msgs",
    "Add New Msg": "addmsg",
    "Reset Groups": "resetgroups",
    "SLEEP SECONDS (Resend All Msgs)": "sleep",
    "START BOT": "startbot",
    "STOP BOT": "stopbot",
}

# Keyboard for adding groups & messages
def MessagesKeyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    for msg in Messages:
        markup.add(telebot.types.InlineKeyboardButton(text=msg,callback_data=F"addMsg_{Messages.index(msg)}"),
        telebot.types.InlineKeyboardButton(text=u"\u274C",callback_data=F"removeMsg_{Messages.index(msg)}"))
    return markup

def GroupsKeyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    for Group in Groups:
        markup.add(telebot.types.InlineKeyboardButton(text=Groups[Group],callback_data=F"addG_{Group}"),
        telebot.types.InlineKeyboardButton(text=u"\u274C",callback_data=F"removeG_{Group}"))
    return markup

def StartKeyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    for OPTION in OPTIONS:
        markup.add(telebot.types.InlineKeyboardButton(text=OPTION, callback_data=F"op_{OPTIONS[OPTION]}"))
    return markup



# START TELE BOT
@bot.message_handler(commands=['start'])
def start_handler(message):
    if message.from_user.id in ADMINS:
        bot.send_message(chat_id=message.chat.id, text="BOT OPTIONS :", reply_markup=StartKeyboard(),parse_mode='HTML')


# START BOT
@bot.message_handler(commands=['stop_bot'])
def add_msg(message):
    if message.from_user.id in ADMINS:
        global isRuning
        isRuning = False
        bot.send_message(chat_id=message.chat.id,text="STOPED .")

# STOP BOT
@bot.message_handler(commands=['start_bot'])
def add_msg(message):
    if message.from_user.id in ADMINS:
        global isRuning
        isRuning = True
        bot.send_message(chat_id=message.chat.id,text="STARTED .")

# SLEEP
@bot.message_handler(commands=['sleep'])
def add_msg(message):
    if message.from_user.id in ADMINS:
        global SLEEP
        SLEEP = int(message.text.split(" ")[1])
        bot.send_message(chat_id=message.chat.id,text=F"CHANGED TO : {SLEEP} Seconds .")

# Add MSG Handler
@bot.message_handler(commands=['add_msg'])
def add_msg_handler(message):
    if message.from_user.id in ADMINS:
        Messages.append(message.text.replace("/add_msg ",""))
        bot.send_message(chat_id=message.chat.id,text="Added .\n"+message.text.replace("/add_msg ",""))


# Show MSGs Handler
@bot.message_handler(commands=['msgs'])
def handle_command_msgs(message):
    if message.from_user.id in ADMINS:
        bot.send_message(chat_id=message.chat.id,text="Messages",reply_markup=MessagesKeyboard(),parse_mode='HTML')


# Show Groups Handler
@bot.message_handler(commands=['groups'])
def handle_command_groups(message):
    if message.from_user.id in ADMINS:
        bot.send_message(chat_id=message.chat.id, text="Groups", reply_markup=GroupsKeyboard(), parse_mode='HTML')

# Reset Groups
@bot.message_handler(commands=['reset_groups'])
def handle_command_groups_rest(message):
    if message.from_user.id in ADMINS:
        global ConstGroups , Groups
        Groups = ConstGroups
        bot.send_message(chat_id=message.chat.id, text="Groups Reseted")

# Buttons Handlers
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global isRuning, ConstGroups, Groups
    msg = call.data.split("_")
    if (msg[0] == "removeMsg"):
        Messages.pop(int(msg[1]))
        bot.edit_message_text(chat_id=call.message.chat.id,text="Messages",message_id=call.message.message_id,reply_markup=MessagesKeyboard(),parse_mode='HTML')
    if (msg[0] == "removeG"):
        del Groups[int(msg[1])]
        bot.edit_message_text(chat_id=call.message.chat.id, text="Groups", message_id=call.message.message_id, reply_markup=GroupsKeyboard(), parse_mode='HTML')
    if (msg[0] == "op"):
        if (msg[1] == "start"):
            bot.send_message(chat_id=call.message.chat.id,text="BOT OPTIONS :",reply_markup=StartKeyboard(),parse_mode='HTML')
        if (msg[1] == "groups"):
            bot.send_message(chat_id=call.message.chat.id,text="Groups",reply_markup=GroupsKeyboard(),parse_mode='HTML')
        if (msg[1] == "resetgroups"):
            Groups = ConstGroups
            bot.send_message(chat_id=call.message.chat.id, text="Groups Reseted")
        if (msg[1] == "msgs"):
            bot.send_message(chat_id=call.message.chat.id,text="Messages",reply_markup=MessagesKeyboard(),parse_mode='HTML')
        if (msg[1] == "addmsg"):
            bot.send_message(chat_id=call.message.chat.id,text='Type /add_msg Your Message Here 0w0')
        if (msg[1] == "startbot"):
            isRuning = True
            bot.send_message(chat_id=call.message.chat.id, text="STARTED .")
        if (msg[1] == "stopbot"):
            isRuning = False
            bot.send_message(chat_id=call.message.chat.id, text="STOPED .")
        if (msg[1] == "sleep"):
            bot.send_message(chat_id=call.message.chat.id,text=F"Type /sleep Your Seconds Here 0w0, For EX :\n/sleep 60")

# Run BOT 
async def RUN_BOT():
    print("[+] BOT SENDER RUNNING ...")
    while True:
        if (isRuning == True):
            for Group in Groups:
                try:
                    for Message in Messages:
                        try:await client.send_message(Group, Message)
                        except:print("[+] ERROR SEND MSG TO GROUP : "+str(Group)) 
                    print(F"[+] Sended To Group Named => {str(Groups[Group])} , Group ID => {str(Group)}")
                except:
                    print("[+] ERROR :: SENDING TO GROUP : "+str(Group))
            await asyncio.sleep(SLEEP)


def RUN_TELE_BOT():
    print("[+] TELE BOT RUNNING ...")
    BOT_TELE = asyncio.get_event_loop()
    BOT_TELE.create_task(bot.infinity_polling(timeout=10, long_polling_timeout = 5))

print("[+] STARTED")
BOT = asyncio.get_event_loop()
BOT.create_task(RUN_BOT())
Thread(target=BOT.run_forever).start()
Thread(target=RUN_TELE_BOT()).start()