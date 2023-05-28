
import yt_ext

#hint code here: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp


def show_comp_playlists():
    playlist_names = {
        "p3":"PLAwxTw4SYaPnhRXZ6wuHnnclMLfg_yjHs", #3
        "p4":"PLAwxTw4SYaPn79fsplIuZG34KwbkYSedj", #4
        "p5":"PLAwxTw4SYaPkr-vo9gKBTid_BWpWEfuXe", #5
        "p6":"PLAwxTw4SYaPndXEsI4kAa6BDSTRbkCKJN" #6
    }

    playlists = {}
    for key,name in playlist_names:
        playlists[key] = yt_ext.Playlist(name, populate_now=True);
        print(f"Processing playlist {key}...")

    for key,p in playlists:

        (d,h,m,s) = yt_ext.seconds_to_dhms(p.total_duration_seconds)
        text_duration= yt_ext.dhms_to_string((d,h,m,s))
        print(f'Playlist #{key}: Videos: {p.videos_count}, Duration: {text_duration}')

p = yt_ext.Playlist('PLm7BxCUdWqZzjZ-jRe73KUfj2GsSS2FPy', populate_now=True)
p.show_info()

import AppKit
AppKit.NSBeep()