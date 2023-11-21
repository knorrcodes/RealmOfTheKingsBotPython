from util.helper import logAndPrint
from util.aws import getS3Object, putS3Object
from classes.events import Events
from classes.users import Users

async def execute(self, msg, args):
    try: 
        if args[0] == "new":
            await add_event(self, msg, eventName=args[1], eventType=args[2], eventDate=args[3], eventTime=args[4], location=args[5])
        elif args[0] == "getEvent":
            await msg.reply(getS3Object("events"))
        elif args[0] == "addParticipant":
            await add_participant(self, msg, eventId=args[1])
    except BaseException as err:
        await logAndPrint(self, msg, err, True)

async def add_admin():
    print("something")

### EVENTS ###
async def add_event(self, msg, eventName, eventType, eventDate, eventTime, location):
    #Check to make sure no event ID already exists
    try:
        Events(eventName, eventType, eventDate, eventTime, location)
    except BaseException as err:
        await logAndPrint(self, msg, err, True)

def remove_event(eventId):
    print("do something")

def update_events(new_event):
    print("something")

### PARTICIPANTS ###
def add_participant(self, msg, eventId):
    current_users = getS3Object("users")
    current_events = getS3Object("events")
    new_users = current_users
    new_events = current_events
    print("here")
    if msg.author.id in current_users["users"]:
        print("here2")
        new_events["events"][eventId]["participants"].append(current_users[msg.author.id])
        print("here4")
        new_users["users"][msg.author.id]["currentEvents"].append(current_events["events"][eventId])
    else: 
        print("here3")
        print(msg.author, msg.author.id)
        u1 = Users(str(msg.author), str(msg.author.id))
        print("here5")
        new_events["events"][eventId]["participants"].append(u1.getUser())
        print("here6")
        u1.getUser()["currentEvents"].append(current_events["events"][eventId])
        print("here7")
        new_users["users"][msg.author.id] = u1.getUser()
        new_users["users"][msg.author.id]["currentEvents"].append(current_events["events"][eventId])
        print("here8")

    putS3Object(new_users, current_users, "users")
    putS3Object(new_events, current_events, "events")

def remove_participant():
    print("something")

### ADMINS AND USERS
async def remove_admin():
    print("something")

def get_users():
    print("something")

def update_users(new_user):
    print("something")

remove_event("123")