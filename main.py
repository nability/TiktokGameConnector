import pyautogui
import time
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@nabiruuuuuu")


# Listen to an event with a decorator!
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to @{event.unique_id} (Room ID: {client.room_id}")


# Or, add it manually via "client.add_listener()"
async def on_comment(event: CommentEvent) -> None:
    print(f"{event.user.nickname} -> {event.comment}")
    # player 1
    if event.comment == 'w':
        pyautogui.typewrite('w')
    elif event.comment == 's':
        pyautogui.typewrite('s')
    elif event.comment == 'a':
        pyautogui.typewrite('a')
    elif event.comment == 'd':
        pyautogui.typewrite('d')
    elif event.comment == 'f':
        pyautogui.typewrite('f')
    elif event.comment == 'g':
        pyautogui.typewrite('g')
    elif event.comment == 'h':
        pyautogui.typewrite('h')
    elif event.comment == 'r':
        pyautogui.typewrite('r')
    elif event.comment == 't':
        pyautogui.typewrite('t')
    elif event.comment == 'y':
        pyautogui.typewrite('y')
    elif event.comment == 'u':
        pyautogui.typewrite('u')
    # player 2
    elif event.comment == 'up':
        pyautogui.typewrite('up')
    elif event.comment == 'down':
        pyautogui.typewrite('down')
    elif event.comment == 'left':
        pyautogui.typewrite('left')
    elif event.comment == 'right':
        pyautogui.typewrite('right')
    elif event.comment == 'k':
        pyautogui.typewrite('k')
    elif event.comment == 'l':
        pyautogui.typewrite('l')
    elif event.comment == ';':
        pyautogui.typewrite(';')
    elif event.comment == 'i':
        pyautogui.typewrite('i')
    elif event.comment == 'o':
        pyautogui.typewrite('o')
    elif event.comment == 'p':
        pyautogui.typewrite('p')

client.add_listener(CommentEvent, on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()

