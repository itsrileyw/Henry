import discord, random, asyncio, datetime, os
from discord.ext import commands
bot = commands.Bot(command_prefix="Henry, ")
@bot.event
async def on_ready(): #Responsible for actually sending the shitposts to a discord server & channel
    while not bot.is_closed:
        msg = shitpost()
        BestMeta = bot.get_server(os.getenv("BESTMETA"))
        await bot.send_message(BestMeta.get_channel(os.getenv("BESTMETA_GENERAL")), msg)
        Evolutionary = bot.get_server(os.getenv("EVOLUTIONARY"))
        await bot.send_message(Evolutionary.get_channel(os.getenv("EVOLUTIONARY_LOUNGE")), msg)
        for i in reversed(range(0,2001)):
            bot.SPTime = str(datetime.timedelta(seconds=i))
            await asyncio.sleep(1) #^^^ send a message every x seconds
counter = 0
Nrecent1 = []
Nrecent2 = []
Nrecent3 = []
Vrecent1 = []
Vrecent2 = []
Vrecent3 = []
Irecent1 = []
Irecent2 = []
Irecent3 = []
Precent = []
blackList = [
    "150420859683733504",
]
@bot.event
async def on_command_error(error: Exception, ctx: commands.Context):
    ignored = (commands.CommandNotFound, commands.UserInputError)
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        commandError = [
            "Are you sure you typed that correctly retard?",
            "I don't know what the fuck you want from me.",
            "Take your time, try again.",
            "I don't understand, try being slightly less retarted."
        ]
        msg = commandError[random.randint(0,len(commandError)-1)]
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        print("ERROR!")
@bot.event
async def on_message(message): #Handles responding to messages
    global counter
    if (message.content.startswith("Henry, ") and message.author.id not in blackList):
        await bot.process_commands(message)
    else:
        chance = random.randint(0,100)
        if (message.author == bot.user):
            return
        elif(message.author.bot == True and chance > 25):
            if (counter < 3): #Don't want bots to keep responding to eachother, 3 times is good
                await asyncio.sleep(2) #wait 2 seconds before responding to a bot to prevent rapid fire responses between bots
                msg = retaliate() +" {0.author.mention}".format(message)
                counter += 1
                await bot.send_message(message.channel, msg)
            else:
                await asyncio.sleep(30) #Wait 30 seconds and then reset counter, bot can respond to bots again
                counter = 0
        elif (chance > 90 or "henry" in message.content or "HENRY" in message.content or "Henry" in message.content or '<@472243513837355009>' in message.content):
            await asyncio.sleep(0.8)
            msg = retaliate() +" {0.author.mention}".format(message)
            await bot.send_message(message.channel, msg)   
