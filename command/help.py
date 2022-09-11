
import discord
client = discord.Client()


@client.event
async def on_ready():
    print('目前登入身份：',client.user)

    status_w = discord.Status.dnd

   
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="Jeff is Coding discord bot")

    await client.change_presence(status= status_w, activity=activity_w)



@client.event

async def on_message(message):
    if message.content == 'help':
        
        tmpmsg = await message.channel.send("@Jeff6794#2397 is Admin")

    
    print(message.content)
    if message.author == client.user:
        return
   
    if message.content.startswith("say"):
     
      tmp = message.content.split(" ",1)
      
      print(tmp)
      if len(tmp) == 1:
        await message.channel.send(f"{message.author.mention} 你要我說什麼啦？")

      else:
        await message.channel.send(f"{message.author.mention} 他逼我說「{tmp[1]}」！！！！！！！！！！" )

    if message.content == 'who is the handsome guy':
        
        tmpmsg = await message.channel.send(f"{message.author.mention} IDK, But not you" )

    if message.content == 'who is the ugly guy':
        
        tmpmsg = await message.channel.send(f"{message.author.mention} I know , you!!!!!!!!!" )

   
    print(message.content)
    if message.author == client.user:
        return
   
    if message.content.startswith("!say"):
     
      tmp2 = message.content.split(" ",1)
      
      print(tmp2)
      if len(tmp2) == 1:
        await message.channel.send(f"{message.author.mention} 你要我說什麼啦？")

      else:
        await message.channel.send(f"{tmp2[1]}")

    if message.content == 'Cnm':
        
        tmpmsg = await message.channel.send(f"{message.author.mention} Dont Say bad word!!!!!!" )
    
    if message.content == 'wtf':
        
        tmpmsg = await message.channel.send(f"{message.author.mention} Dont Say bad word!!!!!!" ) 

    if message.content == 'Wtf':
        
        tmpmsg = await message.channel.send(f"{message.author.mention} Dont Say bad word!!!!!!" )

     

client.run('')

   
