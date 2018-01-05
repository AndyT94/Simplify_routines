"""
A program for web scraping the site mangestream.com and then opening the links
to manga that is preferred to read on a specific release date
"""
__author__ = 'Andy Truong'

from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import sys

def parse_html(website):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    header = {'User-Agent':user_agent,}
    request = urllib.request.Request(website, headers=header)
    response = urllib.request.urlopen(request)
    html = response.read()
    return BeautifulSoup(html, "lxml")

def is_pref_manga(manga_list, text):
    for manga in manga_list:
        if manga in text:
            return True
    return False

def main(args):
    if len(sys.argv) > 1:
        filter = (' ').join(sys.argv[1:])
    else:
        filter = 'today'

    pref_manga = {
        'Akatsuki no Yona',
        'All Out',
        'Black Clover',
        'Boruto',
        'Dr. Stone',
        'Grashros',
        'Haikyuu',
        'My Hero Academia',
        'One Piece',
        'One-Punch Man',
        'Robot x Laserbeam',
        'Shokugeki no Souma',
        'The Seven Deadly Sins',
        'Tokyo Ghoul:re',
        'Ubel Blatt',
        'Vinland Saga'
        }
    website = 'https://readms.net/'

    parsed_html = parse_html(website)
    latest_manga = parsed_html.body.find('ul', attrs={'class':'new-list'})
    for manga in latest_manga.find_all('li'):
        date = manga.find('span')
        if filter in date.text.lower() and is_pref_manga(pref_manga, manga.find('a').text):
            webbrowser.get('firefox.exe %s').open(website + manga.find('a').get('href'))

if __name__ == '__main__':
    main(sys.argv[1:])