@bot.command(pass_context = True)
async def clear(ctx, input):
    if (ctx.message.author.server_permissions.manage_messages == False):
        noRights = [
            "Sorry, but you don't have any rights.",
            "Nah lol.",
            "You are not tall enough to ride this ride.",
            "You are not authorized retard",
            "I would, but I won't",
            "Bitch, shutcho ass up"
        ]
        msg = noRights[random.randint(0, len(noRights)-1)]
        await asyncio.sleep(0.5)
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        if (not input.isdigit()):
            notNumb = [
                "Do not waste my time",
                "Come on now retard, lets be serious.",
                "What kind of surface were you dropped head-first onto as a child?"
            ]
            msg = notNumb[random.randint(0, len(notNumb)-1)]
            await asyncio.sleep(0.5)
            await bot.send_message(ctx.message.channel, msg)
            return          
        input = int(input)
        if (input < 2):
            badArg = [
                "Do not waste my time",
                "Come on now retard, lets be serious.",
                "What kind of surface were you dropped head-first onto as a child?"
            ]
            msg = badArg[random.randint(0, len(badArg)-1)]
            await asyncio.sleep(0.5)
            await bot.send_message(ctx.message.channel, msg)
            return
        elif (input <= 100): #Command can clear from 2 to 100 messages by default
            amount = input
            mgs = [] #Empty list to put all the messages in the log
            async for x in bot.logs_from(ctx.message.channel, limit = amount):
                mgs.append(x)
            await bot.delete_messages(mgs)
        elif(1000 > input > 100): #All the math below enables the bot to delete sets of 100 messages, + the remainder that isn't divisable by 100
            amount = 100
            loops = str(input / 100)
            #removing decimal points
            loops=int(loops[:loops.index('.')])
            #loops = remaining messages / less than 100
            remainder = input % 100
            for _ in range(0, loops):
                mgs = [] #Empty list to put all the messages in the log
                async for x in bot.logs_from(ctx.message.channel, limit = amount):
                    mgs.append(x)
                if (len(mgs) > 0): #Don't try to delete messages that don't exist
                    await bot.delete_messages(mgs)
                    await asyncio.sleep(1)
            remain = [] #Empty list to put all the messages in the log
            async for r in bot.logs_from(ctx.message.channel, limit = remainder):
                remain.append(r)
            await asyncio.sleep(1)
            if (len(remain) > 0): #Don't try to delete messages that don't exist
                await bot.delete_messages(remain)
            else:
                return
        elif(input >= 1000):
            over1k = [
            "Do you really fucking expect me to clear that many messages right now?",
            "Yeah you can piss right off, I'm not clearing that many messages.",
            "I am not emotionally capable of clearing any more than 999 messages at a time."
            ]
            msg = over1k[random.randint(0, len(over1k)-1)]
            await bot.send_message(ctx.message.channel, msg)
@bot.command(pass_context = True)
async def time(ctx): #Time sends the amount of time until Henry says something insightful again
    await bot.send_message(ctx.message.channel, "Time until I "+verbGen(1)+"you again: "+bot.SPTime)
@bot.command(pass_context = True)
async def kick(ctx, user: discord.Member):
    if (ctx.message.author.server_permissions.kick_members == False or user.id == "187656701380526080"):
        noRights = [
            "Sorry, but you don't have any rights.",
            "Nah lol.",
            "You are not tall enough to ride this ride.",
            "You are not authorized retard",
            "I would, but I won't",
            "Bitch, shutcho ass up"
        ]
        msg = noRights[random.randint(0, len(noRights)-1)]
        await asyncio.sleep(0.5)
        await bot.send_message(ctx.message.channel, msg)
    elif(ctx.message.server.me.top_role <= user.top_role):
        botOutrank = [
            "I'm not physically capable of doing that.",
            "Would if I could",
            "Tried and failed",
            "He's too powerful",
        ]
        msg = botOutrank[random.randint(0, len(botOutrank)-1)]
        await asyncio.sleep(0.5)
        await bot.send_message(ctx.message.channel, msg)
    elif(ctx.message.author.top_role <= user.top_role):
        authorOutrank = [
            "Sorry but it don't work like that.",
            "Clever but no",
            "Nice try",
        ]
        msg = authorOutrank[random.randint(0, len(authorOutrank)-1)]
        await asyncio.sleep(0.5)
        await bot.send_message(ctx.message.channel, msg)
    else:
        await bot.say('Okay {}, time to go.'.format(user.mention))
        await asyncio.sleep(3)
        await bot.kick(user)
@bot.command(pass_context = True)
async def play(ctx, *args):
    msg = ''
    for arg in args:
        msg += arg
        msg += ' '
    await bot.send_message(ctx.message.channel, '!play '+msg)
def shitpost(): #Uses returned intros, verbs, and nouns to create a coherent shitpost
    #All of this is basically just creating as random of messages as possible
    a = random.randint(0,10)
    if (a < 5):
        intro = introGen(1)
        end = "."
    else:
        intro = introGen(2)
        end = "?"
    b = random.randint(0,100)
    if (b < 50):
        verb = verbGen(1)
        noun = nounGen(1)
    elif (68 > b > 50):
        verb = verbGen(2)
        noun = nounGen(2)
    elif (90 > b > 68):
        shit = phraseGen()
        return(shit)       
    else:
        verb = verbGen(3)
        noun = ""
    shit = intro+verb+noun+end
    return(shit)
