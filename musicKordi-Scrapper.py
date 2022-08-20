import requests as rq
import re
from requests_html import HTMLSession
base_url = "https://musickordi.com/singer/%D8%B3%DB%8C%D9%88%D8%A7%D9%86-%DA%AF%D8%A7%DA%AF%D9%84%DB%8C.html"

def findLink(link):
    regex = r"(https:\/\/dl\.musickordi.com\/).*(mp3)"

    links = []
    matches = re.finditer(regex, link, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        # print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
        #    start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
        list.append(match.group(groupNum))
    return list
def downloadMusic(musicLink, name):
    response = rq.get(musicLink)
    open(name, "wb").write(response.content)
def call(url):
    s = HTMLSession()
    response = s.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'})
    audio = response.html.find('audio.default-player')
    print("-"*50)
    print("Downloading Started ...\n")
    for item in audio:
        music = item.find('source', first=True).attrs['src']
        print(music)
        #  downloadMusic(str(music), music[music.rindex("/") + 1:])
        print(music[music.rindex("/") + 1:],"")
def link_generator(page_number):

    print(f"page : #{page_number}")
    return base_url+"/page/{}/".format(page_number)



def fetchPages():
    s = HTMLSession()
    response = s.get(base_url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'})
    pages = response.html.find('div.pagination')
    list = pages[0].find('a')
    last_page=int(list[len(list)-2].text)

    for i in range(1,last_page):
        call(link_generator(i))


fetchPages()