import discord
from util.secretsmanager import getsecrets

class ROTKBot(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        secrets = getsecrets()
        if message.content.startswith(secrets[1]):
            await message.reply("Hello!")
            print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = ROTKBot(intents=intents)
client.run("NzU1MTQzNjkyMzQzMzEyNDQ0.G2y4Xj.idqcbGrNDnk6bMJcQE2sUd2Xfa4lhV0EqWcc9o")