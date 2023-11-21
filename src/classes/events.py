import random
from datetime import datetime
from util.aws import getS3Object, putS3Object

class Events():
    def __init__(self, eventName, eventType, eventDate, eventTime, location) -> None:
        self.eventName = eventName
        self.eventType = eventType
        self.eventDate = eventDate
        self.eventTime = eventTime
        self.location = location
        self.dateCreated = str(datetime.now())
        self.id = str(self.getUniqueEventId())
        self.participants = []
        
        self.createEvent()

    def getEvent(self):
        return { 
            self.id: {
                "eventName": self.eventName,
                "eventType": self.eventType,
                "dateCreated": self.dateCreated,
                "dateScheduled": self.eventDate,
                "eventStart": self.eventTime,
                "location": self.location,
                "participants": self.participants
            }
        }

    def createEvent(self) -> None:
        # Try and append to a copy of the events.json file and if successfull then append to the actualy
        # do this in case it fails, it wont destroy the actual document
        new_event = {
            "eventName": self.eventName,
            "eventType": self.eventType,
            "dateCreated": self.dateCreated,
            "dateScheduled": self.eventDate,
            "eventStart": self.eventTime,
            "location": self.location,
            "participants": self.participants
        }
        
        old_data = getS3Object("events")
        
        new_data = old_data
        new_data["events"][self.id] = new_event
        resp = putS3Object(new_data, old_data, "events")
    
    def getUniqueEventId(self) -> str:
        data = getS3Object("events")
        keys = data["events"].keys()
        # for event_dict in data['events']:
        #     keys.extend(event_dict.keys())
        while True: 
            id = random.randint(10000,99999)
            if id in keys:
                pass
            else:
                return id