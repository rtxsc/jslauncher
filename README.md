# jslauncher
Joystick centralized multi-python scripts launcher

# What is this for ?
This is something like a front page of a website, or an operating system for a robot. Since robot could have
multiple operating modes, let say, automatic and manual mode. This could come in handy as you could switch between 
the 2 modes by simply pressing the button on your joystick.

The idea is simple. Using a wireless joystick (Bluetooth/2.4G) you can switch between multiple
Python scripts from inside the launcher script called jslauncher.py in this directory.

# Demo code
For simple demo, there are 3 python scripts in this directory:


- [x] [`jslauncher.py`](jslauncher.py)  
- [x] [`codeone.py`](codeone.py)  
- [x] [`codetwo.py`](codetwo.py)  

Use `Select` button to switch between scripts (mode)
Use `Start` button to run the selected script
Use `Home` button to return to launcher from within `codeone.py` or `codetwo.py`

# How to use ?
Just run jslauncher by using `Python 2` command
```
python jslauncher.py

```
Since the purpose of this code is to let the user switch between few different python scripts without
having to access the terminal, it is recommended to run this code at boot in the background assuming
that you are building a multi-purpose robot.

# Run at boot with crontab
Run crontab with the -e flag to edit the cron table:
```
crontab -e
```

The first time you run `crontab` you'll be prompted to select an editor; 
if you are not sure which one to use, choose `nano` by pressing `Enter`.

# Run jslauncher at boot (background)

This will run your Python script every time the Raspberry Pi reboots. If you want your command to be run in the background while the Raspberry Pi continues starting up, add a space and `&` at the end of the line, like this:

```
@reboot python /home/pi/jslauncher/jslauncher.py &
```
# Things to note

![joystick](/CF542661-D6C5-4A50-9768-753CD4F24E8E.jpg)

- The button mapping might need to be changed if you're using a different type of controller (not similar to the one used in this demo)

