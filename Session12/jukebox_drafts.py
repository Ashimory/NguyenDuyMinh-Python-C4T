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


ydl_opts = {
    # 'outtmpl': "%(id)s", 
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    a = ydl.extract_info('https://www.youtube.com/watch?v=Xmg8xinUO-M', download = True )
    # b = ydl.extract_info('https://www.youtube.com/watch?v=lwM14YRpq-0', download = True )
    c = ydl.extract_info('https://www.youtube.com/watch?v=ImPM5IDIYPs', download = True )
# information = {
#     1:a,
#     2:b,
#     3:c,
# }
# with open("info.txt", "w") as a:
#     a.writelines(information)