# Simple and configurable AI chatbot for Discord

This bot is made using the discord.py library and utilizes Google's generative AI for the responses.

## Setup:
### Discord Bot:
#### Make an application at: https://discord.com/developers/applications, you can follow this guide: https://discordpy.readthedocs.io/en/stable/discord.html

#### Make sure the bot has access to message content.

### API Key:
#### go to https://console.cloud.google.com and create a project, then go to https://aistudio.google.com/app/apikey and make an API key

## Libraries:
#### you will need to install a couple libraries to be able to use this bot
### discord.py
> pip install -U discord.py
#### python-dotenv:
> pip install python-dotenv
#### Gemini API:
> pip install -U google-generativeai
#### Colorama:
> pip install colorama

## Config:
#### open .env and paste your discord bot token and google API key in it's respective spots (MAKE SURE THEY'RE IN QUOTES!!)
#### open config.yml and insert the channel-id of the channel you want the bot to send it's logs in and insert the channel-id of the chat channel
#### setup the config as you like although I recommend you keep the included instructions for safety reasons.
#### put any information you want the bot to know at the bottom of the config.yml, replacing "PUT INFORMATION HERE"

## Usage:
#### the bot will reply to any message sent in the "chat" channel, assuming you have it setup correctly.
#### I recommend you stick with the Gemini-1.5-flash because the free version is good enough for what it is and won't get rate limited from normal usage

## Extra:
#### please let me know if you encounter any issues or open a pull request if you would like to add something
#### you can contact me on my discord: WayTooIcyy
