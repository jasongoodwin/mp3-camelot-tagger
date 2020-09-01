import unittest

from mp3_file import Mp3File

class Mp3FileTestSuite(unittest.TestCase):
    def test_should_read_file_if_exists(self):
        file = Mp3File("resources/tagged.mp3")
        self.assertEqual(file.get_key(), "Abmin")
        file.update_key()
        self.assertEqual(file.get_key(), "1A")

    def test_should_convert_key(self):
        file = Mp3File("resources/tagged.mp3")
        self.assertEqual(file.convert_key("Abmin"), "1A")

if __name__ == '__main__':
    unittest.main()
