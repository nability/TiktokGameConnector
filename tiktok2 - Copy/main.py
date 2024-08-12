import keyboard
import time
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@rapspoint_real")

# Listen to an event with a decorator!
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to @{event.unique_id} (Room ID: {client.room_id}")
def hold_key(key):
    keyboard.press(key)
    time.sleep(0.5)
    keyboard.release(key)

def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

# Or, add it manually via "client.add_listener()"
async def on_comment(event: CommentEvent) -> None:
    print(f"{event.user.nickname} -> {event.comment}")

    # player 1
    if event.comment == 'w':
        hold_key('w')
    if event.comment == 's':
        hold_key('s')
    if event.comment == 'a':
        hold_key('a')
    if event.comment == 'd':
        hold_key('d')
    if event.comment == 'f':
        press_key('f')
    if event.comment == 'g':
        press_key('g')
    if event.comment == 'h':
        press_key('h')
    if event.comment == 'r':
        press_key('r')
    if event.comment == 't':
        press_key('t')
    if event.comment == 'y':
        press_key('y')
    if event.comment == 'u':
        press_key('u')
# player 2
    if event.comment == 'up':
        hold_key('up')
    if event.comment == 'down':
        hold_key('down')
    if event.comment == 'left':
        hold_key('left')
    if event.comment == 'right':
        hold_key('right')
    if event.comment == 'k':
        press_key('k')
    if event.comment == 'l':
        press_key('l')
    if event.comment == ';':
        press_key(';')
    if event.comment == 'j':
        press_key('i')
    if event.comment == 'o':
        press_key('o')
    if event.comment == 'p':
        press_key('p')
    if event.comment == '[':
        press_key('[')

client.add_listener(CommentEvent, on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()

# # import keyboard
# # import time

# # def press_key(key):
# #     keyboard.press(key)
# #     time.sleep(0.1)

# #     keyboard.release(key)

# # while True:
