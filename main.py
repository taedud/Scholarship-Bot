import requests
from bs4 import BeautifulSoup
import telegram
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Bot's token
bot=telegram.Bot(token="5010570024:AAHdPgLDEUySVEJ1CjE_yZe1im77qOHdGho")

#chating room id
chat_id = 5010614602

#infinite root
while True:
#site url
  url = "http://pc-scholarship.or.kr/community/notice" 
  req=requests.get(url)
  soup=BeautifulSoup(req.content,"html.parser")

  #read information
  posts=soup.select('td.board-num--fc')
  subj=soup.select('td.board-subject--fc')
  date=soup.select('td.board-date--fc')

  #latest information
  latest=subj[0].text
  lsubj=subj[0].text
  ldate=date[0].text  

#read file
  with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    #old subject
      before = f_read.readline()
      if before != latest:
          bot.sendMessage(chat_id=chat_id, text='장학재단에 새 글이 올라왔어요!\n'+lsubj+'\n 날짜: '+ldate)
      f_read.close()

#write file
  with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
      f_write.write(latest)
      f_write.close()

  time.sleep(3600)