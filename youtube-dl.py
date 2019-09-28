import sys
from urllib.parse import quote

import youtube_dl
import webbrowser


def main():
    with youtube_dl.YoutubeDL({'format': 'best'}) as ydl:
        info = ydl.extract_info(sys.argv[1], download=False)

    if sys.argv[-1].startswith('shortcuts-production://'):
        url = f'{sys.argv[-1]}?x-source=Pythonista3&filename='
        url += quote(f'{info["title"]}.{info["ext"]}')
        url += '&url='
        url += quote(info["url"])
        webbrowser.open(url)

if __name__ == '__main__':
    main()

