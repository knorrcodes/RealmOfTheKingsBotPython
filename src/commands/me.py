from util.helper import logAndPrint

async def execute(msg, args):
    """
    :Desc:
    Returns the User name and User ID

    :inputs:
    msg = the Discord.Message object

    :outputs:
    None
    """
    resp = f"User: {str(msg.author)}\nID: {str(msg.author.id)}"
    await logAndPrint(msg, resp, sendMessage=True)
