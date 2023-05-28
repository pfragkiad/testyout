import yt_dlp

#hint code here: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp

import threading

class Video:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'{self.name}'

class Playlist:
    def __init__(self, name,populate_now = False):
        self.name = name
        if populate_now:
            self.update_video_urls()

    def get_url(self):
        baseurl = "https://www.youtube.com/playlist?list="
        return f'{baseurl}{self.name}'

    def update_video_urls(self, get_durations = True):
        url = self.get_url()
        self.videos = get_video_urls(url)
        self.videos_count = len(self.videos)
        #or: self.total_duration_seconds = get_playlist_duration(url)
        if get_durations:
            self.total_duration_seconds = sum(get_video_duration(v) for v in self.videos)

    def download(self):
        threads=[]
        for url in self.videos:
            t = threading.Thread(target=download_video,args=(url,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        # for url in self.videos:
        #     with yt_dlp.YoutubeDL() as ydl:
        #         ydl.download(url)

    #The method should be called after a call to the populate method.
    def show_info(self):
        (d,h,m,s) = seconds_to_dhms(self.total_duration_seconds)
        text_duration= dhms_to_string((d,h,m,s))
        print(f'Videos: {self.videos_count}, Duration: {text_duration}')


def download_video(url):
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(url)

# Retrieves the video duration in seconds.
def get_video_duration(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        duration = info.get('duration')
        return duration
    
# Retrieves the playlist duration in seconds.
def get_playlist_duration(playlist_url):
    video_urls = get_video_urls(playlist_url)
    total_duration = 0 
    for url in video_urls:
        total_duration+= get_video_duration(url)
    return total_duration

def get_video_count(playlist_url):
    ydl_opts = {
        'dump_single_json': True,
        'extract_flat': 'in_playlist',
        'playlist_items': '1-',
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        return len(info['entries'])

def get_video_urls(playlist_url):
    ydl_opts = {
        'dump_single_json': True,
        'extract_flat': 'in_playlist',
        'playlist_items': '1-',
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        video_urls = [item['url'] for item in info['entries']]
    return video_urls

def seconds_to_dhms(seconds):
    seconds = int(seconds)
    d = seconds // (3600 * 24)
    h = seconds // 3600 % 24
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    return (d,h,m,s)

def dhms_to_string(dhms):
    (d,h,m,s) = dhms
    if d > 0:
        return '{:02d}d {:02d}h {:02d}m {:02d}s'.format(d, h, m, s)
    elif h > 0:
        return '{:02d}h {:02d}m {:02d}s'.format(h, m, s)
    elif m > 0:
        return '{:02d}m {:02d}s'.format(m, s)
    elif s > 0:
        return '{:02d}s'.format(s)
