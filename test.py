
import yt_ext
#hint code here: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp


#playlist = "https://www.youtube.com/playlist?list=PLAwxTw4SYaPnhRXZ6wuHnnclMLfg_yjHs"
playlists =[
    "https://www.youtube.com/playlist?list=PLAwxTw4SYaPn79fsplIuZG34KwbkYSedj", #4
    "https://www.youtube.com/playlist?list=PLAwxTw4SYaPkr-vo9gKBTid_BWpWEfuXe", #5
    "https://www.youtube.com/playlist?list=PLAwxTw4SYaPndXEsI4kAa6BDSTRbkCKJN" #6
]
i=3
info={}
for playlist in playlists:
    i+=1
    print("Processing playlist {}...".format(i) )
    info[i] = (yt_ext.get_video_count(playlist),yt_ext.get_playlist_duration(playlist))

for i in range(4,7):
    (count,duration) = info[i]
    (d,h,m,s) = yt_ext.seconds_to_dhms(duration)
    text_duration= yt_ext.dhms_to_string((d,h,m,s))
    print('Playlist #{}: Videos: {}, Duration: {}'.format(i,count,text_duration))

import AppKit
AppKit.NSBeep()