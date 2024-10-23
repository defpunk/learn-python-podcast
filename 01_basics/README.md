# Session 1 The Basics

The first episode of the podcast covers a lot of
ground. This folder contains a few simple programs so you can see
some of the basics in action. Read the description of each program,
take a look at the code in the file and then run it. Programming is
experimental learning so try writing your own versions and help the learning stick
by attempting the challenges

## hello_world_v1.py

The example files show some simple Python in action
hello_world_v1.py contains the traditional first program
making use of the print function to display a message.
Note we need to enclose the message in quotes so the computer knows
it's effectively one thing. The technical term for this is a string literal, that's a fixed, unchangeable string value.
If we missed the quotes the Program would throw a SyntaxError like the one shown
below. A SyntaxError in programming is like a grammatical mistake in a written sentence.
It occurs when the code you've written doesn't follow the set of rules, called syntax,
that the programming language expects. Just as grammatical mistakes can make it difficult to understand a sentence,
syntax errors can prevent your code from running correctly.

```commandline
  File "/Users/david/Projects/lbg/learn-python-podcast/01_basics/hello_world_v1.py", line 1
    print(Hello World)
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

## hello_world_v2.py

hello_world_v2.py extends the basic hello world to ask for a name using
the input function and assigns the result to the name variable
then prints a message it creates using the concatenation operator.
When the operands (fancy name for the things the operator is operating on)
to + are strings its the concatenation operator, when they're numbers its the
addition operator.

Joining strings together is such a common activity in programming,
most languages have this shortcut built in

## maths.py

maths.py shows Python's mathematical operators in action. Notice that the str function
is used to wrap each mathematical expression, this isn't part of the maths its being used
so we can print the question and answer all on the same line, we need to do this so that
both sides of the + being used for string concatenation are strings, if we remove the str function
from an example and run the file you'll see an error like this

```commandline
Traceback (most recent call last):
  File "/Users/david/Projects/lbg/learn-python-podcast/01_basics/maths.py", line 4, in <module>
    print('2 + 1 = ' + 2 + 1)
          ~~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Python is a dynamically-typed language, which means you don't need to specify the data type
of a variable explicitly. Behind the scenes Python determines the type of the variables and
expressions we create.

The basic types Python supports are:

* int: Represents integer numbers.
* float: Represents floating-point numbers.
* bool: Represents either a True or False value.
* str: Represents a string of characters.

There are a few others that we'll encounter in later episodes. Each function and operator has a combination of operands
or inputs it
supports, when the inputs we pass are not of the right type a TypeError will occur when the
program is run. Most of the time the types will sort themselves out, its not often we need
to perform the programming equivalent of comparing apples with oranges. When we do come across
TypeErrors we can easily fix them by using on of the `int(), float(), bool(), str()` functions
to convert things to the type we need.

This example uses # to denote that some of the code is comments for humans not source code. Use comments
sparingly the code tells other programmers what the code does save comments for explaining why something is happening.

## Challenges

Computer programming is practical craft, to get good you need to do some as well as read about
it try the challenges below, once you've worked on them for a while check out the answers here

- will add link later

### my_first_program.py

Create a simple program and run it. Follow the example of hello_world_v1.py and print a message
of your choice, an encouraging quote would be nice or if your stuck maybe this affirmation -
'I'm on my way to being a Python programmer'

### maths_challenge.py

Create a program to work out and print the answers to the following

* 893 plus 552
* 743 minus 342
* 66 multiplied by 44
* 73833 divided by 5 with a decimal point
* The remainder of 83538 divided by 7
* 7 to the power of 4

### double.py

Can you create a double.py program - it should ask the user to enter a number
and then print out a message telling them what the number doubled is. Hint you'll need to use the
int function to turn the users input into a number - the input function always returns a string




