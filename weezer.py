from gpiozero import Button
from subprocess import call
import os, random, signal

# Directory that the songs are stored in
song_directory = "/home/pi/Dev/projects/weezer-button/songs"
button = Button(2, hold_time=5)
is_playing = False

# Define function when button is pressed
def button_press():
    global is_playing
    print(is_playing)
    if is_playing == False:
        # Choose a random song
        song = random.choice(os.listdir(song_directory))
        # Play it
        call("omxplayer -o local %s/%s &" % (song_directory, song), shell=True)
        print(song)
        is_playing = True
    elif is_playing == True:
        print('Stop')
        # Stop song
        call("killall omxplayer.bin", shell=True)
        is_playing = False

def shutdown():
    print("~~~~~SHUTTING DOWN~~~~~")
    button.close()
    call("sudo poweroff", shell=True)

# When button is released, execute function
button.when_pressed = button_press
# When button is held, execute hold function
button.when_held = shutdown

print('Ready.')

try:
    # Pause program execution
    signal.pause()
except:
    # Free gpio
    button.close()
