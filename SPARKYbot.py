
import discord
from discord.ext import commands
import json
import os
import random
import asyncio
import datetime

os.chdir("/storage/emulated/0/!superbot")


def get_prefix(client,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)

bot = commands.Bot(command_prefix=get_prefix)

@client.event
async def on_guild_join(guild):


    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "*"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)



@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    

    await ctx.send(f"The prefix was changed to {prefix}")



@client.event
async def on_message(msg):

    try:
        if msg.mentions[0] == client.user:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(msg.guild.id)] 

            await msg.channel.send(f"My prefix for this server is {pre}")

    except:
        pass

    await client.process_commands(msg)


mainshop = [{"name":"Watch","price":100,"description":"Time"},
            {"name":"Laptop","price":1000,"description":"Work"},
            {"name":"PC","price":10000,"description":"Gaming"}]

links = ["www","https","discord.gg/"]

@client.event
async def on_ready():
	print('bot is ready')
	
@client.event
async def on_message(msg):
	for word in links:
		if word in msg.content:
			await msg.delete()
			await msg.channel.send("Links Not Allowed")
			
		if ":" == msg.content[0] and ":" == msg.content[-1]:
			emoji_name = msg.content[1:-1]
			for emoji in msg.guild.emojis:
				  if emoji_name == emoji.name:
				  	await msg.content.send(str(emoji))
				  	await msg.delete()
				  	break
					
			
	await client.process_commands(msg)
	
@client.event
async def on_command_error(ctx,error):
		if isinstance(error,commands.MissingPermissions):
			await ctx.send("You don't have enough permissions to use that command")
		elif isinstance(error,commands.MissingRequiredArgument):
			await ctx.send("You didn't use the command correctly")
		else:
			print(error)

	
