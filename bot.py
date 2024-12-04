import discord, dbint, datetime, requests, json
from discord.ext import commands

myid = 301014178703998987 #Creator's ID

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command("help")
tree = client.tree

@client.event
async def on_ready():
    print(f"Sowitawy now online with {round(client.latency * 1000)}ms ping.")

def checkuser(username):
    user = requests.post("https://users.roblox.com/v1/usernames/users", json={"usernames": [username], "excludeBannedUsers": True})
    user = json.loads(user.text)
    if "errors" in user:
        return (None, discord.Embed(title="Error", colour=Colours.black, description=f"Uh-oh, it looks like something went wrong\nAre you sure that user exists/their name was spelled correctly?"))
    thumbnail = json.loads(requests.get("https://thumbnails.roblox.com/v1/users/avatar-headshot", params={"userIds": [user["data"][0]["id"]], "size": "720x720", "format": "Png", "isCircular": False}).text)["data"][0]["imageUrl"]
    return (True)

#class Colours:
    #red = 0xe05151
    #orange = 0xdbc067
    #green = 0x7ced68
    #blue = 0x518ae0
    #black = 0x2e2e2e

@tree.command(name="send", description="Send a user to solitary")
@discord.app_commands.choices(timetype = [
    discord.app_commands.Choice(name="Years", value="31536000"), #integer limit error fr
    discord.app_commands.Choice(name="Months", value="2592000"),
    discord.app_commands.Choice(name="Weeks", value="604800"),
    discord.app_commands.Choice(name="Days", value="86400"),
    discord.app_commands.Choice(name="Hours", value="3600"),
    discord.app_commands.Choice(name="Minutes", value="60"),
    discord.app_commands.Choice(name="Seconds", value="1")
])
async def send(interaction : discord.Interaction, username : str, timetype : discord.app_commands.Choice[str], timeamount : int):
    check = checkuser(username)
    if not check[0]:
        await interaction.response.send_message(embed=check)
    logschannel = client.get_channel(1190765333968060416)
    logmsg = await logschannel.send(embed=discord.Embed(title="Solitary", colour=Colours.red, description=f"**{user['data'][0]['name']}** has been __Sent to Solitary__\nby {interaction.user.mention} for `{timeamount} {timetype.name}`").set_thumbnail(url=thumbnail))
    await interaction.response.send_message(embed=discord.Embed(title="Successful", colour=Colours.blue, description=f"Your command went through successfully!\n**Log:**{logmsg.jump_url}"))
    dbint.currin.insert(user["data"][0]["id"], (datetime.datetime.now() + datetime.timedelta(seconds=(timetype.value * timeamount))))

@tree.command(name="update", description="Update a user's time in solitary")
@discord.app_commands.choices(timetype = [
    discord.app_commands.Choice(name="Years", value="31536000"), #integer limit error fr
    discord.app_commands.Choice(name="Months", value="2592000"),
    discord.app_commands.Choice(name="Weeks", value="604800"),
    discord.app_commands.Choice(name="Days", value="86400"),
    discord.app_commands.Choice(name="Hours", value="3600"),
    discord.app_commands.Choice(name="Minutes", value="60"),
    discord.app_commands.Choice(name="Seconds", value="1")
])
async def update(interaction : discord.Interaction, username : str, timetype : discord.app_commands.Choice[str], timeamount : int):
    check = checkuser(username)
    if not check[0]:
        await interaction.response.send_message(embed=check)
    logschannel = client.get_channel(1190765333968060416)
    logmsg = await logschannel.send(embed=discord.Embed(title="Solitary", colour=Colours.orange, description=f"**{user['data'][0]['name']}** has had their __Sentence Updated__\nby {interaction.user.mention} to `{timeamount} {timetype.name}`").set_thumbnail(url=thumbnail))
    await interaction.response.send_message(embed=discord.Embed(title="Successful", colour=Colours.blue, description=f"Your command went through successfully!\n**Log:**{logmsg.jump_url}"))
    dbint.currin.update(user["data"][0]["id"], (datetime.datetime.now() + datetime.timedelta(seconds=(timetype.value * timeamount))))

@tree.command(name="free", description="Remove a user from solitary")
async def free(interaction : discord.Interaction):
    check = checkuser(username)
    if not check[0]:
        await interaction.response.send_message(embed=check)
        return
    logschannel = client.get_channel(1190765333968060416)
    logmsg = await logschannel.send(embed=discord.Embed(title="Solitary", colour=Colours.green, description=f"**{user['data'][0]['name']}** has been __Freed from Solitary__\nby {interaction.user.mention}").set_thumbnail(url=thumbnail))
    await interaction.response.send_message(embed=discord.Embed(title="Successful", colour=Colours.blue, description=f"Your command went through successfully!\n**Log:**{logmsg.jump_url}"))
    dbint.currin.remove(user["data"][0]["id"])

@client.command()
@commands.check(lambda ctx : ctx.author.id == myid)
async def connect(ctx):
    await tree.sync()

client.run("MTE5MDc5OTUzNTMyMTEyOTA3Mw.GnU9vI.MQV2xiTSNAVOae5Vd9gshTkawH8uvB7e_NYiZE")
#https://discord.com/api/oauth2/authorize?client_id=1190799535321129073&permissions=8&scope=bot