import unittest
import Sources.Scene


class TestSendActions(unittest.TestCase):
    def setUp(self):
        self.scene = Sources.Scene.Scene()
        self.actionsIsEmpty = []

    def testActionsIsEmpty(self):
        with self.assertRaises(ValueError):
            self.scene.sendActions(self.actionsIsEmpty)
