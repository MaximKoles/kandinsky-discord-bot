# Installation

1. First we need to check that Python is installed and have 3.11 version(its important)
```
python -V
```
if running this command in command line giver error like "python is not recognized bla bla bla" or it have not 3.11 version we need to install 3.11 version from [official website](https://www.python.org/downloads/release/python-3110/)

Right result should be:
```
python -V
Python 3.11.0
```

2. Now lets clone repository with bot by command below, if git isnt installed, install [it](https://git-scm.com/downloads)
```
git clone https://github.com/MaximKoles/kandinsky-telegram-bot
cd kandinsky-telegram-bot
```

3. To install needed modules lets run this command:
```
pip install -r requirements.txt
```

4. IMPORTANT!! If you used libraries such as nextcord, disnake, discord, discord.py, DiscordUtils, etc... before, you need to uinstall them after uninstallation of them or if you didnt used them, you should run command to install py-cord:
```
pip install -U git+https://github.com/Pycord-Development/pycord
```

5.After all of this actions we need to get our api tokens:

1)First token that we need is Replicate api token, to get it enter [Replicate](https://replicate.com/) website, Login or Register if you not, then go to your profile page and copy token, save it somewhere


6. Замените токены
```
REPLICATE_API_TOKEN=<paste your replicate token here instead of this text and ><>
TELEGRAM_BOT_TOKEN=<paste here your discord bot token instead of this text and ><>
```

7. Run bot by command:
```
python kandinsky.py
```
wait some minutes after this to sync commands

8. Enjoy bot!!!!

# How to use this command of bot?
![image](https://user-images.githubusercontent.com/118455214/230778796-69a0ff38-e5fe-48e0-ab60-4f86db83ad6b.png)

This bot will have slash command /kandinsky that have options:
`prompt`(required) - text of what should be on picture
`steps` - number of steps in 1-500
`scale` - scale varioable is float and can be from 1 to 20
Generation time depends on steps and scale value
