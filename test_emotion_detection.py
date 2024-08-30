from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emtotion_detector(self):
        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual(result_joy['dominant_emotion'], 'joy')

        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual(result_anger['dominant_emotion'], 'anger')

        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')

        result_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(result_sadness['dominant_emotion'], 'sadness')

        result_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

unittest.main()