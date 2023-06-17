# import
import os, logging,time,tracemalloc,asyncio
from telethon import *
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import DeleteMessagesRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

#----------------------------------- logging --------------------------------------------
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
tracemalloc.start()
#---------------------------- set info acc ----------------------------------------------
f = open("setting.txt", "r")
setting = []
for x in f:
  setting.append(x.split("=")[1]) 

api_id = 1331656
api_hash = '868c8254ed0fbc05a5ef0dab474ffdf9'
phone_number = '+989330362596'
#------------------------------ connect client ------------------------------------------
if not os.path.exists('session'):
    os.makedirs('session')

client = TelegramClient('session/'+phone_number, api_id, api_hash)
client.start()

#------------------------------ function ------------------------------------------------
async def joinLeave(link, status):
    if status==0:
        await client(JoinChannelRequest(str(link)))
    else:
        await client(LeaveChannelRequest(str(link)))
    
async def getMember(link):
    await joinLeave(link, 0)
    async for user in client.iter_participants(str(link)):
        print(user)

@client.on(events.NewMessage)
async def main(event):
    await event.message.click()

    if (str(event.raw_text).startswith("$")):
        pass
     
#--------------------------------- check connect client ----------------------------------
if client.is_connected():
    print('Start')
client.run_until_disconnected()