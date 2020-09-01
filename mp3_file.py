from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TKEY

class Mp3File():
    KEYS_MAP = {
        "Abmin": "1A",
        "G#min": "1A",

        "Ebmin": "2A",
        "D#min": "2A",

        "Bbmin": "3A",
        "A#min": "3A",

        "Fmin": "4A",

        "Cmin": "5A",

        "Gmin": "6A",

        "Dmin": "7A",

        "Amin": "8A",

        "Emin": "9A",

        "Bmin": "10A",

        "F#min": "11A",
        "Gbmin": "11A",

        "Dbmin": "12A",
        "C#min": "12A",

        "B": "1B",

        "F#": "2B",
        "Gb": "2B",

        "Db": "3B",
        "C#": "3B",

        "Ab": "4B",
        "G#": "4B",

        "Eb": "5B",
        "D#": "5B",

        "Bb": "6B",
        "A#": "6B",

        "F": "7B",

        "C": "8B",

        "G": "9B",

        "D": "10B",

        "A": "11B",

        "E": "12B",
    }

    def __init__(self, file_location):
        """ Class representing an mp3 file.
        - Throws IOError if file not found.
        - self.file is None if not mp3"""
        self.file_location = file_location
        self.easyid3 = EasyID3(file_location)
        self.id3 = ID3(file_location)

        # print("try")
        # print(self.id3["TKEY"][0])
        # self.id3.add(TKEY(encoding = 3, text=[u"A1"]))
        # print("set now print")
        # print(self.id3["TKEY"][0])

    def get_key(self):
        return self.id3["TKEY"][0]

    def convert_key(self, old_key):
        return self.KEYS_MAP[old_key]

    def update_key(self):
        tkey = self.get_key()
        new_key = self.KEYS_MAP[tkey]
        self.id3.add(TKEY(encoding=3, text=[new_key]))

    def save_updated_file(self):
        self.id3.save()

    def __str__(self):
        return """Artist: {} Title: {} Key: [{}]""".format(self.easyid3["artist"], self.easyid3["title"], self.id3["TKEY"][0])