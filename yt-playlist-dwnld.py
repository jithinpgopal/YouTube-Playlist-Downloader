##########################################################################################################################
#                                                                                                                        #
#  	************************Code for downloading videos from a public youtube playlist********************************   #
#	PlayList format				:"https://www.youtube.com/playlist?list=PLVjwdZylAT2lbiWNAdFssOhf2obBIEU5Y"              #
#	Maximum file numbers 		: 25 - This can be changed in the array size "links"                                     #
#	Author						: Jithin P Gopal trijithu@gmail.com	                                                     #
#	Version						: 1.0                                                                                    #
#	                                                                                                                     #
##########################################################################################################################

from pytube import YouTube
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pathlib import Path
from builtins import str
import pytube

links=[None]*25
dpath=input("Enter the target path")
print("PlayList format: https://www.youtube.com/playlist?list=PLVjwdZylAT2lbiWNAdFssOhf2obBIEU5Y")
plst=input("Enter the playlest in the above format")


opener=urllib.request.build_opener()
# opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
# opener.addheaders=[('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')]
urllib.request.install_opener(opener)


def ydnld(url):
    try:
        yt = YouTube(url)
        #print(yt)
        try:
            video = yt.get('mp4','1080p')
            print("1080p Available")
        except pytube.exceptions.DoesNotExist:
            try:
                video = yt.get('mp4','720p')
                print("720p Available")
            except pytube.exceptions.DoesNotExist:
                video = yt.get('mp4','360p')
                print("360p Available")
        myfile2=Path(dpath+"/" + yt.filename+".mp4")
        print("Downloading " + yt.filename)
        if myfile2.is_file()== False:
            print(str(myfile2))
            video.download(dpath)
            print("Downloaded ")
        else:
            print("File Exist")
    except Exception as f:
        print (str(f))
   

def dwplaylist(url):
    i = 0;
    req = Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
    page = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(page,"lxml")
    playlist=url[38:]
    print("PlayList is : " + playlist)
    for line in soup.find_all('a'):
        #print (line)
        link = line.get('href')
        lnk = str(link)
        if (lnk.find(playlist)!= -1)and len(lnk) < 90: 
            i=i+1       
            lnk = ("https://www.youtube.com"+lnk)
            print("link  is " + lnk)
            ydnld(lnk)
    print("Tolal Links " + str(i))
    
dwplaylist(plst)   