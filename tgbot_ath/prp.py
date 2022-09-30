from telethon import TelegramClient, events
import asyncio


api_id=7427530
api_hash='86945cc35c57c8131c16566cb37f0249'

#Канал(ы) на которые постим
my_channel_id='@TL2_concept'

#Канал(ы) с которых постим
channels=[-1001270106774,-1001412801292,-1001240018332,'@FlyAgaric_Mushrooms']

BADTEXT = {'t.me', 'http', 'подписаться', '@', 'joinchat'} # исключения

client = TelegramClient('Grab_TrashBot', api_id, api_hash)
print("GRAB - Started")

def to_lower(word: str):
    return word.lower()
                 
@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event: events.newmessage.NewMessage.Event):
    global BADTEXT
    message_text = event.raw_text
    message_text_lowered = event.raw_text.lower()   
    if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        await asyncio.sleep(0.5) #задержка
        await client.send_message(my_channel_id, event.message)
            
@client.on(events.Album(chats=channels))
async def handler(event):
    await client.send_message(my_channel_id,
        file=event.messages,
         message=event.original_update.message.message,)

with client:
    client.run_until_disconnected() 
    