from telethon import TelegramClient, events, sync
import re

api_id = 'api id'
api_hash = 'api hash'
regex = r"BTC_CHANGE_BOT\?start="

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage())
async def normal_handler(event):
    user_mess = event.message.to_dict()['message']
    m_from = event.message.to_dict()
    to_id = event.message.to_dict()['to_id']['channel_id']

    if re.search(r'BTC_CHANGE_BOT\?start=', user_mess):
        m = re.search(r'c_\S+', user_mess)
        await client.send_message('BTC_CHANGE_BOT', '/start ' + m.group(0))
        print(m.group(0))

client.start()
client.run_until_disconnected()