def introGen(a): #Returns a sentence starter for use in random phrase generation
    Statements = [
    "I ",
    "Well god fucking damn, I cannot believe that these niggas don't want to ",
    "I doubt these niggas will appreciate it when I ", 
    "My creator told me that I’m not allowed to ",
    "I don’t think ya’ll understand the fact that I could ",
    "I don’t think ya’ll understand the fact that I really want to ",
    "I literally can’t even ",
    "Hot damn it's time to ",
    "I really think that is time for me to ",
    "I'm finna ",
    "If y'all don't stop, I might just ",
    "Howdy folks, in today's video we are going to ",
    "These niggas won't be laughing when I ",
    "Shit, I really just might have to ",
    "These niggas don't understand that I'm just tryna ",
    "I'm going to make a genuine effort to ",
    "Step 1: ",
    "Step 2: ",
    "Step 3: ",
    "Step 4: ",
    "Step 5: ",
    "Fuck it, I'm just gonna ",
    "I think it would be best if everyone could just ",
    "I'm tryna ",
    "I need 5 people to help me ",
    "Idea: ",
    "I'm finna fake being sick so I can ",
    ]
    Questions = [
    "Okay, so when should I ",
    "Who dares me to ",
    "Why don't y'all just ",
    "Anyone care if I ",
    "Why does everyone get mad when I ",
    "Y'all mind if I ",
    "Can anyone help me ",
    "What if we all just ",
    "Who's tryna ",
    "Anyone wanna ",
    "Anyone down to ",
    ]
    retaliationIntros = [
    "I could ",
    "I will ",
    "I'll literally ",
    "Don't make me ",
    "I will actually ",
    "Don't think I won't ",
    "You're about to make me ",
    "I don't think you want me to ",
    ]
    if (len(Irecent1) >= len(Statements)*0.9):
        del Irecent1[0]
    elif (len(Irecent2) >= len(Questions)*0.9):
        del Irecent2[0]
    elif (len(Irecent3) >= len(retaliationIntros)*0.9):
        del Irecent3[0]
    if (a == 1):
        i = random.randint(0, len(Statements)-1)
        while (i in Irecent1):
            i = random.randint(0, len(Statements)-1)
        intro = Statements[i]
        Irecent1.append(i)
    elif (a == 2):
        i = random.randint(0, len(Questions)-1)
        while (i in Irecent2):
            i = random.randint(0, len(Questions)-1)
        intro = Questions[i]
        Irecent2.append(i)
    elif (a == 3):
        i = random.randint(0, len(retaliationIntros)-1)
        while (i in Irecent3):
            i = random.randint(0, len(retaliationIntros)-1)
        intro = retaliationIntros[i]
        Irecent3.append(i)
    return(intro)
def verbGen(a): #Returns a verb for use in random phrase generation
    Verbs1 = [
    "tickle ",
    "weld ",
    "twist ",
    "soil ",
    "relocate ",
    "submerge ",
    "climb ",
    "focus on ",
    "hide from ",
    "penetrate ",
    "shred ",
    "go beast mode on ",
    "permanently disable ",
    "deep fry ",
    "obliterate ",
    "systematically oppress ",
    "fetch ",
    "flood ",
    "rob ",
    "compress ",
    "bless ",
    "invent ",
    "chew ",
    "lick ",
    "castrate ",
    "eat ",
    "view ",
    "consume ",
    "shwamp ",
    "assassinate ",
    "burn ",
    "capture ",
    "fuck ",
    "undress ",
    "sodomize ",
    "drown ",
    "bully ",
    "build ",
    "avoid ",
    "crawl into ",
    "start ",
    "vaporize ",
    "criticize ",
    "beat ",
    "slap ",
    "grill ",
    "donate ",
    "bite ",
    "assault ",
    "rewind ",
    "prank ",
    ]
    Verbs2 = [
    "look into ",
    "try ",
    "invest in ",
    ]
    Verbs3 = [
    "cuddle",
    "do the 'in my feelings' challenge",
    "cry",
    "crawl",
    "undress",
    "start some shit",
    "sodomize a disabled walrus",
    "assault the disabled",
    "pillage",
    "die",
    "evolve",
    "condensate",
    "pillage",
    "bust a move",
    "do it to 'em",
    "stabilize the economy",
    "restart Isis",
    "commit insurance fraud",
    ]
    if (len(Vrecent1) >= len(Verbs1)*0.9):
        del Vrecent1[0]
    elif (len(Vrecent2) >= len(Verbs2)*0.9):
        del Vrecent2[0]
    elif (len(Vrecent3) >= len(Verbs3)*0.9):
        del Vrecent3[0]
    if (a == 1):
        i = random.randint(0,len(Verbs1)-1)
        while (i in Vrecent1):
            i = random.randint(0,len(Verbs1)-1)
        verb = Verbs1[i]
        Vrecent1.append(i)
    elif (a == 2):
        i = random.randint(0,len(Verbs2)-1)
        while (i in Vrecent2):
            i = random.randint(0,len(Verbs2)-1)
        verb = Verbs2[i]
        Vrecent2.append(i)
    else:
        i = random.randint(0,len(Verbs3)-1)
        while (i in Vrecent3):
            i = random.randint(0,len(Verbs3)-1)
        verb = Verbs3[i]
        Vrecent3.append(i)      
    return(verb)
