# mp3-camelot-tagger
Take rekordbox generated key data in mp3s and convert it to camelot.

## Why write this?
I was using mixed-in-key w/ rekordbox for a while just to get camelot notation.
I'd rather just take the key-data that's there and convert it to camelot notation so this does that.
I couldn't find anything easy to use that did this for me - mac has python running. This project has everything you need to get this done easily.

## Usage
Pass a file or list of files to the app.
It will validate it can open and modify _ALL_ files passed before writing the updated tags.
Note that rekordbox will _not_ save the tags if you're using rekordbox for keying files.
Beatport includes key information, so this may update the beatport key tags after analyzing w/ rekordbox - just be careful and try on a file or two to ensure your workflow is functioning as expected.

To use just pass a list of mp3 files as arguments. It tries to safely validate the files are there, can be read, and have the _expected_ key information.
```
python mp3-camelot-tagger music_location/*.mp3
```
