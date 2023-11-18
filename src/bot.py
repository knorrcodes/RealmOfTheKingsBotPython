import discord
from util.secretsmanager import getsecrets
from util.helper import getCommand, commandExists, logAndPrint
import os
from importlib import import_module
import sys

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
                    await imported_module.execute(msg=message, args=args)
                else: 
                    await logAndPrint(message, "Hey! Sorry, it doesnt look like we have that command yet!", sendMessage=True)
            except ImportError as err:
                print(err)
            except BaseException as err:
                print("ERROR HERE")
                print(err)

intents = discord.Intents.default()
intents.message_content = True
#intents.members = True

client = ROTKBot(intents=intents)
client.run(getsecrets()[0])