import subprocess
import os

#UserInputs:
ytDlpExeName = "yt-dlp.exe"
ffmpegPath = "./ffmpeg/ffmpeg.exe"
outputFolder = "./downloads/"
nameArgs = "%(title)s-%(id)s.%(ext)s"
#-----------------------------------------------------------------



outputPathFull = outputFolder + nameArgs

def askLink():
    global link
    link = input('Paste Youtube / SoundCloud Link here (q to quit): ')



def askFormat():
    print("1: mp4")
    print("2: mp3")
    print("3: m4a")
    print("4: select from all available formats")
    print("q: Quit")
    global dlFormat
    dlFormat = input("select a file format [1, 2, 3, 4, q]: ")


def downloadMP3():
    subprocess.run([ytDlpExeName, "--format=bestaudio", "--extract-audio", "--audio-format=mp3", "--audio-quality=160K", "--ffmpeg-location=" + ffmpegPath, link, "-o"+outputPathFull])

def downloadM4A():
    subprocess.run([ytDlpExeName, "--ffmpeg-location=" + ffmpegPath, "-f ba[ext=m4a]", link, "-o"+outputPathFull])

def downloadMP4():
    subprocess.run([ytDlpExeName, "--ffmpeg-location=" + ffmpegPath, "--recode=mp4", link, "-o"+outputPathFull])


def FormatsScreenDownload():
    subprocess.run([ytDlpExeName, "-F", link])
    ID = input("Input a ID from the list above: ")
    subprocess.run([ytDlpExeName, "-f"+ID, link])



def download():

    if dlFormat == str(1):
        downloadMP4()
    elif dlFormat == str(2):
        downloadMP3()
    elif dlFormat == str(3):
        downloadM4A()
    elif dlFormat == str(4):
        FormatsScreenDownload()
    elif dlFormat == "q":
        exit()
    else: 
        print("Unknown action. Please enter one of the numbers from 1-5.")
        askFormat()


while 1 == 1:
    askLink()
    if link == "q": exit()
    os.system('cls')

    askFormat()
    
    download()
    print("\n \n \n \n \n \n \n \n \n")
