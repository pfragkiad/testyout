
import yt_ext




import yt_ext_samples
#yt_ext_samples.show_simple_playlist_info()

# import threading

# import time
# def task(item):
#     time.sleep(5)
#     print(item)

# items =(i for i in range(1,101))

# threads=[]
# for item in items:
#     t = threading.Thread(target=task,args=(item,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()
# print('done!')

arch = "PLPidHDiAMOCuZRa1f0k88gKsRXwXCvJjh"
#print("Reading videos...")
#p_arch = yt_ext.Playlist(arch,False)
#p_arch.update_video_urls(False)
#print("Downloading...")
#p_arch.download()

import yt_dlp
ydl_opts = {
        'dump_single_json': True,
        'extract_flat': 'in_playlist',
        'playlist_items': '1-',
        'skip_download': True,
    }

playlist_url = yt_ext.build_playlist_url(arch)
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)
    for key,value in info.items():
        if key =='entries':
            i=0
            for entry in value:
                i+=1
                for key2,value2 in entry.items():
                    print(f'{i}  {key2}={value2}') 
        else:
            print(f'{key}={value}')
    
