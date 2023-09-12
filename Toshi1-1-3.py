import discord, os, random, time, re
from discord.ext import commands


#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN="TOKEN"
bot = commands.Bot(command_prefix=['>', 'toshi ', 'toshi', 'Toshi ', 't.', 't. '])



#Bot events:                                         commands-and-actions-here
#1
@bot.event
async def on_ready():
    print(f'{bot.user.name} bot has connected to Discord!')
    

#3
@bot.command(name='rd', help='rolls dice <no.of dice> <no. of sides>')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


#reposter
@bot.command(name='repeat', help='repeats what you say')
@commands.has_role('Server Staff')
async def post(ctx,*args):
    #await ctx.send(*args)
    await ctx.send('{}'.format(' '.join(args)))

#rules:
#@bot.command(name='rule', help='A reminder of rule !')
#async def post(ctx):
#    await ctx.send('r')

@bot.command(name='selfpromo', help='A reminder of rule 1')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('Self advertisement/promotion is **only** permitted within <#892821290065477632> ')

@bot.command(name='spam', help='A reminder of rule 2')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('**No** spam in any form including messages, images, gifx, emotes and stickers.')

@bot.command(name='topics', help='A reminder of rule 3')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('**No** discussion of politics or religion and **no** misogyny, sexism, racism, homophobia, transphobia or hate speech')

@bot.command(name='nsfw', help='A reminder of rule 4')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('**No** NSFW content including messages, images, gifs, names or profiles')

@bot.command(name='triggers', help='A reminder of rule 5')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('**No** discussion of disturbing/triggering content, if you have to ask its probably not okay')

@bot.command(name='respect', help='A reminder of rule 6')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('''**Please be respectful of others, both in and out of VCs***
    Especially the mods! Keep in mind any "bot" seen talking in chat are actually a person - more info about that at the end of <#956164492675383326> ''')

@bot.command(name='roleplay', help='A reminder of rule 7')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('''**No roleplaying/impersonation**
(DID/OSDD alters based on IRL sources are not included in this)''')

@bot.command(name='threats', help='A reminder of rule 8')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('''**No attempts/threats of Doxxing, DDosing, IP grabbing or other similar activities**
Please be aware of the information you share and do not share others information without consent''')

@bot.command(name='friendj', help='A reminder of rule 9')
@commands.has_role('Server Staff')
async def post(ctx):
    await ctx.send('''**Please do not attempt to friend/DM J without asking and remember she is under no obligation to give that permission**
If you wish to interact with her just be active in the server! She's usually lurking''')




#info
@bot.command(name='J', help='About J!', aliases=['aboutj', 'aboutJ', 'j'])
async def post(ctx):
    await ctx.send('''J is a 19 year old British streamer who's obsessed with purple, screams constantly and always has a song in her head.
She mainly streams Minecraft but will mix things up if the discord demands <:aceofyum:1011326188737794138>
Her DMs are closed but she's almost always on the server, say her name and she's likely to appear! she loves to chat with you guys <:aceoflove:1011326211336712254>''')

@bot.command(name='about', help='tells you information about the bot, and credits!', aliases=['hello', 'abt', 'bot', 'toshi', 'Toshi'])
async def post(ctx):
    message = await ctx.send('''Hello! I am Toshi, a personalised bot made for this server, and developed by SkylaEris#7625. If you have any questions about me, you can do the ?help command in any channel to show the commands list, or ping Skyla with your question!''')
    await message.edit(content = '''Hello! I am Toshi, a personalised bot made for this server, and developed by <@633743097586647054>. If you have any question about me, you can do the ?help command in any channel to show the commands list, or ping Skyla with your question!''')


@bot.command(name='streams', help='Show AceOfJ\'s stream schedule', aliases=['schedule'])
async def schedule(ctx):
    await ctx.send(file=discord.File('streams.png'))
    await ctx.send('''Stream schedule is posted on twitter at https://twitter.com/AceOfJJ and in <#972511823381295205> at the start of every week!''')#add to other abt J posts!

