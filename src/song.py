import vlc
import time
song = vlc.MediaPlayer("songs/song.mp3")

singer = input("Choose a singer(Chainsmokers,Marshmello,Alan Walker)")
if singer == "Marshmello":
    mello = input("Choose the song (Alone, Friends)")
    if mello ==  "Friends":
        song.play()
    elif mello == "Alone":
        song.play()
    else:
        print("Invalid Input")
elif singer == "Chainsmokers":
    smokers = input("Choose the song(Closer, High)")
    if smokers == "Closer":
        song.play()
    elif smokers == "High":
        song.play()
    else:
        print("Invalid Input")
elif singer == "Alan Walker":
    walker = input("Choose a song(Faded, Lost Control)")
    if walker == "Faded":
        song.play()
    elif walker == "Lost Control":
        song.play()
    else:
        print("Invalid Input")
        
else:
    print("Invalid Input")

time.sleep(200)


