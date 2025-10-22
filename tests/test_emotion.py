import unittest
from app.emotion import emotion

class TestEmotionPredictor(unittest.TestCase):
    def test_joy(self):
        result = emotion("I am so happy today!")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion("I am feeling very down.")
        self.assertEqual(result["dominant_emotion"], "sadness")

if __name__ == '__main__':
    unittest.main()
