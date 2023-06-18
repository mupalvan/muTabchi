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
phone_number = '+989338429252'
#------------------------------ connect client ------------------------------------------
if not os.path.exists('session'):
    os.makedirs('session')

client = TelegramClient('session/'+phone_number, api_id, api_hash)
client.start()

#------------------------------ function ------------------------------------------------
async def joinLeave(link, status):
    try:
        if status==0:
            try:
                await client(ImportChatInviteRequest(str(link)))
            except:
                await client(JoinChannelRequest(str(link)))
        else:
            await client(LeaveChannelRequest(str(link)))
    except:
        pass

async def getMember(link):
    await joinLeave(link, 0)
    async for user in client.iter_participants(str(link)):
        print(user.id)

@client.on(events.NewMessage)
async def main(event):
    await event.message.click()

    if (str(event.raw_text).startswith("/getm")):
        if str(event.raw_text).split("/")[-1] != "":
            link = str(event.raw_text).split("/")[-1]
        else:
            link = str(event.raw_text).split("/")[-2]
        
        print(link)
        await getMember(link)
     
#--------------------------------- check connect client ----------------------------------
if client.is_connected():
    print('Start')
client.run_until_disconnected()