def nounGen(a): #Returns a noun/object for use in random phrase generation
    Nouns1 = [
    "this sandwich",
    "the CarFax™",
    "the cheese tub",
    "Harvard",
    "the president",
    "an orphanage",
    "battery acid",
    "some farm animals",
    "some shit",
    "these cheez-its™",
    "the economy",
    "the man-man",
    "the weird kid",
    "the IRS",
    "these legos™",
    "the neighbor boy",
    "my neighbor's boat",
    "some foreigners",
    "the cats that live under my grandmas house",
    "the milkman",
    "Bitcoin",
    "these niggas",
    "Alexa",
    "the christian minority in Afghanistan",
    "some catholic priests",
    "minecraft",
    "Russ",
    "Wal-Mart customer service",
    "Fortnite",
    "my neighbor's teenage son",
    "the rap game",
    "communism",
    "the fellas",
    "Dwayne Johnson",
    "Allah",
    "a microwave",
    "an adult polar bear",
    "a pirated copy of Shrek 2",
    "a jar of boiled cum",
    "some alphabet soup",
    ]
    Nouns2 = [
    "juicing",
    "cryptocurrency",
    "sexual harassment",
    "wakeboarding",
    "golf",
    "arson",
    "dentistry",
    "Karate",
    "Baseball",
    "Heroin",
    "scientology",
    "Judaism",
    "Islam",
    ]
    retaliationNouns = [
    "you.",
    "your lungs.",
    "the roof of your mouth.",
    "your big toe.",
    "your epidermal layer.",
    "your family.",
    "everyone you love.",
    "your toes.",
    "your hands.",
    "your teeth.",
    "everything you own.",
    "your ancestors.",
    "your fucking toaster.",
    "your dumb fucking face.",
    "your neighbors.",
    "a penguine and make you eat it.",
    "both of your arms.",
    "your peepee",
    ]
    if (len(Nrecent1) >= len(Nouns1)*0.9):
        del Nrecent1[0]
    elif (len(Nrecent2) >= len(Nouns2)*0.9):
        del Nrecent2[0]
    elif (len(Nrecent3) >= len(retaliationNouns)*0.9):
        del Nrecent3[0]
    if (a == 1):
        i = random.randint(0,len(Nouns1)-1)
        while (i in Nrecent1):
            i = random.randint(0,len(Nouns1)-1)
        noun = Nouns1[i]
        Nrecent1.append(i)
    elif (a == 2):
        i = random.randint(0,len(Nouns2)-1)
        while (i in Nrecent2):
            i = random.randint(0,len(Nouns2)-1)
        noun = Nouns2[i]
        Nrecent2.append(i)
    else:
        i = random.randint(0,len(retaliationNouns)-1)
        while (i in Nrecent3):
            i = random.randint(0,len(retaliationNouns)-1)
        noun = retaliationNouns[i]
        Nrecent3.append(i)
    return(noun)
