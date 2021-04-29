import shortuuid
from datetime import datetime

shortuuid.set_alphabet("0123456789")

class Game:

    def __init__(self, author,name, playdate):
        self.id = shortuuid.uuid()
        self.datecreated = datetime.now()
        self.author = author
        self.playdate = playdate
        self.name = name
        self.banned = {}
        self.picked = {}

    def set_ban(self, author, ban):
        self.banned[author] = ban

    def set_pick(self, author, pick):
        self.picked[author] = pick

    def get_name(self):
        return str(self.name)

    def get_author(self):
        return str(self.author)

    def get_playdate(self):
        return str(self.playdate)
