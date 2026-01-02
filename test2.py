import yt_dlp as yt

def auUrl(name):
    print(name)
    ytopt = {"quiet":True , "skip_download":True}
    with yt.YoutubeDL(ytopt) as d:
        info = d.extract_info(f'ytsearch1:{name}',download = True)
        return info["entries"][0]["requested_downloads"]
    

name = "creep"
info = auUrl(name)[0]
for i in info:
    print(i,'\n',info[i])
    print('=======================================================')

# info["entries"][0]["requested_formats"][0]["url"]
# requested_formats 
# requested_downloads