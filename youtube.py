from tkinter import filedialog

from pytube import YouTube
import tkinter as tk
from tkinter.filedialog import askdirectory

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.first()  # Get the highest resolution stream
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    print("teste antes")
    folder = filedialog.askdirectory()
    print("teste depois")
    if folder:
        print(f"Selected folder: {folder}")
    root.destroy()  # Destroy the tkinter window after selection
    return folder

if __name__ == "__main__":
    video_url = input("Please enter a YouTube URL: ")
    print("URL RECEBIDO")
    save_dir = open_file_dialog()
    if not save_dir:
        print("Invalid save location")
    else:
        print("Downloading...")
        download_video(video_url, save_dir)





