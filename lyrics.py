from lyrics_extractor import SongLyrics

# Replace with your own API key and Engine ID
api_key = "YOUR_API_KEY"
engine_id = "YOUR_ENGINE_ID"

extract_lyrics = SongLyrics(api_key, engine_id)

# Example: Get lyrics for the song "Shape of You"
song_name = "Shape of You"
lyrics = extract_lyrics.get_lyrics(song_name)
print(lyrics['lyrics'])

from tkinter import *
from lyrics_extractor import SongLyrics

def get_lyrics():
    extract_lyrics = SongLyrics("YOUR_API_KEY", "YOUR_ENGINE_ID")
    song_name = e.get()
    lyrics = extract_lyrics.get_lyrics(song_name)
    result.set(lyrics['lyrics'])

master = Tk()
master.configure(bg='light grey')

result = StringVar()

Label(master, text="Enter Song name:", bg="light grey").grid(row=0, sticky=W)
Label(master, text="Result:", bg="light grey").grid(row=3, sticky=W)

Entry(master, textvariable=result, bg="light grey").grid(row=3, column=1)
e = Entry(master, width=50)
e.grid(row=0, column=1)

Button(master, text="Show", command=get_lyrics, bg="Blue").grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
