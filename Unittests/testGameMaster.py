import unittest
from unittest import mock
import Sources.GameMaster


class TestGetHero(unittest.TestCase):
    def setUp(self):
        self.GM = Sources.GameMaster.GameMaster()
        self.old_hero = "old_hero"
        self.new_hero = "new_hero"
        self.old_user_id = 4201
        self.new_user_id = 4202
        self.GM.current_heroes = {str(self.old_user_id): self.old_hero}

        self.GM.createHero = mock.Mock(return_value=self.new_hero)

    def testUserIDIsOld(self):
        result = self.GM.getHero(self.old_user_id)
        assert self.old_hero == result

    def testUserIDIsNew(self):
        result = self.GM.getHero(self.new_user_id)
        assert self.new_hero == result