# @bot.command(name='aseron', help='Displays information about Project Aseron')
# async def epic(ctx):
#     await ctx.send('''Project Aseron is a build project I have been working on for a long while, essentially I'm making a minecraft map that my views get to influence! 
# It's fantasy inspired and we started by creating a mushroom castle, which had evolved into a whole kingdom! We also have lore, written by myself. It will be expanded # as I build more. 
# Currently my mods and twitch subs can be added to the world's lore, but feel free to head cannon what you would do in this world!''')

######################################################################################################################################################################################################

@bot.command(name='smp', help='Tells you to the SMPs that AceOfJ is on, and some info about them', aliases=['smps', 'SMPs']) 
async def SMP(ctx):  
    await ctx.send('''Mythrill SMP - a lore SMP with custom items and textures inspired by hermitcraft and Empires SMP, which J co-owns! Remember to Join the discord and follow the twitter! https://twitter.com/MythrillSMP https://discord.gg/WNENbvqxWR
PrideCraft SMP - A Hermitcraft inspired SMP, creating a safe space for LGBTQIA+ community, Owned by IzzyFoxy https://twitter.com/PrideCraftSMP
Resonance SMP - A fantasy lore SMP in the heart of Absentan, with unique species and origins. Owned by TheStoryPainter https://twitter.com/ResonanceSMP''')

@bot.command(name='mythrillsmp', help='Sends information about the mythrill SMP and a link to the twitter page', aliases=['msmp', 'MSMP', 'mythrill', 'mythrillSMP'])
async def post(ctx):
    await ctx.send('''The Mythrill SMP is a lore SMP with custom items and textures inspired by hermitcraft and Empires SMP, which J co own's.
Remember to folow the twitter and join the discord! https://twitter.com/MythrillSMP https://discord.gg/WNENbvqxWR ''')


#@bot.command(name='eelsmp', help='Info about the Eel SMP')
#async def post(ctx):
#    await ctx.send('Sorry, but if you need help with the Eel SMP you should ask the mods in the Big Boys Discord server and not the Ace Of J discord as it is not her SMP. Here is a link to the Big Boys server; https://discord.com/invite/CRmk7JepZD')

#@bot.command(name='texture', help='info about J\'s texture pack')
#async def post(ctx):
#    await ctx.send('My lovely texture pack made by Miyyist; https://miyyist.com/#download')

@bot.command(name='welcome', help='Welcome a user to the server, and direct them to some useful channels!')
async def post(ctx):
    await ctx.send('Welcome to the server! please remember to get some <#873959044543549560> , don\'t forget to read <#956164492675383326> and the <#819938150025527308>, feel free to introduce yourself in <#897801023073173515>, and I hope you enjoy it here!')

@bot.command(name='levels', help='Find out information about the server\'s levelling system and rewards, and get a link ti the leaderboard')
async def epic(ctx):
    await ctx.send('''Gain levels by talking in chat! (don\'t spam) With levels you get special rewards;
level 5 - change nickname & use external emojis  ❤️ 
level 15  - gives access to give aways 🧡 
level 30  - able to post gifs in all chats 💛
level 50  - use external stickers 💚 
level 60 - get a custom role 💙 
level 100  - get the Starfire role (OG role) 💜 

For any rewards above 60 please contact a mod
Leader board; https://arcane.bot/lb/AceOfJ''')

@bot.command(name='pk', help='directs ppl to the pk explanation')
async def post(ctx):
    await ctx.send('''Pluralkit is a bot that allows server member who are apart of systems (DID/OSDD) to better identify themselves. This is why bots will sometimes appear in chat, there actually are server members using the bot! So please be respectful.
If you are apart of a system you may request the @systems role from or mod or by opening a 
support-ticket 
For more information on systems check out; https://did-research.org/, and https://systemsupport.carrd.co/ 
(This information can also be found in <#956164492675383326>)''')

@bot.command(name='spoiler', help='explains how to hide text by marking it as a spoiler')
async def post(ctx):
    await ctx.send('Put \|| on either side of the text you want to spoiler, like this: \||text\|| so it looks like this: ||text||')

