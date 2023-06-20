# import
import os, logging,time,tracemalloc,asyncio, sqlite3
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
api_id = 1331656
api_hash = '868c8254ed0fbc05a5ef0dab474ffdf9'
phone_number = '+989923162636'
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
    
def addMemberToDatabase(id): #Complite
    try:
        conn = sqlite3.connect('users.db')
        conn.execute("INSERT INTO member (id) \
            VALUES ({})".format(id));
        conn.commit()
        conn.close()
    except:
        pass

async def moveMember(member, link, status):
    # for i in member:
        try:
            if status==0:
                print("Move M------------------")
                await client(AddChatUserRequest(
                    "https://t.me/joinchat/T80gGmfAzgtmNmM8",
                    '@sisoc0',
                    fwd_limit=10  # Allow the user to see the 10 last messages
                ))
                # await client(InviteToChannelRequest(
                #     channel="https://t.me/joinchat/T80gGmfAzgtmNmM8", 
                #     users=['@sisoc0'] 
                # ))
                print("down")
                    # addMemberToDatabase(i)
            else:
                pass

        except Exception as e:
            print(e)
            if (e.__class__.__name__ == "FloodWaitError"):
                print('sleep', e.seconds)
                await asyncio.sleep(e.seconds + 10)
                pass
                # continue
            else:
                pass
                # continue
        
@client.on(events.NewMessage)
async def main(event):
    await event.message.click()
    if (str(event.raw_text).startswith("/ga")):
        likns = ['',''] #link = https://.../../..
        likns[0] = str(event.raw_text).split(" ")[1]
        likns[1] = str(event.raw_text).split(" ")[2]
        members = await getMember(likns)
        links = linkmaker(likns) #link : https://.../../ss ----> links = ss 
        await moveMember(members, likns[1], 0)

#--------------------------------- check connect client ----------------------------------
if client.is_connected():
    print('Start')
client.run_until_disconnected()

