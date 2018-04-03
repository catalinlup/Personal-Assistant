try:
    import imageio
    imageio.plugins.ffmpeg.download()
except:
    print("Error Install Imageio!")
try:
    from moviepy.editor import*
except:
    print("Error Install MoviePy!")
try:
    from pytube import YouTube
except:
    print("Error Install Pytube!")
from codes import*
import os
import time
def DownloadYouTubeAudio(url,name):
    yt=YouTube(url)
    yt.streams.first().download(PATH_TO_AUDIO)
    extension=str(yt.streams.first().mime_type).split('/')[1]
    clip=VideoFileClip(PATH_TO_AUDIO+"/"+yt.title+'.'+extension)
    ptToRemove=PATH_TO_AUDIO+"/"+yt.title+'.'+extension
    clip.audio.write_audiofile(PATH_TO_AUDIO+"/"+name+".mp3")
