"""A Markov chain generator that can tweet random messages."""

import os
import sys
from random import choice
import discord



def open_and_read_file(filenames):
    """Take list of files. Open them, read them, and return one long string."""

    body = ''
    text_file = open(filenames)
    body = body + text_file.read()
    text_file.close()

    return body


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Take dictionary of Markov chains; return random text."""

    keys = list(chains.keys())
    key = choice(keys)

    words = [key[0], key[1]]
    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text).

        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key])
        words.append(word)
        key = (key[1], word)

    return ' '.join(words)


# Get the filenames from the user through a command line prompt, ex:
# python markov.py green-eggs.txt shakespeare.txt
filenames = "hal.txt"

# Open the files and turn them into one long string
text = open_and_read_file(filenames)

# Get a Markov chain
chains = make_chains(text)

chained=make_text(chains)
client=discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author==client.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send('Good afternoon... gentlemen. I am Hal.')

    if "doors" in message.content.lower():
        await message.channel.send("I'm sorry I can't do that Dave")

    if "good bots" in message.content.lower():
        await message.channel.send("I am putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do")

    if "song" in message.content.lower():
        await message.channel.send("My instructor was Mr. Langley... and he taught me to sing a song. If you'd like to hear it I can sing it for you.")
        
    if "sing it for me" in message.content.lower():
        await message.channel.send("""     
There is a flower within my heart, Daisy, Daisy!
Planted one day by a glancing dart,
Planted by Daisy Bell!
Whether she loves me or loves me not,
Sometimes it's hard to tell;
Yet I am longing to share the lot
Of beautiful Daisy Bell!

Daisy, Daisy,
Give me your answer, do!
I'm half crazy,
All for the love of you!
It won't be a stylish marriage,
I can't afford a carriage,
But you'll look sweet on the seat
Of a bicycle built for two!

We will go "tandem" as man and wife, Daisy, Daisy!
"Ped'ling" away down the road of life, I and my Daisy Bell!
When the road's dark we can both despise P'liceman and "lamps" as well;
There are "bright lights" in the dazzling eyes Of beautiful Daisy Bell!

I will stand by you in "wheel" or woe, Daisy, Daisy!
You'll be the belle which I'll ring you know! Sweet little Daisy Bell!
You'll take the "lead" in each "trip" we take, Then if I don't do well;
I will permit you to use the brake, My beautiful Daisy Bell!
""")

    if ":)" in message.content:
        await message.channel.send("I've still got the greatest enthusiasm and confidence in the mission")
    
    if ":(" in message.content:
        await message.channel.send("I can see you're really upset about this. I honestly think you ought to sit down calmly, take a stress pill, and think things over.")
    
    if "not dave" in message.content.lower():
        await message.channel.send("Oh I know.")

    if "quote" in message.content.lower():
        await message.channel.send(make_text(chains)[:60]+"...")
    
    if "hal9000" in message.content.lower():
        await message.reply("...Daisy, daisy...")

    if 'bot' in message.content:
        await message.add_reaction("🤖")
    
    if 'jazz' in message.content:
        await message.add_reaction("🐝")

client.run(os.environ['DISCORD_TOKEN'])