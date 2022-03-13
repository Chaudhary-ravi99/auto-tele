# Info 
# Start this Tool then go to the Telegram Group you want to find his ID and send any message, the ID will show in the console.

from telethon import TelegramClient, events, sync

client = TelegramClient('session_name',"API_ID","API_HASH")
client.start()

@client.on(events.NewMessage(from_users=client.get_me().id))
async def handler(event):
    print("CHAT ID : "+str(event.chat_id))
client.run_until_disconnected()
