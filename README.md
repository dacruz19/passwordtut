# passwordtutorial

Now, lets say for some odd reason, you want to add a password to your python script, in this repository I will show you how to if you didn't already know.

Firstly, import the `getpass` python module, which is a standard module so no need to install it.
The functionality of the ``getpass`` module is to help get password input which makes it ever so more useful.

Next, wherever you want in the code, from the ``getpass`` module call the ``getpass()`` function to actually recieve the input.
The ``getpass()`` function works similarly to the ``input()`` so to call it all you may need is something like this:
```getpass.getpass(prompt)```
So now, to actually get the input from the user, you can just store it into a variable like ``password`` which then gives you the input.

Final Code:

```
import getpass

password = getpass.getpass("Password: ")
```

Try it out for yourself. Try experimenting like having a certain password then comparing it with the input before a certain block of code is executed (my example is in example.py).
