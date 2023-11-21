import discord
from util.aws import getsecrets
from util.helper import getCommand, commandExists, logAndPrint
import os
from importlib import import_module
import sys
from classes.events import Events
from classes.users import Users

class ROTKBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        secrets = getsecrets()
        args = message.content.split(' ')[1:]
        command = message.content.split(" ")[0]
        if message.content.startswith(secrets[1]):
            try: 
                print(f'Message from {message.author}: {command}')
                if commandExists(msg=command, prefix=secrets[1]):
                    sys.path.append(f'{os.getcwd()}/src/commands')
                    imported_module = import_module(getCommand(prefix=secrets[1], msg=command).lower())
                    await imported_module.execute(self, msg=message, args=args)
                else: 
                    await logAndPrint(self, message, "Hey! Sorry, it doesnt look like we have that command yet!", sendMessage=True)
            except ImportError as err:
                print(err)
            except BaseException as err:
                print("ERROR HERE")
                print(err)

intents = discord.Intents.default()
intents.message_content = True

client = ROTKBot(intents=intents)
client.run(getsecrets()[0])

# t5 = Events("test5", "test5", "test5", "test5", "test5")
# print(t5.getEvent())
# u1 = Users("dknorr", "12345").addEventToUser({"55555": {"stuff": "to add"}})
# u1.addEventToUser({"66666": {"stuff": "to add"}})
# print(u1.getUser())