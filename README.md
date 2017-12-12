# This is a primitive telegrams bot in Python, which on request /pynews the telegram sends a random post from the VK dedicated to the Python programming language

In the first place for this program to work, you need to get your own token VK(after Reading the documentation, you will easily be able to do it. https://vk.com/dev/manuals), but in the same token telegrams bot(you need to create your bot written in telegrams FatherBot)

Documentation for the library telebot - https://github.com/eternnoir/pyTelegramBotAPI

Components:
1. Parser
    This is the module that is using the library vk_api loads into database(format file .json), a list of 200 links to the posts from vk devoted to the Python programming language. Also the script takes the information from the Config module, which in turn contains two keys(api_key)

2. bot
   This script contains the bot. For work script needs to be injected PIP library telebot, as well as random. The script downloads the movie database, which is stored in file format .json on disk on request /pynews via cables sends one of the links on the post from the base.

3. Json
    It is a script that creates(if not) file format .json on disk and uploads there the transmitted information, stored in any variable variable

