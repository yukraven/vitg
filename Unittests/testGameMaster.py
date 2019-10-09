import unittest
import Sources.GameMaster


class TestSendMessage(unittest.TestCase):
    def setUp(self):
        self.GM = Sources.GameMaster.GameMaster()
        self.newUserId = 424242
        self.oldUserId = 441591973

    def testUserIsNew(self):
        result =
