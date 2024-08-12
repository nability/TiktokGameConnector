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

def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)

    keyboard.release(key)
# Or, add it manually via "client.add_listener()"
async def on_comment(event: CommentEvent) -> None:
    print(f"{event.user.nickname} -> {event.comment}")
    # player 1

    if event.comment == '1':
        press_key('j')
    elif event.comment == '2':
        press_key('k')
    elif event.comment == '3':
        press_key('l')
    elif event.comment == '4':
        press_key('u')
    elif event.comment == '5':
        press_key('i')
    elif event.comment == '6':
        press_key('o')


client.add_listener(CommentEvent, on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()

# import keyboard
# import time

# def press_key(key):
#     keyboard.press(key)
#     time.sleep(0.1)

#     keyboard.release(key)

# while True:
