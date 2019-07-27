from __future__ import unicode_literals
import youtube_dl, json
playlist = {}
mainmenu = ["Show all songs", "Show song details", "Play a song", "Search and download a song", "Exit"]
print("No, we don't need your money like a normal jukebox...")
for i in range(0, len(mainmenu)):
    print(i+1, ".", mainmenu[i])
act = int(input())
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
    down = int(input("Choose song to download:")) - 1
    downurl = a[down]["webpage_url"]
    ydl_opts['outtmpl'] = '%(id)s.%(mp3)s'
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        dl = ydl.extract_info(downurl, download = False)
    with open("playlist.json","a+", encoding="utf8") as f:
        # try:
        pl = json.load(f)
        pl.append(dl)
        f.seek(0) 
        json.dump (pl,f)
        # except json.JSONDecodeError:
        #     json.dump([dl],f)
