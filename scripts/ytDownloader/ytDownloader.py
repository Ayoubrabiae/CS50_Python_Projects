from pytube import YouTube
from sys import argv, exit
import re

def main():
    video_link = get_video_link()
    video = get_video(video_link)
    print_video_info(video)
    download_video(video, './Videos')


def get_video_link():
    if len(argv) > 2:
        exit("Please enter only the video link")
    elif len(argv) < 2:
        exit("Please enter the video link")

    return argv[1]


def get_video(link):
    video = YouTube(link)
    return video


def print_video_info(video: YouTube):
    print(video.title)
    print(video.views, "views")
    print(video.length / 60, "minute")


def download_video(video: YouTube, path: str):
    video = video.streams.get_highest_resolution()
    video.download(path)
    print("Video downloaded successfly 😁")


main()