@bot.command(name='notabot', help='for when a system member gets called a bot')
@commands.has_role('systems')
async def post(ctx, user = ''):
    #print(user)
    if user != '':
        #print(user)
        try:
            user = int(user)
            #print(user)
            user=' <@'+user+'>'
        except:
            user = user
        if user == "@everyone":
            user = "everyone"
    await ctx.send('Hello '+user+'! I see that you are calling me a bot, but in actuality I am part of a DID system, and I am not the only server member who is part of one. Systems can be formed from mental health disorders such as DID and OSDD, and other causes as well. I use Pluralkit to express myself easier, along with everyone else who is part of a DID/OSDD system! I would appreciate if you would not call me a bot, and call me by my name. If you wish to know more about DID/OSDD then visit one of these links! https://did-research.org/ https://systemsupport.carrd.co/')

@bot.command(name='notabot2', help='for when a system member gets called a bot')
#@commands.has_role('Server Staff')
async def post(ctx, user = ''):
    if user != '':
        #print(user)
        try:
            user = int(user)
            #print(user)
            user=' <@'+user+'>'
        except:
            user = user
        if user == "@everyone":
            user = "everyone"
    await ctx.send('Hello'+user+'! I see that you are calling this person a bot, but in actuality, they are part of a system, and are not the only server member who is part of one. Systems can be formed from mental health disorders such as DID and OSDD, and other causes as well. They use Pluralkit to express themself easier, along with many others who are part of a system! It would be appreciated if you would not call our members bots, and call them by their names. If you wish to know more about DID/OSDD then visit one of these links! https://did-research.org/ https://systemsupport.carrd.co/')

@bot.command(name='ender', help='translate to and from ender') #aww yissssss :D
async def post(ctx, *args):
    EndAlphabet= ['⏃','⏚','☊','⎅','⟒','⎎','☌','⊑','⟟','⟊','☍','⌰','⋔','⋏','⍜','⌿','☌','⍀','⌇','⏁','⎍','⎐','⍙','⌖','⊬','⋉']
    EnAlpha =    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plaintext = ''
    message = ''
    end = False
    for word in args:
        plaintext= plaintext+' '+word

    for letter in plaintext:
        if letter in EndAlphabet:
            end = True

    if end == True:
        for letter in plaintext:
            if letter in EndAlphabet:
                message = message + EnAlpha[EndAlphabet.index(letter)]
            else:
                message = message + letter
    else:
        for letter in plaintext:
            if letter in EnAlpha:
                message = message + EndAlphabet[EnAlpha.index(letter)]
            else:
                message = message + letter
            
    print(message)

    await ctx.send(f'<@{ctx.author.id}> says: '+message)

#@bot.command(name='mentalhealth', help='give mental health support, and give a link to helplines')
#async def post(ctx):
#    await ctx.send('If you are struggling, we hope that you will feel better soon, because we are not trained professionals and aren\'t able to help you here are the phone numbers/text lines for around the world. hopefully this helps:https://www.helpguide.org/find-help.htm')

@bot.command(name='mentalhealth', help='give mental health support, and give a link to helplines')
async def post(ctx):
    await ctx.send('If you are struggling, we hope that you will feel better soon, but its important to remember that we are not trained professionals and aren\'t able to help you in the way that we need you need. Please remember that we have the ?helplines command if you need it. ')

@bot.command(name='helplines', help='gives a link to helplines')
async def post(ctx):
    await ctx.send('''help you here are the phone numbers/text lines for around the world. hopefully this helps:
    https://www.helpguide.org/find-help.htm''')



#quick links
@bot.command(name='socials', help='Send J\'s socials link')
async def post(ctx):
    await ctx.send('All J\'s socials can be found here! Check them out!  https://solo.to/aceofj')

@bot.command(name='twitch', help='Sends a quick link to J\'s twitch page', aliases=['tw'])
async def post(ctx):
    await ctx.send('https://www.twitch.tv/aceofjj')

