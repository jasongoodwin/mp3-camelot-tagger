# mp3-key-translator
Take rekordbox generated key data in mp3s and convert it to whatever format you want.

# DON'T USE THIS!
Note that this probably doesn't work so please proceed with caution.
The key map is missing so you'd need to fill that out (note that camelot is proprietary so I will not post the notation here.)

## Why write this?
I was using mixed-in-key w/ rekordbox for a while just to get camelot notation.
I lost my mixed-in-key license while prepping on the road so I decided to just take the beatport TKEY tag and convert it to Camelot notation.
I couldn't find anything easy to use that did this for me - mac has python running.
I wanted to see and understand the ID3 data a bit better so I wrote this.

## Is this legal?
Not with the Camelot notation - my friend Sara Simms just highlighted to me that camelot is IP of mixed-in-key. 
This project does not include key translations - you'll have to fill that in yourself.
I mailed Yakov @ Mixed in Key and he said that it would be confusing for users to translate the Beatport keys to camelot as they're very often wrong (and Mixed-In-Key is generally only off by a fifth if it's off at all - Yakov mentioned this is fixed/improved in upcoming versions.)
I found my mixed in key license and strongly recommend using it - this project was just a little one or two hour hack project, but it's here if you want to translate your key notation in the ID3 tags for any reason, or if you just want to see how to interact with the metadata in python.

## Usage
Note you'll need to first modify this to fill in the key mappings.
Pass a file or list of files to the script (shown below).
It will validate it can open and modify _ALL_ files passed before writing the updated tags.
Note that rekordbox will _not_ save the tags if you're using rekordbox for keying files.
Beatport includes key information, so this may update the beatport key tags after analyzing w/ rekordbox - just be careful and try on a file or two to ensure your workflow is functioning as expected.

To use just pass a list of mp3 files as arguments. It tries to safely validate the files are there, can be read, and have the _expected_ key information.
```
python mp3-camelot-tagger music_location/*.mp3
```
