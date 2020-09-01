import click

from mp3_file import Mp3File

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
def main(filenames):
    print("Attempting to open mp3 files for read/write...")
    print("Not all files passed MUST be tagged correctly.")

    click.echo("{}".format(filenames))
    print("")

    mp3s = list(map(lambda fn: Mp3File(fn), filenames))
    print("all files open successfully as MP3 files. Will validate we can update all TKEY tags:")
    print("")

    for mp3 in mp3s:
        print(mp3)
        mp3.update_key()
        print("updates to")
        print(mp3)
        print("")

    print("Will now save updated files!")

    for mp3 in mp3s:
        print("saving: " + mp3.__str__())
        mp3.save_updated_file()

if __name__ == "__main__":
    main()