@bot.command(name='tiktok', help='Sends a quick link to J\'s Tiktok page', aliases=['tt', 'toktik', 'tiktiktoktok'])
async def post(ctx):
    await ctx.send('https://www.tiktok.com/@aceofjj')

@bot.command(name='twitter', help='Sends a quick link to J\'s Twitter page', aliases=['twt'])
async def post(ctx):
    await ctx.send('https://twitter.com/AceOfJJ')

@bot.command(name='youtube', help='Sends a quick link to J\'s YouTube channel', aliases=['yt'])
async def post(ctx):
    await ctx.send('https://www.youtube.com/channel/UCqgQ7kxE0vwC6xxffvWEZxA')

@bot.command(name='vods', help='Sends a quick link to J\'s vods YouTube channel', aliases=['vod', 'vodsyt'])
async def post(ctx):
    await ctx.send('https://www.youtube.com/channel/UCRYK64u2DXqNxugoBIq3w7A')

@bot.command(name='insta', help='Sends a quick link to J\'s Instagram page', aliases=['instagram', 'ig'])
async def post(ctx):
    await ctx.send('https://www.instagram.com/p/CVYmDIoLM9d/')

@bot.command(name='donate', help='Sends a quick link to J\'s donation page')
async def post(ctx):
    await ctx.send('Support J without giving anything to Jeff Bezos! https://streamelements.com/aceofjj/tip')

@bot.command(name='merch', help='Sends a quick link to J\'s merch shop!')
async def post(ctx):
    await ctx.send('''J\'s MERCH STORE!! (remember twitch subs get a discount! code in <#954066033403121684>)
    https://aceofj-shop.fourthwall.com/''')

@bot.command(name='pop', help='Get 10% discount on your Paws of Pride order!', aliases=['pawsofpride', 'PawsOfPride'])
async def post(ctx):
    await ctx.send('''Get 10% discount on your Paws of Pride order! www.pawsofpride.com/aceofjj''')

@bot.command(name='leaderboard', help='Sends a quick link to the server\'s levels leaderboard.', aliases=['lb'])
async def post(ctx):
    await ctx.send('https://arcane.bot/lb/AceOfJ')


#fun
@bot.command(name='lurk', help='just for fun lol, may be useful, who knows')
async def post(ctx):
    await ctx.send(f'<@{ctx.author.id}> is now lurking in the shadows!')

@bot.command(name='unlurk', help='unlurk...self explanatory')
async def post(ctx):
    await ctx.send(f'<@{ctx.author.id}> has emerged from the shadows!')

@bot.command(name='compliment', help='tell someone they\'re amazing :)', aliases=['<3','\<3', '<3its', 'complement'])
async def post(ctx, *args): #user=''):
    #print (args)
    user = ''
    for word in args:
        user= user+' '+word

    if user != '':
        isID = True
        #print(user)
        for character in user:
            if character != ' ':
                try:
                    character = int(character)
                except:
                    isID = False
            
    if isID:
        user = user[1:]
        user=' <@'+user+'>'
        #print(user)
    else:
        #print('except')
        user = user
    if user == "@everyone":
        user = "everyone"
    print('here')
    wordList = ("amazing", "amazing", "awesome", "a legend", "really cool", "wonderful", "adorable")
    word = random.choice(wordList)
    await ctx.send(user+' you\'re '+word)

@bot.command(name='hug', help='Hug someone!', aliases = ['Hug', 'hug!'])
async def post(ctx, *args): #user=''):
    user = ''
    for word in args:
        user= user+' '+word
    if user != '':
        isID = True
        #print(user)
        for character in user:
            if character != ' ':
                try:
                    character = int(character)
                except:
                    isID = False 
    if isID:
        user = user[1:]
        user=' <@'+user+'>'
    else:
        user = user
    if user == "@everyone":
        user = "everyone"
    await ctx.send(f'<@{ctx.author.id}> gave '+user+' a hug! <:aceoflove:1011326211336712254>')
    #await ctx.send(str(ctx.message.author)+' gave '+user+' a hug! <:aceoflove:1011326211336712254>')

