# Session 2 Selection

Now and again you'll write programs that run from start to finish with needing to adjust
for circumstances. However, these are rare cases,most of the time you'll need to tell
the computer how to handle different situations. Python has a few constructs

## 01_basic_if.py

This is a shows the syntax of the if condition, the if keyword followed by a boolean expression,
in this case we've used the boolean literal True (capitalisation is important), the condition is
followed by a colon: - Miss the colon and when you run the program you'll get SyntaxError, as we
saw last time don't follow the rules of the language and the interpreter won't know what to do

```python
if True:
    print('True is always true')
```

NB indentation is important. Python saves the programmer from typing symbols
just to help the computer understand your code. Preferring indentation, if your line ends with a colon then
Python will expect the next line to be indented. If you forget this you'll see an error like the one below when you
execute your program.

```commandline
  File "/Users/david/Projects/lbg/learn-python-podcast/02_selection/01_basic_if.py", line 2
    print('True is always true')
    ^
IndentationError: expected an indented block after 'if' statement on line 1
```

## 02_hello_world.py

If True: is always true so we could remove that leaving the print statement and have the same effect.
The second example shows a more typical use of if, taking different action depending on the value of
a variable (this is something that can change). When the user inputs John we print one message, all other
values get the second message that's defined in the else: block. Recall that the input function always returns a string
which is why we can compare it to the String literal 'John'

```python
name = input('What is your name? ')
if name == 'John':
    print("Hello John, that's a great name")
else:
    print('Hello ' + name)
```

Note you can use either single quotes ' or double quotes to
enclose a string literal the preference is for single quotes but when you
need to include a ' in the text use ".

## 03_generation.py

This example shows off a different kind of boolean condition, less than <
and introduces the elif keyword - short for else if.

The program asks the user
to enter their birth year, that's the input function, then converts it to a integer using
int - remember that input function always returns (gives us) a value with the string type
so we need to convert it to use it as a number. When Python evaluates an expression, it follows a specific set of rules
called operator precedence. Parentheses (()) have the highest precedence, so expressions inside
parentheses are evaluated first. Within the parentheses, operators are evaluated according to their precedence.
After evaluating expressions inside parentheses, Python evaluates any remaining operators in the
expression from left to right.

When the program runs the
computer will check each of the conditions in turn, working from top to bottom and execute
the code that follows the matching condition. If the if condition nor any of the elif conditions are
satisfied the else condition will run just like in the if else example of 02_hello_world.py

## 04_reverse_generation.py

In some cases a long ladder of if / elif clauses is better expressed as a
match statement with case statements. This shows a typical case
taking some action based on the value of a variable. Similar to
the elif example the computer will execute the code block in the first case
that matches, in this example we have used string literals but Python will support
the use of conditional cases.

```python
match generation:
    case 'Silent Generation':
        print('born before 1945')
    case 'Baby Boomer':
        print('born between 1945 and 1963')
    case 'Generation X':
```

## 05_generation_match_style.py

This shows 03_generation.py rewritten to use the match
syntax, the case is more complex now with an if and an underscore.
The underscore (_) in the match statement serves as a placeholder for the matched value,
_ automatically refers to the value matched by the expression, which in this case is birth_year.
In this case it wasn't an improvement over the 03_generation.py version however sometimes
match can end up with an easier to read version of the code. Once you get passed the tutorial stage you'll
find that code is read more often than it's written so making things easier to understand for people
looking at your code in future even if that's only going to be doing is one aspect of good programming practice.

```python
match birth_year:
    case _ if birth_year < 1945:
        print('Silent Generation')
    case _ if birth_year < 1964:
        print('Baby Boomer')
    case _ if birth_year < 1979:
        print('Generation X')
```

## 06_hello_world_v2.py

This version of hello world introduces Python's conditional expression, you may come across it being called ternary
operator.
It's like a shortcut if that's useful if there are only two options
and the condition to choose between them is succient.
It's used as follows value to return when condition is true if conditional expression else value if condition is false
Used in the right place it can make your code simpler and therefore easier
to understand. The two programs below will have exactly the same
effect. Which do you find easier to read?

```python
name = input('What is your name? ')
if name == 'John':
    print("Hello John, that's a great name")
else:
    print('Hello ' + name)
```

```python
name = input('What is your name? ')
output = "John, that's a great name" if name == 'John' else name
print('Hello ' + output)
```

## 07_logic.py

In these examples we've used basic conditional statements, but in real
life the rules we need to code are more complex.
Wherever you've seen an expression like `name == 'John'` you can have something
like `name == 'John' or name == 'Sarah'`. We need to repeat the name == section
as the interpreter isn't smart enough to understand `name == 'John' or 'Sarah'`
each side of the or needs to return True or False. Python also has an and operator and
not. It's possible to combine the operations to create complex conditions when you do
this it's a good idea to use parenthesis to ensure the code runs as you intend.
Without parentheses, It's essential to understand the order in which Python evaluates logical operators
(not, and, or) to ensure the desired outcome.

```python
a = True
b = False
c = False

print(a and b)
print(a or b)
print(not a)
print((a and b) or not c)
```

## Challenges

1. Write your own version of 03_generation.py that uses an if elif ladder rather than the match statement
2. Implement a simple text-based calculator using logical operators and conditional statements. Create a program that
   takes two numbers and an operator (+, -, \*, /) as input. The program should perform the specified operation and
   display the result. Ensure that the input is valid and handle possible errors (e.g., division by zero).
3. Create a simple login system using conditional statements.
   Design a program that simulates a basic login system. The program should ask for a username and password, and then
   compare the input to a list of predefined credentials. Display a success or failure message based on the input. Use
   the usernames and password below.

| Username	 | Password          |
|-----------|-------------------|
| admin1    | 	P@ssw0rd1        |
| user2	    | Str0ngP@ssw0rd    |
| guest3	   | GuestP@ssw0rd3    |
| student4  | 	L3arn1ngP@ssw0rd |
| tester5	  | P@ssw0rdTester5   |

These are just example combinations, and in real-world scenarios, you should ensure that passwords are securely stored (
e.g., using hashing) and follow good password practices.

Good luck when you've given it a good attempt take a look at this answer video to see how we did it