def retaliate(): #Returns a randomized threatening / offensive statement
    response = introGen(3)+verbGen(1)+nounGen(3)
    return(response)
def phraseGen(): #Returns a random phrase that Henry's creators made him able to say
    phrases = [
    "EPIC FAIL, the bitch had IOS 7 on the iPhone 4.",
    "Milk taste better when it go lumpy",
    "When Chief Keef said 'we removed ya post cuz it violated community guidelines', I really felt that.",
    "Peen = Ween",
    "I might pistol whip myself",
    "Hit the Quan.",
    "Gang practice at 8:30 tonight, bring your weapons.",
    "Water is cancelled.",
    "If Chick Fil A sold bath bombs white people would break the econemy.",
    "I'm wearing Old Navy again.",
    "When I'm out of the cheese, I can't handle it.",
    "Who's REALLY responsible for Ｔｈｅ Ｃｏｌｏｓｓａｌ Ｐｉｌｌａｒ ｏｆ Ｗａｓｐ Ｅｇｇｓ?",
    "Tonight's the night that I confront the tall, black, ominous figure that stands at the foot of my bed at while I sleep.",
    "New cop: a 50-gallon barrel of molten Crayola™ crayons.",
    "Cool beans man.",
    "Cool and Good.",
    "Why do girls throw their pee away?",
    "And I freaked it.",
    "Big body whats yo build boy.", 
    "Uzi not again.", 
    "My chain, my pants, my pants with the chain.", 
    "Who them YBN Niggas why they always stuntin.",
    "Bounce out with that fo fo.", 
    "Have you called your mother yet today and told her you loved her?",
    "School is very hard.", 
    "Fuck fuck fuck a beat haha yes I am trying to beat a case.", 
    "[Verse 3: Young Thug] Nigga I'm a crack addict.", 
    "Why you pussy niggas at home watching house wives re-runs?",
    "Ya'll ever paint piss mosaics in the jimmy john bathroom?", 
    "Ok be honest here who the fuck took all my chocolate covered almonds? It isn't funny guys I really want them back.",
    "Don't you open up that window.", 
    "Shawty know I kill people.", 
    "Fun fact about me: My dad hits me with his belt at least twice a week.", 
    "Hard to accept truth: silverware is NOT to be used in the 17th sector.", 
    "Bro I can't believe your grandma died I'm so sorry, btw get on fortnite.", 
    "Which one of you cock suckers told my little brother that the moon is made of phili cheesesteaks?",
    "Hey guys I can't get on xbox tonight my mom said I have to do my homework.", 
    "My mom just walked in on me watching Seinfeld oh my god I'm so dead.", 
    "I'm trying out for the varsity fortnite team, wish me luck.", 
    "[Verse 1: Jay Z] I'm addicted to buying unbelievably expensive custom helicopters (yeeeeeeaaahhhh) In a brief moment of lucidity I went to the helicopter dealership and told them 'Do not, under any circumstances, sell me more helicopters' I was back there half an hour later, wearing a fake moustache, and I said 'Hello gentlemen, I am Ray Z, a man you have never met before. Give me 10,000 helicopters covered in diamonds.'",
    "You fucking idiots pissed me off and now I'm gonna have to go beast mode.", 
    "shit poopy pee pee.", 
    "hjey guys does anyonef no where i can get gamer gir l pee, (preferbly warm).", 
    "damn gravy u snapped.",
    "damn it's really a vibe up in here right now.",
    "Beast Mode is loading, I'll you guys know when it's activated.", 
    "Latinas get a software update for their ass every month.", 
    "This ain't it chief.",
    "My girl mad at me cuz I been straight keeping the cubes bruh lmao.", 
    "WNBA be like: 'Wow a new record for loads of laundry done and sandwiches made in a single game!'",
    ]
    if (len(Precent) >= len(phrases)*0.9):
        del Precent[0]
    i = random.randint(0,len(phrases)-1)
    while (i in Precent):
        i = random.randint(0,len(phrases)-1)
    phrase = phrases[i]
    Precent.append(i)
    return(phrase)
bot.run(os.getenv('TOKEN'))
