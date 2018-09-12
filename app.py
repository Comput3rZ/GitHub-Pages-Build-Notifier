import requests
import time
import os

# The notifier function
def notify(title, message):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(message)
    i = '-appIcon {!r}'.format("/Users/bensommer/Local/Sites/Notifier/icon.png")
    os.system('terminal-notifier {}'.format(' '.join([m, t, i])))

def Ok():
    # Calling the function
    notify(title    = 'Success!',
           message  = 'Your GitHub Pages site has been published.')

global prev
prev = ""

first = True

while True:
    url = "https://school.bensommer.co.uk"
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
