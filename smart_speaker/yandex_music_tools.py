from yandex_music import Client
import random
import yaml
    
    
with open("./conf.yaml", "r") as yamlfile:
    conf = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
    
client = Client(conf['api_key_yandex']).init()


def get_first_track() -> str:
    track = client.users_likes_tracks()[0].fetch_track()
    track.download('./music_data/example_current.mp3')
    return f"Artist: {track.artists[0].name}, Track: {track.title}"

def get_random_track() -> str:
    track = client.users_likes_tracks()[random.randint(0, len(client.users_likes_tracks()))].fetch_track()
    track.download('./music_data/example_current.mp3')
    return f"Artist: {track.artists[0].name}, Track: {track.title}"

def get_track_by_query(query) -> str:
    track = client.search(query).tracks.results[0]
    track.download('./music_data/example_current.mp3')
    return f"Artist: {track.artists[0].name}, Track: {track.title}"


if __name__ == '__main__':
    input_query = 'Дайте танк - Люди любят'
    res = get_track_by_query(input_query)
    print(res)
    
    res = get_first_track()
    print(res)
    
    res = get_random_track()
    print(res)
