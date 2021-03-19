from mcstatus import MinecraftServer
from os import system
from time import sleep
from tkinter import *
from win10toast import ToastNotifier
from time import sleep
from pypresence import Presence
import time



root = Tk()
root.geometry('300x100')

def button_command():
    entry1.get()
    text = entry1.get()
    root.quit()
    try:
        while True:
            client_id = '819553518234107904' #Put your client ID here
            RPC = Presence(client_id) 
            RPC.connect() 

            print(RPC.update(state="uzywajac MCmonitor", details="Monitoruje swoj serwer", large_image="logo", small_image=" ", large_text="Monitoruje swoj serwer MC!", buttons=[{"label": "Pobierz MC monitor!", "url": "https://google.com"}], start=time.time()))  # Set the presence
            time.sleep(15)  
            server = MinecraftServer.lookup(text)
            status = server.status()
            print("Na serwerze gra {0} graczy na pingu {1} ms".format(status.players.online, status.latency))
            sleep(2.00)
    except Exception:
        print("error")
        toaster = ToastNotifier()
        toaster.show_toast("Blad serwera!",
        "Blad serwera!",
        icon_path=None,
        duration=60)

entry1 = Entry(root, width = 20)
entry1.pack()

Button(root, text="Uruchom", command=button_command).pack()

root.mainloop()