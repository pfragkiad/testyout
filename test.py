
import yt_ext


import yt_ext_samples
#yt_ext_samples.show_simple_playlist_info()
#yt_ext_samples.show_comp_playlists()

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

#arch = "PLPidHDiAMOCuZRa1f0k88gKsRXwXCvJjh"
#print("Reading videos...")
#p_arch = yt_ext.Playlist(arch,False)
#p_arch.update_video_urls(False)
#print("Downloading...")
#p_arch.download()

p4 = "PLAwxTw4SYaPn79fsplIuZG34KwbkYSedj"
p = yt_ext.Playlist(p4,True)
duration = p.get_partial_duration(83,103)
text_duration= yt_ext.seconds_to_dhms_string(duration)
print(f'Playlist #{p4}: Duration: {text_duration}')

    
