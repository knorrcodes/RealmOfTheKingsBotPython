from util.helper import logAndPrint

async def execute(self, msg, args):
    """
    :Desc:
    Returns the User name and User ID

    :inputs:
    msg = the Discord.Message object

    :outputs:
    None
    """
    resp = f"User: {str(msg.author)}\nID: {str(msg.author.id)}"
    await logAndPrint(self, msg, resp, sendMessage=True)
