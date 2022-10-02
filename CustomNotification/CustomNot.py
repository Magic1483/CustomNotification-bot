import asyncio
import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from valuts import get_price


from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()
bot = Bot(token='1321270292:AAFPRksSAZR2u4V7ohtGDtx3jgwi_Lh_b-0')
dp = Dispatcher(bot,storage=storage)




class Form(StatesGroup):
    symbol = State()
    delay = State()
    
    
    
      
  
async def Notification(delay, message,data):
  while True:
    tmpString=''
    for i in data:
      tmp = ' '.join(map(str, i))
      price=f"{tmp}:{round(get_price(tmp),3)} USDT"
      
      tmpString+=price+'\n'
    await bot.send_message(message.chat.id,tmpString)
    await asyncio.sleep(delay)
    
    


def CheckId(id):
  #connect DB
  connect=sqlite3.connect('db.db')
  cursor=connect.cursor()
  #check id exist
  cursor.execute(f'SELECT id FROM users WHERE id={id}')
  data = cursor.fetchone()
  if data != None:
    return True
  else: 
    return False


def CheckSymbol(user_id,symbol):
  #connect DB
  connect=sqlite3.connect('db.db')
  cursor=connect.cursor()
  #check id exist
  cursor.execute(f"""SELECT symbol FROM valuts WHERE ( user_id={user_id} AND symbol='{symbol}')""")
  data = cursor.fetchone()
  if data == None:
    return True
  else: 
    return False

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message,state: FSMContext):
    await bot.send_photo(
        message.chat.id,
        'https://img.discogs.com/3_j4VhfbWwBSpFtRwaCFx_Yohgg=/fit-in/500x500/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-14178205-1569327372-9612.jpeg.jpg'
    )
    #connect DB
    connect=sqlite3.connect('db.db')
    cursor=connect.cursor()

    #check id exist
    user_id=[message.chat.id]
    
  
    cursor.execute(f'SELECT id FROM users WHERE id={user_id[0]}')
    data = cursor.fetchone()
    if data is None:
      #insert into DB
      cursor.execute("INSERT INTO users VALUES(?);",user_id)
      connect.commit()
    else:
      await bot.send_message(message.chat.id,f'user is exist:  {user_id[0]}');

    await state.update_data(user_id=user_id[0])
    await asyncio.sleep(0.1)
    await bot.send_message(message.chat.id,
                     "Вы запустили Azrael - тестовая версия --"+
                     f"\nПомощь: \help")






@dp.message_handler(commands=['help'])  #/com
async def t4_command(message):
    await bot.send_message(
        message.chat.id,
        "тест кастомных уведомлений\n/get_s - получить все свои валюты\n/add_s - добавить валюту"+
        "\n/del_s - удалить свои валюты\n/cs - включить уведомления\n/ex - выключить уведомления"
    )



@dp.message_handler(commands=['ex'])
async def exit(message: types.Message):
  await message.reply(f'Close Session {message.chat.id}')
  task, = [task for task in asyncio.all_tasks() if task.get_name() == str(message.chat.id)]
  task.cancel()


@dp.message_handler(commands=['cs'])
async def exit(message: types.Message):
  await message.answer(text='Write delay ')
  await Form.delay.set()

@dp.message_handler(commands=['add_s'])  #/com
async def l1(message):
  await message.answer(text='Write symbol ')
  await Form.symbol.set()

@dp.message_handler(commands=['get_s'])  #/com
async def l3(message):
  if CheckId(message.chat.id)==True:
    #connect DB
    connect=sqlite3.connect('db.db')
    cursor=connect.cursor()
    cursor.execute(f"""SELECT symbol FROM valuts  WHERE user_id='{message.chat.id}'""")
    data = cursor.fetchall()
    if not data:
      await bot.send_message(message.chat.id,'U hav not crypto');
    else:
      await bot.send_message(message.chat.id,f'Your crypto is:');
      for i in data:
        tmp = ' '.join(map(str, i))
        await bot.send_message(message.chat.id,tmp);

@dp.message_handler(commands=['del_s'])  #/com
async def l4(message):
  if CheckId(message.chat.id)==True:
    #connect DB
    connect=sqlite3.connect('db.db')
    cursor=connect.cursor()
    #print(message.chat.id)
    cursor.execute(f"""DELETE FROM valuts  WHERE user_id={message.chat.id}""")
    connect.commit()
    await bot.send_message(message.chat.id,f'Your crypto is deleted')

    



@dp.message_handler(state=Form.symbol,content_types=types.ContentTypes.TEXT)
async def process_symbol(message: types.Message,state: FSMContext):
  #await state.update_data(symbol=message.text.title())
  #connect DB
  connect=sqlite3.connect('db.db')
  cursor=connect.cursor()
  
  user_id=message.chat.id
  #print(user_id)
  #print(message.text.upper())
  #print(CheckId(user_id),CheckSymbol(user_id,message.text.upper()))
  
  if (CheckId(user_id)==True):
    #if user is exist but symbol isn't exist
    if (CheckSymbol(user_id,message.text.upper())==True):
      #insert into DB
      cursor.execute(f"""INSERT INTO valuts (user_id, symbol) VALUES ('{user_id}', '{message.text.upper()}');""")
      connect.commit()
      await bot.send_message(message.chat.id,f'[{message.text.upper()}] succesfully added')
    else:
      await bot.send_message(message.chat.id,'Symbol already exist')
  else:
    await bot.send_message(message.chat.id,'UNDEFINED ID')
  await state.finish()
    
  
  
  

@dp.message_handler(state=Form.delay)
async def process_delay(message: types.Message,state: FSMContext):
  #await state.finish()
  #await message.reply(f'ur delay is {message.text}')
  tmp = 0
  s = message.text
  
  if s.isdigit():
    tmp = int(s)
  elif s[-1]=='m' and s[0:-1].isdigit():
    #minutes
    await bot.send_message(message.chat.id,f'Delay is:{int(s[0:-1])} min')
    tmp = int(s[0:-1])*60
  elif s[-1] == 'h' and s[0:-1].isdigit():
    #hours
    await bot.send_message(message.chat.id,f'Delay is:{int(s[0:-1])} hours')
    tmp = int(s[0:-1])*60*60          
   
  #print(tmp)
  
  if tmp!=0:
    await state.update_data(delay=tmp)
    
    user_data = await state.get_data()
    await state.finish()

    connect=sqlite3.connect('db.db')
    cursor=connect.cursor()
    cursor.execute(f"""SELECT symbol FROM valuts  WHERE user_id='{message.chat.id}'""")
    data = cursor.fetchall()
    
    await asyncio.create_task(Notification(int(user_data['delay']), message,data),name=str(message.chat.id))
  else:
    await bot.send_message(message.chat.id,f'Delay is wrong\nClose Session {message.chat.id}')




print('CnBot successfully started!!')

if __name__ == '__main__':
    executor.start_polling(dp)

