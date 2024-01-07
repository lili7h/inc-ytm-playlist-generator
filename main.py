from pathlib import Path
from ytmusicapi import YTMusic
from loguru import logger


MONSTERCAT: Path = Path('lists/MonstercatList.txt')
EPIDEMIC: Path = Path('lists/EpidemicList.txt')
MONSTERCAT_PL_ID: str = "VLPLs4gA2jv-WBk6nB7AdTKHGJgm19qo95hI"
EPIDEMIC_PL_ID: str = "PLs4gA2jv-WBnGXkRtlfMLEDaU_4-UGp63"

yt = YTMusic('oauth.json')


def populate_epidemic_pl():
    songs = [x.strip() for x in EPIDEMIC.read_text('utf16').split(".mp3")]
    _empties: int = 0
    for song in songs:
        if song == '':
            _empties += 1

    for i in range(_empties):
        songs.remove('')

    print(f"There are {len(songs)} songs in the list.")
    for song in songs:
        search_results = yt.search(song)
        logger.info(f"Searching for '{song}'...")
        try:
            yt.add_playlist_items(EPIDEMIC_PL_ID, [search_results[0]['videoId']])
            logger.success(f"Added song '{search_results[0]['title']}' to playlist.")
        except KeyError:
            # This happens when the search returns an album as the first element,
            # rather than a song. Can't be bothered to fix this atm
            logger.error(f"Failed to add song '{song}'.")


def populate_monstercat_pl():
    songs = [x.strip() for x in MONSTERCAT.read_text('utf16').split(".mp3")]
    _empties: int = 0
    for song in songs:
        if song == '':
            _empties += 1

    for i in range(_empties):
        songs.remove('')

    print(f"There are {len(songs)} songs in the list.")
    for song in songs:
        search_results = yt.search(song)
        logger.info(f"Searching for '{song}'...")
        try:
            yt.add_playlist_items(MONSTERCAT_PL_ID, [search_results[0]['videoId']])
            logger.success(f"Added song '{search_results[0]['title']}' to playlist.")
        except KeyError:
            # This happens when the search returns an album as the first element,
            # rather than a song. Can't be bothered to fix this atm
            logger.error(f"Failed to add song '{song}'.")


populate_monstercat_pl()