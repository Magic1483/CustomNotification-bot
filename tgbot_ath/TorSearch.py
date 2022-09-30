#pip3 install https://github.com/rachmadaniHaryono/we-get/archive/refs/tags/1.1.5.tar.gz
#myrepls

from we_get.core.we_get import WG
import string
from ast import Global
import string
import os
import sys

def TSearch(send):
  we_get = WG()
  we_get.parse_arguments(['--search',send,'--json','--target','1337x,the_pirate_bay,yts,eztv,limetorrents'])
  res = we_get.start(api_mode=True)

  res1=str(res)

  arr=res1.split("('")
  result=''
  for i in arr:
    result=result+i+'\n\n'
      
  f1=open("t4.txt","w+")
  f1.write(result)
  f1.close