@bot.command(name='jhug', help='Get a hug from J!', aliases=["Jhug"])
async def post(ctx):
    await ctx.send(f'J uses magic to send you, <@{ctx.author.id}> , support! She wraps you in her starry cape, because you are a shining star, and pulls you into a warm hug. Always remember; you are loved. Not only by me but by so many others. You are deserving, you are special, you are loved. Never forget that - Ace Of J <:aceoflove:1011326211336712254>')


@bot.command(name='roles', help='tell someone to get reaction roles', aliases = ['getroles'])
async def post(ctx, *args): #user=''):
    user = ''
    for word in args:
        user= user+' '+word
    if user != '':
        isID = True
        #print(user)
        for character in user:
            if character != ' ':
                try:
                    character = int(character)
                except:
                    isID = False 
    if isID:
        user = user[1:]
        user=' <@'+user+'>'
    else:
        user = user
    if user == "@everyone":
        user = "everyone"
    await ctx.send('''Hi'''+user+''', please get some roles from <#873959044543549560>
Thank you!''')

@bot.command(name='proud', help='tell someone we\'re proud of them :)')
async def post(ctx, *args): #user=''):
    user = ''
    print(args)
    for word in args:
        print(word, user)
        if word != 'of':
            user= user+' '+word
            continue
    print(user)
    if user != '':
        isID = True
        #print(user)
        for character in user:
            if character != ' ':
                try:
                    character = int(character)
                except:
                    isID = False 
    if isID:
        user = user[1:]
        user=' <@'+user+'>'
    else:
        user = user
    if user == "@everyone":
        user = "everyone"
    await ctx.send(user+', we\'re proud of you!')

@bot.command(name='no', help=' no u', aliases=['no u'])
async def post(ctx, args):
    #print(args)
    check = False
    check=re.search('(yo)?u+',args[0])
    print(check)
    if check:
        await ctx.send('no u :)')
    else:
        await ctx.send('no what?')

@bot.command(name='pridesquid', help='pridesquid yayyyy', aliases=['pride'])
async def post(ctx):
    #so = bot.get_emoji(998236964136439918)
    #await ctx.send(f'{so}<:squid2:998916686503759932> <:squid3:998916686503759932><:squid2:998916686503759932><:squid4:998916686503759932><:aceofintersex::aceoface::aceofbi::aceofgay::aceoftrands::aceofpan::aceofnb::aceoffluid::aceoflesbian:')
    await ctx.send('<:squid1:998236964136439918><:squid2:998236966413926440><:squid3:998236968301379614><:squid2:998236966413926440><:squid4:998236970104913992><:aceofintersex:998636217983844403><:aceoface:998636188816654476><:aceofbi:998636204465606787><:aceofgay:998636214850687066><:aceoftrans:998636231317524581><:aceofpan:998636228066955284><:aceofenby:998636207653265559><:aceoffluid:998636211067441225><:aceoflesbian:998636221662244916>')

@bot.command(name='petj',help= 'Pet J :)', aliases=['aceofpets'])
async def tree(ctx):
    await ctx.send(file=discord.File('aceofpets.gif'))

@bot.command(name='pettoshi',help= 'Pet Toshi :)', aliases=['pet', 'petoshi'])
async def tree(ctx):
    await ctx.send(file=discord.File('toshipets.gif'))

#@bot.command(name='buff',help= '*GIGACHAD TOSHI*', aliases=['chad'])                         #, 'w-what?', 'w-what'])
#async def tree(ctx):
#    await ctx.send(file=discord.File('Buff.png'))

@bot.command(name='contest',help= 'See the amazing art from the Toshi art contest! (doesn\'t ping)', aliases=['winner'])
async def tree(ctx):
    message = await ctx.send("This is the amazing art from Avadawn that won the contest!")
    await ctx.send(file=discord.File('contest.png'))
    await message.edit(content="This is the amazing art from <@572087771267727360> that won the contest!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Only server staff can use this command.')


bot.run(TOKEN)

