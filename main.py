# import
import os, logging,time,tracemalloc,asyncio
from telethon import *
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import DeleteMessagesRequest


#----------------------------------- logging --------------------------------------------
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
tracemalloc.start()
#---------------------------- set info acc ----------------------------------------------
f = open("setting.txt", "r")
setting = []
for x in f:
  setting.append(x.split("=")[1]) 

api_id = int(setting[0])
api_hash = str(setting[1])
phone_number = str(setting[2])
#------------------------------ connect client ------------------------------------------
if not os.path.exists('session'):
    os.makedirs('session')

client = TelegramClient('session/'+phone_number, api_id, api_hash)
client.start()

#------------------------------ function ------------------------------------------------
@client.on(events.NewMessage)
async def main(event):
    await event.message.click()

    if (str(event.raw_text).startswith("$")):
        pass
     
#--------------------------------- check connect client ----------------------------------
if client.is_connected():
    print('Start')
client.run_until_disconnected()