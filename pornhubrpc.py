from pypresence import Presence 
import time

start = int(time.time())
client_id = "1076087940662448168"
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image = "large_image",
        large_text = "Pornhub",
        small_image = "small_image",
        small_text = "watching",
        details = "Jerking off to Among Us porn",
        state = "Pornhub",
        start = start,
    )
    time.sleep(60)