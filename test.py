
import yt_ext

#hint code here: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp



import yt_ext_samples
#yt_ext_samples.show_simple_playlist_info()

import threading

import time
def task(item):
    time.sleep(5)
    print(item)

items =['asdf','ffdsafs']

threads=[]
for item in items:
    t = threading.Thread(target=task,args=(item,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print('done!')