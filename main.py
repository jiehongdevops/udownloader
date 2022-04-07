from pytube import YouTube
import datetime
if datetime.datetime.today()<datetime.datetime.strptime("20220415","%Y%m%d"):
    link = input("Enter the youtube link: ")
    try:
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    outName = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    print()
    resList = ['1080p', '720p']
    for i in resList:
        resYT = yt.streams.filter(res=i)
        if len(resYT) > 0:
            resYT.first().download(output_path="./",filename=f"{outName}.mp4")
