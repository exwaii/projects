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

# AI = "The following is a conversation with an AI assistant. The assistant is very cheerful and smart."
AI = "The following is a conversation with a super-intelligent friend. The friend is very smart and witty"
# AI = "The following is a conversation between a teenage boy and his seductive girlfriend. His girlfriend is very attractive."
# print(f"GPT3: {response['choices'][0]['text']}")
# convo += response["choices"][0]["text"]
# human_response = input("Human: ")
# if human_response == "exit":
#     break
# convo += "\nHuman:"
# convo += human_response
# convo += "\nGPT3:"
# with open("convos.txt", "a", encoding="utf-8") as file:
#     file.write(convo)
#     file.write("\n\n")
users = []
conversations = {}


@bot.event
async def on_ready():
    global user_xy, user_meguloli
    print('we have on as {0.user}'.format(bot))
    user_meguloli = bot.get_user(669524792306565141)
    user_xy = bot.get_user(358971085313540097)
    user_isaac = bot.get_user(394318698116022302)
    user_zhong = bot.get_user(454221326471659520)
    users.append(user_xy)
    users.append(user_meguloli)
    users.append(user_isaac)
    users.append(user_zhong)
    for user in users:
        conversations[user.name] = AI + "\n"
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
            conversations[talking_user.name] = AI + "\n"
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
        conversations[talking_user.name] += ai_msg + "\n"
        await talking_user.send(ai_msg)
        print(ai_msg[1:])


bot.run(discord_token)
