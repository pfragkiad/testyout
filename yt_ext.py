from yt_dlp import YoutubeDL
import yt_dlp

# Retrieves the video duration in seconds.
def get_video_duration(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        duration = info.get('duration')
        return duration
    
# Retrieves the playlist duration in seconds.
def get_playlist_duration(playlist):
    video_urls = get_video_urls(playlist)
    total_duration = 0 
    for url in video_urls:
        total_duration+= get_video_duration(url)
    return total_duration

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