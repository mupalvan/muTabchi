# import
import os, logging,time,tracemalloc,asyncio
from telethon import *
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import DeleteMessagesRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest

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
async def joinLeave(link, status): #Complite
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

def linkmaker(link): #Complite
    links = []
    for i in link:
        try:
            links.append(str(i).split("+")[1])
        except:
            links.append(str(i).split("/")[-1])
    return links

async def getMember(link): #Complite
    try:
        links = linkmaker(link)
        await joinLeave(links[0], 0)
        members = []
        async for user in client.iter_participants(link[0], limit=100):
            members.append(user.id)
        return members
    except:
        pass

async def moveMember(member, link):
    for i in member:
        try:
            try:
                print(link)
                result = client(functions.channels.InviteToChannelRequest(
                    channel=link,
                    users=[i]
                ))
            except:
                await client(AddChatUserRequest(
                    "@testgpgpg",
                    int(i),
                    fwd_limit=10
                ))
            print("add {}".format(member))

        except Exception as e:
            print(e)
            if (e.__class__.__name__ == "FloodWaitError"):
                print('sleep', e.seconds)
                await asyncio.sleep(e.seconds + 10)
                continue
            else:
                continue
        
@client.on(events.NewMessage)
async def main(event):
    await event.message.click()
    if (str(event.raw_text).startswith("/getm")):
        likns = ['','']
        likns[0] = str(event.raw_text).split(" ")[1]
        likns[1] = str(event.raw_text).split(" ")[2]
        members = await getMember(likns)
        links = linkmaker(likns)
        await moveMember(members, likns[1])

#--------------------------------- check connect client ----------------------------------
if client.is_connected():
    print('Start')
client.run_until_disconnected()

