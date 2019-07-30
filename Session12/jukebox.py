from __future__ import unicode_literals
from pyglet.media import Source, Player, load
import youtube_dl, json
player =  Player()
# Loop
while True:
    # Error check:
    try:
        with open("playlist.json","r+", encoding="utf8") as f:
            try:
                json.load(f)
                error_key = 0
            except json.JSONDecodeError:
                error_key = 1
    except FileNotFoundError:
        error_key = 2
    # Menu:
    mainmenu = ["Show all songs", "Show song details", "Play a song", "Search and download a song", "Exit"]
    for i in range(0, len(mainmenu)):
        print(i+1, ".", mainmenu[i])
    act = int(input("No, we don't need your money like a normal jukebox... Just enter 1-5 for the corresponding actions: "))
    # Open playlist a.k.a show all songs
    if act == 1:
        if error_key == 0:
            pl = json.load(f)
            for i in range(len(pl)):
                print(i+1,".", pl[i]["title"])
        elif error_key == 1 or error_key == 2:
            print("This playlist is as empty as my wallet!")
    # Show song details
    if act == 2:
        if error_key == 0:
            pl = json.load(f)
            for i in range(len(pl)):
                print(i+1,".", pl[i]["title"])
            detail_query = int(input("Enter song number to see details: ")) - 1
            for i in ["id", "title", "duration"]:
                print(i.capitalize()+":", pl[detail_query][i])
        elif error_key == 1 or error_key == 2:
            print("This playlist is as empty as my wallet!")
    # Play a song
    if act == 3:
        if error_key == 0:
            pl = json.load(f)
            for i in range(len(pl)):
                print(i+1,".", pl[i]["title"])
            queue_song = int(input("Enter song number to add to playlist ")) - 1
            source = load(pl["id"]+".mp3")
            player.queue(source)
            player.play()
            while True:
                playback = input("Enter play, pause or stop for corresponding actions: ")
                if playback.lower() == "play":
                    player.play()
                elif playback.lower() == "pause":
                    player.pause()
                elif playback.lower() == "stop":
                    break

        elif error_key == 1 or error_key == 2:
            print("This playlist is as empty as my wallet!")
    #Search + download a song
    if act == 4:
        class MyLogger(object):
            def debug(self, msg):
                pass

            def warning(self, msg):
                pass

            def error(self, msg):
                print(msg)

        def my_hook(d):
            if d['status'] == 'finished':
                print('Done downloading, now converting ...')

        search = input("Enter search term: ").lower()
        searchnumber = "ytsearch"+input("Number of results?")
        ydl_opts = {
            'format': 'bestaudio/best',
            'default_search': searchnumber, 
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            res = ydl.extract_info(search, download = False)

        a = res['entries']
        for i in range (len(a)):
            c = a[i]["title"]
            print (i+1,".", c)
        down = input("Choose song number to download, or enter cancel to cancel operation : ")
        if down.lower() == "cancel":
            break
        else:
            downurl = a[int(down)-1]["webpage_url"]
            ydl_opts['outtmpl'] = '%(id)s.%(mp3)s'
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                dl = ydl.extract_info(downurl, download = True)
                if error_key == 0:
                    pl = json.load(f)
                    pl.append(dl)
                    f.seek(0) 
                    json.dump (pl,f)
                elif error_key == 1:
                    json.dump([dl],f)
                elif error_key == 2:
                    with open("playlist.json","a+", encoding="utf8") as f:
                        json.dump([dl],f)
            play_audio = input("Do you want to play the song now? y/n")
            if play_audio.lower() == "y":
                source = load(dl["id"]+".mp3")
                player.queue(source)
                player.play()
                while True:
                    playback = input("Enter play, pause or stop for corresponding actions: ")
                    if playback.lower() == "play":
                        player.play()
                    elif playback.lower() == "pause":
                        player.pause()
                    elif playback.lower() == "stop":
                        break
    # Exit
    if act == 5:
        print("Shutting down...")
        break