import unittest
import Sources.Scene


class TestSendActions(unittest.TestCase):
    def setUp(self):
        self.scene = Sources.Scene.Scene()
        self.actionsWithWait = ["wait"]