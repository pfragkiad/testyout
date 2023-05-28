
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
print("Reading videos...")
p_arch = yt_ext.Playlist(arch,False)
p_arch.update_video_urls(False)
print("Downloading...")
p_arch.download()
