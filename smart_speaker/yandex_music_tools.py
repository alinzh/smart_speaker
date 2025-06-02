from yandex_music import Client
import random
import yaml
from smolagents import tool

    
with open("./conf.yaml", "r") as yamlfile:
    conf = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
    
client = Client(conf['api_key_yandex']).init()

@tool
def get_first_track() -> str:
    """
    Returns the first track from 'Мне нравится. Downloads to directory './music_data/current.mp3'.'
    """
    track = client.users_likes_tracks()[0].fetch_track()
    track.download('./music_data/current.mp3')
    return f"Track downloaded successfully. Artist: {track.artists[0].name}, Track: {track.title}"

@tool
def get_random_track() -> str:
    """
    Returns the random track from 'Мне нравится'. Downloads to directory './music_data/current.mp3'.
    """
    track = client.users_likes_tracks()[random.randint(0, len(client.users_likes_tracks()))].fetch_track()
    track.download('./music_data/current.mp3')
    return f"Track downloaded successfully. Artist: {track.artists[0].name}, Track: {track.title}"

@tool
def get_track_by_query(query: str) -> str:
    """
    Performs track search on request. Downloads to directory './music_data/current.mp3'.
    
    Args:
        query: free text query
    """
    track = client.search(query).tracks.results[0]
    track.download('./music_data/current.mp3')
    return f"Track downloaded successfully. Artist: {track.artists[0].name}, Track: {track.title}"

music_tools = [get_first_track, get_random_track, get_track_by_query]


if __name__ == '__main__':
    input_query = 'Дайте танк - Люди любят'
    res = get_track_by_query(input_query)
    print(res)
    
    res = get_first_track()
    print(res)
    
    res = get_random_track()
    print(res)
