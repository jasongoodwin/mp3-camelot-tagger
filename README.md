# mp3-camelot-tagger
Take rekordbox generated key data in mp3s and convert it to camelot.

# DON'T USE THIS!
Note that this probably doesn't work so please proceed with caution.
Still being tested, and actually camelot is licensed by Mixed-in-key so we likely cannot use the notation in open-source projects.

## Why write this?
I was using mixed-in-key w/ rekordbox for a while just to get camelot notation.
I lost my mixed-in-key license while prepping on the road so I decided to just take the beatport TKEY tag and convert it to Camelot notation.
I couldn't find anything easy to use that did this for me - mac has python running. This project has everything you need to get this done easily.

## Is this legal?
No - my friend Sara Simms just highlighted to me that camelot is IP of mixed-in-key so I can't keep this up. I'm querying 

## Usage
Pass a file or list of files to the app.
It will validate it can open and modify _ALL_ files passed before writing the updated tags.
Note that rekordbox will _not_ save the tags if you're using rekordbox for keying files.
Beatport includes key information, so this may update the beatport key tags after analyzing w/ rekordbox - just be careful and try on a file or two to ensure your workflow is functioning as expected.

To use just pass a list of mp3 files as arguments. It tries to safely validate the files are there, can be read, and have the _expected_ key information.
```
python mp3-camelot-tagger music_location/*.mp3
```
