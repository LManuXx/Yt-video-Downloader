import os
import pandas as pd
from pytube import YouTube

output_folder = './videos'

excel_file = './lista_videos.xlsx'

df = pd.read_excel(excel_file)

for i, row in df.iterrows():
    try:
        video_url = row['URL']
        yt = YouTube(video_url)
        
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path = output_folder)
        print("Video descargado correctamente")
    
    except Exception as e:
        print("Error al descargar el video")


