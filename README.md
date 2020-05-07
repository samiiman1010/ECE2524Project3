# ECE2524Project3
Mastermind Implementation in Python

The instructions to the game are included in the code as I thought that inclusion
seemed necessary for users who may not be familiar with Mastermind.  Thusly, I
will not talk so much about the game Mastermind itself, but rather the code
involved.

As you can tell, this program is really not overly complicated and I could
certainly modify it to make it more complex (more on that further down).  
Essentially, my program gives a brief introduction and then asks if the
user wants to read the rules.  This is probably a good idea anyway so the user
knows which colors are included in the game.

I then create an array that holds the color sequence for one iteration of the
game using a Python algorithm that randomly selects an element out of an array
containing all of the colors used in the game.

The player then uses the command line to type in their color sequence; this is
done one at a time.  The program then compares the user guesses to the color
sequence and gives the user feedback on how they did with their guesses.

I had two primary issues with this project: this is the first time that I've
used Python and I also didn't have the time I wanted to write this to the
extent I wanted to.  I considered adding a harder mode that will only tell
you if you chose correct colors, but not if it's in the right place in the
sequence.  I also intended to spice up the output messages so you don't see
the same ones all the time (this wouldn't be hard, it would just take longer
than I have right now).

I really wish I had spent more time on this; unfortunately, Applied Software
Design ate up significantly more time than I anticipated during this last week
of classes.  In fact, my next play tonight is to finish a concurrent quicksort
algorithm with multithreading...

I understand that the intent of this project was to get practice with GitHub
(and maybe get some Python experience); rest assured Applied has kept me very
familiar with GitHub and I can share other, more in depth, projects that I've
done if you desire proof that I know how to use it well.
