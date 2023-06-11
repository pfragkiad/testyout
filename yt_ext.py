import yt_dlp

#hint code here: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp

import threading

class PlaylistVideo:
    def __init__(self, entry):
        self.id = entry["id"]
        self.url = entry["url"]
        self.title = entry["title"]
        self.description = entry["description"]
        self.duration_seconds = entry["duration"]
        self.view_count = entry["view_count"]

    def __str__(self):
        return f'{self.title} ({self.id})'

class Playlist:
    def __init__(self, id, populate_now = False):
        self.id = id
        if populate_now:
            self.update_info()

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def update_info(self):
        ydl_opts = {
            'dump_single_json': True,
            'extract_flat': 'in_playlist',
            'playlist_items': '1-',
            'skip_download': True,
        }
        baseurl = "https://www.youtube.com/playlist?list="
        url = f'{baseurl}{self.id}'
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            self.info = ydl.extract_info(url, download=False)
        
        self.id = self.info["id"]
        self.url = self.info["webpage_url"]
        self.title = self.info["title"]
        self.availability = self.info["availability"]
        self.description = self.info["description"]
        self.modified_date = self.info["modified_date"]
        self.view_count = self.info["view_count"]

        self.videos_count = self.info["playlist_count"]
        self.videos = list(map(lambda e : PlaylistVideo(e),self.info['entries']))
        self.total_duration_seconds = sum(v.duration_seconds for v in self.videos)
    
    def get_partial_duration(self,from_index):
        return sum(v.duration_seconds for v in self.videos[from_index-1:])


    # def get_url(self):
    #     baseurl = "https://www.youtube.com/playlist?list="
    #     return f'{baseurl}{self.name}'

    # def update_video_urls(self, get_durations = True):
    #     url = self.get_url()
    #     self.videos = get_video_urls(url)
    #     self.videos_count = len(self.videos)
    #     #or: self.total_duration_seconds = get_playlist_duration(url)
    #     if get_durations:
    #         self.total_duration_seconds = sum(get_video_duration(v) for v in self.videos)

    def download(self):
        #should control status here BETTER - and the naming of invalid characters
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

def build_playlist_url(playlist_name):
    baseurl = "https://www.youtube.com/playlist?list="
    return f'{baseurl}{playlist_name}'

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

def seconds_to_dhms_string(seconds):
    dhms = seconds_to_dhms(seconds)
    return dhms_to_string(dhms)

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

def analyze_ytdlp(playlist_name):
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