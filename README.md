# jslauncher
Joystick centralized multi-python scripts launcher

# What is this for ?
The idea is simple. Using a wireless joystick (Bluetooth/2.4G) you can switch between multiple
Python scripts from inside the launcher script called jslauncher.py in this directory.
For simple demo, there are two python scripts:
- codeone.py
- codetwo.py

# How to use ?
Just run jslauncher by using Python 2 command

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

This will run your Python script every time the Raspberry Pi reboots. If you want your command to be run in the background while the Raspberry Pi continues starting up, add a space and & at the end of the line, like this:

```
@reboot python /home/pi/myscript.py &

```
