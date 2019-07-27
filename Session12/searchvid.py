from __future__ import unicode_literals
import youtube_dl, json


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

search = input("Enter search term").lower()
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
    res = ydl.extract_info( search, download = False )
    # print(res)
# with open("searches1.json","w") as a:
#     json.dump(res, a)

a = res['entries']
for i in range (len(a)):
    c = a[i]["title"]
    print (i+1,".", c)
# print (a)
# with open('search2.json', 'w') as b:
#     json.dump(a, b)