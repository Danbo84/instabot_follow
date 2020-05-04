import os
import sys

#code by _hugo_jobe_

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot

bot = Bot()
bot.login(username="TOM PSEUDO", password="TON MOT DE PASSE")

bot.approve_pending_follow_requests()

