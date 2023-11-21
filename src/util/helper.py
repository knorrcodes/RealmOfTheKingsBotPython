import os
from datetime import datetime
from typing import Any

def getCommand(prefix, msg):
    """
    :Desc:
    Retrieves the command without the prefix

    :inputs:
    prefix = ROTK bot prefix
    msg: the input message from the user command
    """
    fixed = msg.removeprefix(prefix)
    return fixed

def commandExists(msg, prefix):
    """
    :Desc:
    Validate whether or not the command given by the user exists
    and will return True or False based on the results.

    :inputs:
    msg = the input message from the user command
    prefix = the discord bot prefix

    :outputs:
    bool response = True or False
    """
    fixed = getCommand(prefix=prefix, msg=msg).lower()
    if f'{fixed}.py' in os.listdir("src/commands"):
        return True
    else: 
        return False

async def logAndPrint(self, msg: Any, contents: str, sendMessage: bool):
    """
    :Desc:
    Takes the contents and logs it to logs.txt always and then optionally
    will msg.reply to send the content to the channel where the original
    message was sent from the user

    :inputs:
    msg = the Discord.Message object
    contents: The string object you want to log or reply with
    sendMessage: Whether or not you want to send the contents to the channel as a response

    :outputs: 
    None
    """
    log = ""
    if msg == "":
        log = f"TIME: {datetime.now()} - RESPONSE: {contents}"
    else:
        log = f"TIME: {datetime.now()} - USER: {msg.author} - COMMAND: {getCommand('//', msg.content)}\n - RESPONSE: {contents}"
    logsChannel = self.get_channel(int("1175267246302572584"))
    with open("logs.txt", 'a') as file:
        #updatedContents = contents.replace('\n', '\\n')
        file.write(log)
    print(f'LOG: {contents}')
    await logsChannel.send(log)
    if sendMessage:
        await msg.reply(contents)
