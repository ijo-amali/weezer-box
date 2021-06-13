# weezer-box
Guide/Source code to make a weezer box of your own

-------------
## Construction
You'll need:
* Raspberry Pi (any model is fine)
* Pushbutton
* Small box
* Wires

Place the raspberry pi in the box so that the power plug and aux plug are facing the wall, and so that it's steady in the box and won't move. (Alternatively, you can tape/nail it down.) 
Cut holes in the box so these are accessible from outside the box. Cut a hole in the top of the box for the button and put it through.

Put a wire in GPIO pin 2 and in a ground pin (a pin guide can be found [here](https://pinout.xyz/)). Connect the other ends to the button. (Optionally, put a power bank into the box for maximum portability.)

It should look something like this!
![Image of completed build](https://user-images.githubusercontent.com/33301953/121628800-32d89980-ca37-11eb-822e-f8c4fa4e2ec1.png)

------------
## Software

Download the source code (it's just one python file) and install the `gpiozero` python library if you haven't already:
```
sudo pip install gpiozero
```
Now, create a directory where you store the audio files (make sure that ***only the audio files are in this directory***), and put as many Weezer songs as you want in there. Go into `weezer.py` and change line 7 to the actual path to that directory.
Now, you can run it from the command line:
```
python3 weezer.py
```
But you might want to run it right when it boots up so you don't have to do that. There are several ways to do that, one of which could be to use `crontab`.
To do this, type `crontab -e` and select a text editor. At the bottom of the file, add:
```
@reboot /usr/bin/python3 /path/to/weezer.py
```
(replacing `path/to/weezer/py` with the actual path)
