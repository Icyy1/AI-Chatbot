import os, yaml
import google.generativeai as genai
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("googleToken"))

with open('config.yml', 'r') as file:
  config = yaml.safe_load(file)

generation_config = {
  "temperature": float(config["AI"]["temperature"]),
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": int(config["AI"]["max_output_tokens"]),
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name=config["AI"]["model"],
  generation_config=generation_config,
  system_instruction=config["AI"]["system_instruction"],
)

chat_session = model.start_chat(
  history=[
  ]
)

class chatbot_cog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.client.user:
      return
    if message.content.startswith("//"):
      return 
    if message.channel.id == config["MAIN"]["chatChannel"]:
      msg = await message.reply("Please wait, I am processing your message...")
      try:
        response = chat_session.send_message(f"User's name: {message.author.name}, message: {message.content}")
        await msg.edit(content=response.text)
      except Exception as e:
        print(f"An API error occurred: {e}")
        await msg.edit(content="An error occurred while processing your message, please try again.")
            
async def setup(client):
  await client.add_cog(chatbot_cog(client))