@client.command(aliases=['purge'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount +1)
	await ctx.send("Deleted messages")
	
@client.command(aliases=['Kick'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason = "No Reason Provided"):
	await ctx.send(member.name + " has been kicked. Reason:"+reason)
	await member.kick(reason=reason)
	
@client.command(aliases=['Ban'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason = "No Reason Provided"):
	await ctx.send(member.name + " has been banned. Reason:"+reason)
	await member.ban(reason=reason)
	
@client.command(aliases=['Unban'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')
	for banned_entry in banned_users:
		user = banned_entry.user
		
		if(user.name,user.discriminator)==(member_name,member_disc):
			
			await ctx.guild.unban(user)
			await ctx.send(member_name +" has been unbanned")
			return
	await ctx.send(member +" was not found")
	
@client.command()
@commands.has_permissions(kick_members=True)
async def whois(ctx,member : discord.Member):
	embed = discord.Embed(title = member.name , description = member.mention , colour = discord.Colour.red())
	embed.add_field(name = "ID", value = member.id, inline = True)
	embed.set_thumbnail(url = member.avatar_url)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
	await ctx.send(embed=embed) 
	
@client.command()
async def poll(ctx,*, msg):
	channel = ctx.channel
	try:
		op1 , op2 = msg.split("or")
		txt = f"react with 1️⃣ for {op1} or 2️⃣ for {op2}"
	except:
			await channel.send("correct Syntax: [choice1] or [choice2]")
			return
			
	
	embed = discord.Embed(title = "poll", description = txt, colour = discord.Colour.red())
	message_ = await channel.send(embed=embed)
	await message_.add_reaction("1️⃣")
	await message_.add_reaction("2️⃣")
	await ctx.messge.delete()
	
@client.command(aliases=['bal'])
async def balance(ctx):
	await open_account(ctx.author)
	user = ctx.author
	users = await get_bank_data()

	wallet_amt = users[str(user.id)]["wallet"]
	bank_amt = users[str(user.id)]["bank"]
	
	
	em = discord.Embed(title = f"{ctx.author.name}'s balance",colour = discord.Colour.green())
	em.add_field(name = "Wallet",value = wallet_amt)
	em.add_field(name = "bank",value = bank_amt)
	await ctx.send(embed = em)
	
	
@client.command()
async def beg(ctx):
	await open_account(ctx.author)
	
	users = await get_bank_data()
	
	user = ctx.author
	
	earnings = random.randrange(101)
	
	
	await ctx.send(f"Someone gave you {earnings} coins")	
	
	
	users[str(user.id)]["wallet"] += earnings
	
	with open("mainbank.json","w") as f:
		json.dump(users,f)
	
@client.command(aliases=['with'])
async def withdraw(ctx,amount = None):
	await open_account(ctx.author)
	
	if amount == None:
		await ctx.send("Please enter the amount")
		return
	
	bal = await update_bank(ctx.author)
	
	amount = int(amount)
	if amount>bal[1]:
		await ctx.send("You don't have that much money")
		return
	if amount<0:
		await ctx.send("You can't put that amount")
		return
		
	await update_bank(ctx.author,amount)
	await update_bank(ctx.author,-1*amount,"bank")
	
	await ctx.send(f"You withdrew {amount} coins from your bank!")
		
async def open_account(user):
		
		users = await get_bank_data()
		
		if str(user.id) in users:
			return False
		else:
			users[str(user.id)] = {}
			users[str(user.id)]["wallet"] = 0
			users[str(user.id)]["bank"] = 0
			
		with open("mainbank.json","w") as f:
			json.dump(users,f)
		return True
		
		
		
async def get_bank_data():
		with open("mainbank.json","r") as f:
			users = json.load(f)
			
		return users
		
		
async def update_bank(user,change = 0,mode = "wallet"):
	users = await get_bank_data()
	
	users[str(user.id)][mode] += change
	
	with open("mainbank.json","w") as f:
		json.dump(users,f)
		
	bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
	return bal
	
	
@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):
	await open_account(ctx.author)
	
	if amount == None:
		await ctx.send("Please enter the amount")
		return
	
	bal = await update_bank(ctx.author)
	
	amount = int(amount)
	if amount>bal[0]:
		await ctx.send("You don't have that much money")
		return
	if amount<0:
		await ctx.send("You can't put that amount")
		return
		
	await update_bank(ctx.author,-1*amount)
	await update_bank(ctx.author,amount,"bank")
	
	await ctx.send(f"You deposited {amount} coins from your wallet!")
		
async def open_account(user):
		
		users = await get_bank_data()
		
		if str(user.id) in users:
			return False
		else:
			users[str(user.id)] = {}
			users[str(user.id)]["wallet"] = 0
			users[str(user.id)]["bank"] = 0
			
		with open("mainbank.json","w") as f:
			json.dump(users,f)
		return True
		
		
		
async def get_bank_data():
		with open("mainbank.json","r") as f:
			users = json.load(f)
			
		return users
		
		
async def update_bank(user,change = 0,mode = "wallet"):
	users = await get_bank_data()
	
	users[str(user.id)][mode] += change
	
	with open("mainbank.json","w") as f:
		json.dump(users,f)
		
	bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
	return bal
	
@client.command(aliases=['pay'])
async def give(ctx,member : discord.Member,amount = None):
	await open_account(ctx.author)
	await open_account(member)
	if amount == None:
		await ctx.send("Please enter the amount")
		return
	
	bal = await update_bank(ctx.author)
	
	amount = int(amount)
	if amount>bal[1]:
		await ctx.send("You don't have that much money in your bank!")
		return
	if amount<0:
		await ctx.send("You can't put that amount")
		return
		
	await update_bank(ctx.author,-1*amount,"bank")
	await update_bank(member,amount,"bank")
	
	await ctx.send(f"You gave {amount} coins!")
	
	
@client.command()
async def slots(ctx,amount = None):
	await open_account(ctx.author)
	
	if amount == None:
		await ctx.send("Please enter the amount")
		return
	
	bal = await update_bank(ctx.author)
	
	amount = int(amount)
	if amount>bal[0]:
		await ctx.send("You don't have that much money")
		return
	if amount<0:
		await ctx.send("You can't put that amount")
		return
		
	final = []
	for i in range(3):
		a = random.choice(["🍕","💲","💠","🎊","🎉","⚡"])
		
		final.append(a)
		
	await ctx.send(str(final))
		
	if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
		await update_bank(ctx.author,2*amount)
		await ctx.send("You won!")
	else:
		await update_bank(ctx.author,-1*amount)
		await ctx.send("You lost!")
		
@client.command()
async def rob(ctx,member : discord.Member):
	await open_account(ctx.author)
	await open_account(member)
	
	bal = await update_bank(member)
	
	if bal[0]<100:
		await ctx.send("The user doesn't have much money in their wallet")
		return
		
	earnings = random.randrange(0, bal[0])
		
	await update_bank(ctx.author,earnings)
	await update_bank(member,-1*earnings)
	
	await ctx.send(f"You robbed and got {earnings} coins!")
	
@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)



@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")


@client.command(aliases=['inv'])
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Your Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em) 
async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]
    
@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]
 
@client.command(aliases = ["lb"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)
    
    
client.run("TOKEN")
