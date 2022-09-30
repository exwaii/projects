import openai
import os
import discord
from load_dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

discord_token = os.environ.get("DISCORD_TOKEN")
openai_key = os.environ.get("OPENAI_KEY")
headers = {
    "Authorization": openai_key
}
openai.api_key = openai_key
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

prompt = "The following is a conversation with a super-intelligent friend. The friend is very smart and witty"

users = [os.environ.get("XY"), os.environ.get("MEGULOLI"), os.environ.get("CAASI"), os.environ.get("TOOTHLESS")]
conversations = {}


@bot.event
async def on_ready():
    global user_xy, user_meguloli
    print('we have on as {0.user}'.format(bot))
    users = [bot.get_user(id) for id in users]
    conversations = {user.name : prompt + "\n" for user in users}

    # channel = await bot.fetch_channel(926793922762645514)
    # message = await channel.fetch_message(926806836068376597)
    # await message.delete()
    # HOW TO SAVE AWAIT RESULTS, HOW TO DELETE MESSAGE LFGGGG


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author in users and message.guild is None:
        talking_user = message.author
        if message.content == "!clear":
            print(conversations[talking_user.name])
            with open("convos.txt", "a", encoding="utf-8") as file:
                file.write(talking_user.name + "\n")
                file.write(conversations[talking_user.name])
                file.write("\n\n")
            conversations[talking_user.name] = prompt + "\n"
            return
        if len(conversations[talking_user.name]) > (1600 * 4):
            await talking_user.send("please !clear the conversation has been too long if u wanna continue i can try "
                                    "to extract out parts from it")
            return
        conversations[talking_user.name] += "Human: "
        conversations[talking_user.name] += message.content.replace("<@!926668880053674015>", "you") + "\nGPT3:"
        print(message.content)
        # replaces any @s with you
        response = openai.Completion.create(
            engine="davinci",
            prompt=conversations[talking_user.name],
            temperature=0.9,
            max_tokens=400,
            stop=["\n", "Human:", "GPT3:"],
            presence_penalty=2.0,
            frequency_penalty=2.0,
        )
        ai_msg = response['choices'][0]['text']
        #ai_msg = "h"
        conversations[talking_user.name] += ai_msg + "\n"
        await talking_user.send(ai_msg)
        print(ai_msg[1:])


bot.run(discord_token)
