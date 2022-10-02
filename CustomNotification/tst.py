  tmp = 0
  try:
    if int(message.text):
      tmp = message.text
  except:
      if s[-1]=='m':
          #minutes
          await bot.send_message(message.chat.id,int(s[0:-1]),'sec')
          tmp = int(s[0:-1])*60
      elif s[-1] == 'h':
          #hours
          await bot.send_message(message.chat.id,int(s[0:-1]),'hours')
          tmp = int(s[0:-1])*60*60
      else:
          await bot.send_message(message.chat.id,'dealy is wrong')
      print(tmp)