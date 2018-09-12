import requests
import time
import os

URL = "YOUR-URL"

# The notifier function
def notify(title, message):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(message)
    i = '-appIcon {!r}'.format("path/to/icon.png")
    os.system('terminal-notifier {}'.format(' '.join([m, t, i])))

def Ok():
    # Calling the function
    notify(title    = 'Success!',
           message  = 'Your GitHub Pages site has been published.')

global prev
prev = ""

first = True

while True:
    url = URL
    response = requests.get(url)
    text = response.text

    if (text != prev):
        if (first == True):
            first = False
        else:
            # Change detected
            print("Update Detected")
            Ok()
        prev = text

    time.sleep(1)
