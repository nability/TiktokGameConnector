import keyboard
import time
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent
from TikTokLive.events import GiftEvent

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@tntgaming.mc")

# Listen to an event with a decorator!
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to @{event.unique_id} (Room ID: {client.room_id}")

def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    # Streakable gift & streak is over
    if event.gift.streakable and not event.streaking:
        print(f"{event.user.unique_id} sent {event.repeat_count}x \"{event.gift.name}\"Rose")
        if event.gift.name == 'Rose':
            press_key('r')
    # Non-streakable gift
    elif not event.gift.streakable:
        print(f"{event.user.unique_id} sent \"{event.gift.name}\"Rose")

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()