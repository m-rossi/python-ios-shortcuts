import json
import sys
from urllib.parse import quote

import youtube_dl
import webbrowser


def main():
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(sys.argv[1], download=False)

    audio = {}
    video = {}
    for f in info['formats']:
        # determine filesize of media, if possible
        if f["filesize"] is not None:
            filesize = f' - {f["filesize"] / 1024**2:.0f} MB'
        else:
            filesize = ''
        
        # extract information about audio media
        if f['acodec'] != 'none':
            key = f'{f["ext"]}@{f["abr"]:.0f}{filesize}'
            audio[key] = {
                'url': f['url'],
                'ext': f['ext'],
            }
            
        # extract information about video media
        if f['acodec'] != 'none' and f['vcodec'] != 'none':
            key = f'{f["width"]}x{f["height"]}.{f["ext"]}@{f["tbr"]:.0f}{filesize}'
            video[key] = {
                'url': f['url'],
                'ext': f['ext'],
            }
            
    print(f)

    # return dicts back to shortcuts
    if sys.argv[-1].startswith('shortcuts-production://'):
        url = sys.argv[-1].replace('shortcuts-production', 'shortcuts')
        print(url)
        url += f'?x-source=Pythonista3'
        url += f'&title={quote(info["title"])}'
        url += f'&audio={quote(json.dumps(audio))}'
        url += f'&video={quote(json.dumps(video))}'
        webbrowser.open(url)

if __name__ == '__main__':
    main()

