# BaseRobotFall2022
Common team python BaseRobot class

# WARNING!
Please do not make any edits in any of these four existing files! Almost certainly editing them will not do
what you think it does.
This includes
- base_robot.py
- spike.py
- spike/control.py
- spike/operator.py

Those files are only here to help write programs in VS Code. Editing them will not change how your 
programs run. They provide intellisense hints and that is it. If they are not present, when you are 
writing code the code completion and the intellisense popups will not work. VS Code will also think 
you have coding errors in your program, when in fact you may not. In other words, just leave those 
files alone.

base_robot.py
-------------
base_robot.py is a special file. This is the BaseRobot class. It contains functions and properties 
for FLL Team 24277's Base Robot.

This file must be uploaded to the hub in order for it to work. Use ampy
https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy

To upload the file, use a command like this

    C:\>ampy -p COM6 put "C:\Users\Me\Documents\LEGO Education SPIKE\TestProj\base_robot.py" /base_robot.py

You will need to know what COM port your computer sees the hub. On windows, go
to 

    Settings-> Bluetooth & other devices -> More bluetooth options 

to find the COM port

If you are using USB instead of Bluetooth, I think the procedure is similar, but I have never tried it.

# Instructions
You will write your programs to move the robot and to do things. VS Code will give you hints 
along the way and will help you to make sure spelling is correct. Yes, spelling matters!!

First, make a folder where you want to keep your files. Perhaps Documents\FLL.
Inside there, clone this repository and you will then have

    Documents\FLL\BaseRobotFall2022
    ├── spike.py *
    ├── spike\
    │   ├── control.py *
    │   └── operator.py *
    ├── base_robot.py *
    ├── LICENSE
    ├── README.md
    ├── main.py @@
    ├── mission1.py @@
    ├── AnyOtherProgramsYouWrite.py @@



In there you will make your mission program(s), which you can call just about anything, such as
- main.py
- mission1.py
- master.py
- MissionImpossible.py
- AnythingYouWant.py

etc.


Again, do not edit or delete any of the files with asterisks!
You will create and edit the files with the @@ marks.

Begin your programs with these lines (use mission1.py as a template):

    import base_robot
    import sys
    from spike.control import wait_for_seconds, wait_until, Timer
    from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

    br = base_robot.BaseRobot()

Some generic programming, python and VS Code comments:

Python:
In python, indenting also matters. Unless you are writing loops or using if/then 
statements, all of your code MUST start in the first column of each line. Also,
you can use the line continuation "\\" like that import line above, in which case
the indenting doesn't matter for the continued lines.

VS Code configuration:
Install the extension LEGO SPIKE Prime / MINDSTORM Robot Inventor Extension
Connect your hub to your computer (either BlueTooth or USB)
Open the SPIKE app on your computer and connect to the hub. Install any updates 
that are required.
Back in VS Code, in the lower left corner, click on "LEGO Hub: Disconnected" 
to get it to connect. At the top of the screen, you will see options for ports.
It can be difficult to figure out which port to use, so you may have to try them 
all.

Programming:
When you are writing your code, remember, to python, your robot's name 
is "br" (see that line up above that starts with br =? That's where your robot 
got its name). Try typing "br." (without the quotation marks) and see what hints 
VS Code gives you. Also try "br.driveMotors.". There you will see your familiar 
"move_tank" and other ways to move the robot. You can also use some of the special 
programs that your teammates have written such as GyroDrive. As you write more 
code, you will see all the ways that VS Code tries to help you.
