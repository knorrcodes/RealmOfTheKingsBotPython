from util.helper import logAndPrint
from util.aws import getS3Object, putS3Object
from classes.events import Events
from classes.users import Users

async def execute(self, msg, args):
    try: 
        if args[0] == "newEvent":
            if str(msg.author.id) == "304745620411777024":
                await add_event(self, msg, eventName=args[1], eventType=args[2], eventDate=args[3], eventTime=args[4], location=args[5])
        elif args[0] == "listEvents":
            listEvents = getS3Object("events")["events"]
            events_output = ""
            for key, value in listEvents.items():
                participants = []
                for user in value["participants"]:
                    participants.append(user["userName"])
                #if value["current"] not in value or value["current"] is True:
                events_output = events_output + f"Event: {value['eventName']} (EventID: {key})\n"
                # await msg.reply(
                #     f'Event ID: {key}\n'
                #     f'Event Name: {value["eventName"]}\n'
                #     f'Event Type: {value["eventType"]}\n'
                #     f'Date Created: {value["dateCreated"]}\n'
                #     f'Date Scheduled: {value["dateScheduled"]}\n'
                #     f'Event Start Time: {value["eventStart"]}\n'
                #     f'Location: {value["location"]}\n'
                #     f'Participants: {participants}\n'
                # )
            await msg.reply(events_output)
        elif args[0] == "getEventDetails":
            details = get_event_details(args[1])
            if details == "EventDoesNotExist":
                await msg.reply("Sorry but it looks like that event does not exist!")
            else: 
                event = getS3Object("events")["events"][args[1]]
                participants = []
                for user in event["participants"]:
                    participants.append(user["userName"])
                #if value["current"] not in value or value["current"] is True:
                await msg.reply(
                    f'Event ID: {args[1]}\n'
                    f'Event Name: {event["eventName"]}\n'
                    f'Event Type: {event["eventType"]}\n'
                    f'Date Created: {event["dateCreated"]}\n'
                    f'Date Scheduled: {event["dateScheduled"]}\n'
                    f'Event Start Time: {event["eventStart"]}\n'
                    f'Location: {event["location"]}\n'
                    f'Participants: {participants}\n'
                )
        elif args[0] =="deleteEvent":
            if str(msg.author.id) == "304745620411777024":
                await msg.reply(remove_event(args[1]))
        elif args[0] == "addParticipant":
            resp = await add_participant(self, msg, eventId=args[1])
            if resp == "Success":
                await msg.reply(f"Great work {msg.author}! You have successfuly registered for event {args[1]}! We look forward to seeing you there!")
            elif resp == "AlreadyExists": 
                await msg.reply(f"We love to see the interest, but it looks like you are already registered for event {args[1]}! See you there!")
            elif resp == "EventDoesNotExist":
                await msg.reply(f"Hey! Sorry but it looks like event {args[1]} doesn't exist yet! Try signing up for another event!")
            else:
                await msg.reply("Whoop! Sorry but we couldnt get you registered. Its me not you. Try again here soon!")
    except BaseException as err:
        await logAndPrint(self, msg, err, True)

async def add_admin():
    print("something")

### EVENTS ###
async def add_event(self, msg, eventName, eventType, eventDate, eventTime, location):
    #Check to make sure no event ID already exists
    try:
        print("4")
        Events(eventName, eventType, eventDate, eventTime, location)
    except BaseException as err:
        await logAndPrint(self, msg, err, True)

def get_event_details(eventId):
    eventslist = getS3Object("events")
    if eventslist["events"][eventId]:
        return eventslist["events"][eventId]
    else: 
        return "EventDoesNotExist"

def remove_event(eventId):
    eventList = getS3Object("events")
    oldList = eventList
    try: 
        del eventList["events"][eventId]
        putS3Object(eventList, oldList, "events")
        return f"Sucessfully Removed {eventId} from the events list!"
    except BaseException as err:
        print(err)
        return f"Failed to remove {eventId}!"

def update_events(new_event):
    print("something")

### PARTICIPANTS ###
async def add_participant(self, msg, eventId):
    current_users = getS3Object("users")
    current_events = getS3Object("events")
    new_users = current_users
    new_events = current_events
    print(f"Event ID: {eventId}")
    print(current_events["events"])
    try: 
        #Check to see if the event exists or not
        if eventId not in current_events["events"]:
            return "EventDoesNotExist"
        #Check to see if that user is already registered
        for user in current_events["events"][eventId]["participants"]:
            if str(msg.author.id) in user["userId"]:
                return "AlreadyExists"   
        
        #Get the user registered
        if str(msg.author.id) in current_users["users"]:
            print("1")
            new_events["events"][eventId]["participants"].append(current_users["users"][str(msg.author.id)])
            print('2')
            new_users["users"][str(msg.author.id)]["currentEvents"].append(eventId)
            print('3')
        else: 
            u1 = Users(str(msg.author), str(msg.author.id))
            new_events["events"][eventId]["participants"].append(u1.getUser())
            u1.getUser()["currentEvents"].append(eventId)
            new_users["users"][msg.author.id] = u1.getUser()
        putS3Object(new_users, current_users, "users")
        putS3Object(new_events, current_events, "events")
        await logAndPrint(self, msg, "Success!", False)
        return "Success"
    except BaseException as err:
        print(err)
        await logAndPrint(self, msg, "Failed!", False)
        return "Failed"

def remove_participant():
    print("something")

### ADMINS AND USERS
async def remove_admin():
    print("something")

def get_users():
    print("something")

def update_users(new_user):
    print("something")
