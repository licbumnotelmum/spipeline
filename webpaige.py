import yt_dlp
import os

def getUrl(song_name):
    print(song_name)
    ydl_opts = {
        "quiet": True,
        "skip_download": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{song_name}", download=True)
        return(info["entries"][0]["requested_formats"][0]["url"])
    print("done")  


def downloadCunt(names,dirPath = "/home/onealji/Music/"):      #change the default dir path before running the program
    import subprocess
    for i in names:
        heder = i["name"]+'-'+i['artists']
        heder = cleanString(heder)
        fileName = heder +'.mp3'

        if (fileName in os.listdir(dirPath) ):
            print("skipped ",fileName)
            continue

        if (heder =="-"):
            continue

        filePath = dirPath+fileName
        print(filePath)

        url = getUrl(i["name"]+' '+i['artists'])

        subprocess.run(
            f'n | ffmpeg -i \"{url}\" -vn -acodec mp3 \"{filePath}\"',
            shell=True
            )

        print("written ======= "+filePath)

def cleanString(x):
    excs=('"','\'','.','\\','/',"$")
    nx=''
    for i in x:
        if i in excs:
            continue
        nx=nx+i
    return nx
def isCleaned(x):
    excs=('"','\'','.','\\','/')
    for i in x:
        if i in excs:
            return True
    return False