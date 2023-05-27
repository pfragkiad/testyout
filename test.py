
import yt_ext
#hint code here: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp


#playlist = "https://www.youtube.com/playlist?list=PLAwxTw4SYaPnhRXZ6wuHnnclMLfg_yjHs"
playlists =[
    "https://www.youtube.com/playlist?list=PLAwxTw4SYaPn79fsplIuZG34KwbkYSedj", #4
    "https://www.youtube.com/playlist?list=PLAwxTw4SYaPkr-vo9gKBTid_BWpWEfuXe", #5
    "https://www.youtube.com/playlist?list=PLAwxTw4SYaPndXEsI4kAa6BDSTRbkCKJN" #6
]
i=3
durations={}
for playlist in playlists:
    i+=1
    print("Processing playlist {}...".format(i) )
    durations[i] = yt_ext.get_playlist_duration(playlist)

for i in range(4,7):
    (d,h,m,s) = yt_ext.seconds_to_dhms(durations[i])
    if d > 0:
        print('Playlist #{}: {:02d}d {:02d}h {:02d}m {:02d}s'.format(i,d, h, m, s))
    elif h > 0:
        print('Playlist #{}: {:02d}h {:02d}m {:02d}s'.format(i,h, m, s))
    elif m > 0:
        print('Playlist #{}: {:02d}m {:02d}s'.format(i,m, s))
    elif s > 0:
        print('Playlist #{}: {:02d}s'.format(i,s))

import AppKit
AppKit.NSBeep()