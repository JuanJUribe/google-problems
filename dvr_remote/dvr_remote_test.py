import unittest
import dvr_remote

def getChar(position, grid_size):
    return chr(ord('a') + position['y'] * grid_size + position['x'])

def testSequenceChars(sequence):
    allowed_chars = "udlr!"
    if (set(sequence) - set(allowed_chars)):
        return False;
    return True

def testSequence(sequence):
    max_x = 4
    max_y = 5
    current_pos = {'x': 0, 'y': 0}
    result_string = ""
    normalized_sequence = sequence.lower()
    if not testSequenceChars(sequence):
        return ""
    for char in sequence.lower():
        if char == '!':
            result_string += getChar(current_pos, 5)
        elif char == 'd':
            if (current_pos['y'] < 5 and current_pos['x'] == 0) or current_pos['y'] < 4:
                current_pos['y'] += 1
        elif char == 'u':
            if current_pos['y'] > 0:
                current_pos['y'] += -1
        elif char == 'r':
            if current_pos['x'] < 4 and current_pos['y'] < 5:
                current_pos['x'] += 1
        elif char == 'l':
            if current_pos['x'] > 0:
                current_pos['x'] += -1
    return result_string

class DvrRemoteTest(unittest.TestCase):
    def setUp(self):
        self.remote = dvr_remote.DvrRemote()

    def tryAndCompare(self, input_string):
        res = self.remote.remoteControlSequence(input_string)
        self.assertEqual(input_string.lower(), testSequence(res))

    # Empty string -> No directions
    def testEmptyChar(self):
        test_string = ""
        self.tryAndCompare(test_string)

    # Single Direction
    def testA(self):
        test_string = "a"
        self.tryAndCompare(test_string)

    def testE(self):
        test_string = "e"
        self.tryAndCompare(test_string)

    def testF(self):
        test_string = "f"
        self.tryAndCompare(test_string)

    def testZ(self):
        test_string = "z"
        self.tryAndCompare(test_string)

    def testTwoLetterSequenceSameRowRight(self):
        test_string = "ce"
        self.tryAndCompare(test_string)

    def testTwoLetterSequenceSameRowLeft(self):
        test_string = "db"
        self.tryAndCompare(test_string)

    def testTwoLetterSequenceSameColumnDown(self):
        test_string = "az"
        self.tryAndCompare(test_string)

    def testTwoLetterSequenceSameColumnUp(self):
        test_string = "zf"
        self.tryAndCompare(test_string)

    def testLongString(self):
        test_string = "helloworld"
        self.tryAndCompare(test_string)

    # You must add your test cases here if you want to be sure about your
    # solution.

if __name__=="__main__":
    unittest.main()