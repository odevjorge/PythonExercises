from time import sleep
import emoji

for c in range(10, -1, -1):
    print(f'{c:02}')
    sleep(1)

print(emoji.emojize("Booommm :fireworks:", language='en', variant="emoji_type"))

