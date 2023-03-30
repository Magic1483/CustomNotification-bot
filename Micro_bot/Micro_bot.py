
from pyrogram import Client
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from voice_decode import voice_decode
from pyrogram import enums


api_id=000 #your api id
api_hash=''
bot_token =''

app = Client("nn",api_hash=api_hash,api_id=api_id,bot_token=bot_token)



@app.on_message(filters.voice)
async def my_handler(client,message):
    #print(message)
    await app.download_media(message.voice.file_id,file_name='voice.ogg')
    await message.reply_text(voice_decode())
    # await app.send_message(message.chat.id,voice_decode())
    
@app.on_message(filters.command(["help"]))
async def help(clent,message):
    await message.reply_text(
        text='Привет это бот для расшифровки гс\n'+
        'Он отправляет текст с расшифровкой войсов которые вы ему отправляете'   
    )

app.run()
print('started')

