from mcstatus import MinecraftServer
import time
from os import system

server_address = input("Server address: ")
try:
    while True:
        print("There are "+str(MinecraftServer.lookup(server_address).status().players.online)+" players on "+server_address+". ^C to exit")
        time.sleep(2)
        try:

            print(RPC.update(state="uzywajac MCmonitor", details="Monitoruje swoj serwer", large_image="logo", small_image=" ", large_text="Monitoruje swoj serwer MC!", buttons=[{"label": "Pobierz MC monitor!", "url": "https://google.com"}], start=time.time()))  # Set the presence
            time.sleep(8)  
        except Exception:
            print("program nie ma polaczenia z discordem, aby pomoc nam w promocji programu uruchom aplikacje discord")
except Exception:
    print("error")
    system('notify-send "Error... Blad z serwerem!"')