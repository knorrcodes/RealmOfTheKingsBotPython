from util.aws import getS3Object, putS3Object

class Users():
    def __init__(self, userName, userId) -> None:
        self.userName = userName
        self.userId = userId
        self.currentEvents = []
        self.completedEvents = []

        self.createUser()

    def createUser(self) -> None:
        # Try and append to a copy of the events.json file and if successfull then append to the actualy
        # do this in case it fails, it wont destroy the actual document
        new_user = {
            "userName": self.userName,
            "userId": self.userId,
            "currentEvents": self.currentEvents,
            "completedEvents": self.completedEvents
        }
        
        old_data = getS3Object("users")
        
        new_data = old_data
        new_data["users"][self.userId] = new_user
        resp = putS3Object(new_data, old_data, "users")
        print(resp)

    def addEventToUser(self, event_obj):
        self.currentEvents.append(event_obj)
        return self

    def addCompletedEvents(self, event_obj):
        if event_obj in self.currentEvents:
            self.currentEvents.remove(event_obj)
        self.completedEvents.append(event_obj)
        return self
    
    def getUser(self):
        return {
            "userName": self.userName,
            "userId": self.userId,
            "currentEvents": self.currentEvents,
            "completedEvents": self.completedEvents
        }