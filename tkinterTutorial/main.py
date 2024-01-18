import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=progressFunction)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        video.download()
        finishLabel.configure(text="Download finalizado")
    except:
        finishLabel.configure(text="Erro ao fazer download", text_color="red")
    
def progressFunction(stream, chunk, bytes_remaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytes_remaining
    percentage_of_completion = bytesDownloaded / totalSize * 100
    per = str(int(percentage_of_completion)) + "%"
    pPercentage.configure(text=per)
    pPercentage.update()

    #update progress
    progressBar.set(float(percentage_of_completion) /100)


#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#Adding ui elements
title = customtkinter.CTkLabel(app, text="Coloque um link do youtube")
title.pack(padx = 10, pady = 10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url_var)
link.pack()

#Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(padx = 10, pady = 10)

#Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack(padx = 10, pady = 10)

progressBar = customtkinter.CTkProgressBar(app, width=350, height=20, progress=0)
progressBar.set(0)
progressBar.pack(padx = 10, pady = 10)

#Download button
download = customtkinter.CTkButton(app, text="Download", command = startDownload)
download.pack(padx = 10, pady = 10)

#RUn app
app.mainloop()