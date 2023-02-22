from AtiyaMusic.core.bot import AtiyaBot
from AtiyaMusic.core.dir import dirr
from AtiyaMusic.core.git import git
from AtiyaMusic.core.userbot import Userbot
from AtiyaMusic.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = AtiyaBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
