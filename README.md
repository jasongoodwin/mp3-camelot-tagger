# mp3-key-translator
Take rekordbox or beatport generated key data in mp3s and convert it to whatever format you want.
Note that this project is not really in any state for use, I just wanted to see if I could do it and to understand the ID3 spec a bit better.

# DON'T USE THIS!
Note that this probably doesn't work so please proceed with caution.
The key map is missing so you'd need to fill that out (note that camelot is proprietary so I will not post the notation/translation here.)
The key detection from beatport or rekordbox is not as accurate as camelot so I'd recommend you just buy a copy of Mixed-In-Key if you want camelot notation - if you translate from other detection sources you'll end up with some bad/wrong keys. 
You can read some older (2016) DubSpot analysis of the accuracy here: http://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport/
You'll see mixed-in-key's detection is more reliable, and, when it's incorrect, it's only off by a fifth - you can trust it. Yakov @ Mixed in Key has assured me the new and upcoming versions are even more accurate.

## Why write this?
I was using mixed-in-key w/ rekordbox for a while just to get camelot notation.
I lost my mixed-in-key license while prepping on the road so I decided to just take the beatport TKEY tag and convert it to Camelot notation.
I couldn't find anything easy to use that did this for me - mac has python running.
I wanted to see and understand the ID3 data a bit better so I wrote this.

## Is this legal?
Not with the Camelot notation - my very good friend Sara Simms just highlighted to me that camelot is IP of mixed-in-key. 
This project does not include key translations - you'll have to fill that in yourself if you choose to use it but know it will often not be accurate if you're using other sources of detection (Traktor, Rekordbox, Beatport, etc).
I mailed Yakov @ Mixed in Key and he said that it would be confusing for users to translate the Beatport-detected keys to camelot as they're very often wrong (and Mixed-In-Key is generally only off by a fifth if it's off at all - Yakov mentioned this is fixed/improved in upcoming versions.)
I found my mixed in key license and strongly recommend using it. I've been using it since v3 or v4.

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
