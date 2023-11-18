from  util.helper import logAndPrint
from util.secretsmanager import getsecrets
import discord

async def execute(self, msg, args):
    """
    :Desc: 
    Sends a Discord.Embed with details about the bot

    :inputs:
    msg = the Discord.Message object

    :outputs:
    None
    """
    try: 
        embed = discord.Embed(
            title="Realm of The Kings Bot!",
            description=f"Welcome to the Realm of The Kings Bot! Here you can get a list of all of our current commands.\nDont forget to prefix with {getsecrets()[1]}",
            color=discord.Color.blue()
        )
        embed.add_field(name="me", value="Returns your User name and ID", inline=True)
        await msg.reply(embed=embed)
        await logAndPrint(self, msg, contents="Successfully send ROTK Embed", sendMessage=False)
    except BaseException as err:
        await logAndPrint(self, msg, err)
