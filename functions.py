import csv
import json

data = []
file_name = 'data.csv'
with open(file_name) as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

text_file = open('top-500-songs.txt', 'r')
lines = text_file.readlines()
song_data = []
for line in lines:
    song = {}
    line = line.rstrip().split('\t')
    song['rank'] = line[0]
    song['name'] = line[1]
    song['artist'] = line[2]
    song['year'] = line[3]
    song_data.append(song)
    
file = open('track_data.json', 'r')
json_data = json.load(file)
        
def find_by_name(data, keyword, name):
    album = None
    for details in data:
        if(details[keyword] == name):
            album = details
            break
    return album

def find_by_rank(data, keyword, rank):
    album = None
    for details in data:
        if(details[keyword] == str(rank)):
            album = details
            break
    return album

def find_by_year(data, keyword, year):
    albums = []
    for details in data:
        if(details[keyword] == str(year)):
            albums.append(details)
    return albums

def find_by_years(data, keyword, start_year, end_year):
    albums = []
    for details in data:
        if(int(details[keyword]) >= start_year and int(details[keyword]) <= end_year):
            albums.append(details)
    return albums

def find_by_ranks(data, keyword, start_rank, end_rank):
    albums = []
    for details in data:
        if(int(details[keyword]) >= start_rank and int(details[keyword]) <= end_rank):
            albums.append(details)
    return albums

def all_titles(data, keyword):
    titles = []
    for details in data:
        titles.append(details[keyword])
    return titles

def all_artists(data, keyword):
    artists = []
    for details in data:
        artists.append(details[keyword])
    return list(set(artists))

def artists_with_the_most_albums(data, keyword):
    unique_artists = {}
    most_albums = 0
    most_artists = []
    for artist in all_artists(data,keyword):
        unique_artists[artist.title()] = 0
    for details in data:
        unique_artists[details[keyword].title()] += 1
    most_albums = max(unique_artists.values())
    for artist in unique_artists:
        if(unique_artists[artist] == most_albums):
            most_artists.append(artist)
    return most_artists

def most_popular_word(data, keyword):
    max_words = []
    most_words = 0
    unique_words = {}
    for title in all_titles(data, keyword):
        for word in title.split():
            unique_words[word.title()] = 0
    for title in all_titles(data, keyword):
        for word in title.split():
            unique_words[word.title()] += 1
    most_words = max(unique_words.values())
    for word in unique_words:
        if(unique_words[word.title()] == most_words):
            max_words.append(word)

    return max_words

def histogram_of_albums_by_decade():
    pass

def histogram_by_genres():
    pass

def album_with_most_top_songs():
    pass

def albums_with_top_songs():
    pass

def songs_that_are_on_top_albums():
    pass

def top_ten_albums_by_top_songs():
    pass

def top_overall_artist():
    pass