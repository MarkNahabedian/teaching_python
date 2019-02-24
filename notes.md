# Learning

One way to learn about programming is to read other people's programs
and try to understand how they work.  I've been learning about
woodworking by watching videos on YouTube.  For as long as there have
been people we've been learning by watching and listening to each
other.

Another way to learn is to have a project in mind that motivates you,
and to work towards completing that project.  This approach has the
problem that one might not know how much work and learning are
involved when one gets started and then give up in frustration.  The
key to solving any problem that is too big to work out all at once is
to figure out how to break it up, or decompose it, into smaller and
smaller problems one can solve.  Sometimes one finds that a particular
decomposition isn't as helpful as one first hoped, so one needs to
back up and try again.  At this point and at your age it's all a
learning experience and the more you try it the better you"ll get.

# Programming as a Tool

Computer programming is a tool we can use to simplify some task.  If
we want to hang a picture on a wall we might use a hammer to pound in
a nail.  If we want to design a bicycle we might use a computer to
help us figure out what combinations of gears we should have at the
crank and rear wheel.

Computer languages have accumulated large libraries of programs.
Chances are that if the problem you're trying to solve is common
enough, then someone has already written a program to solve it or get
you part way there.  You can use Google to help you find these
libraries or programs if you can describe what you're looking for in
the same way the author would have.  I often do a Google search rather
than looking for something in the manual.

# Text Based Programming Languages

In Scratch you used basic building blocks and dragged them together,
connecting them to describe your program.

In python and most other computer languages, programs are described
textually.  In English we put words together to make sentences and put
sentences together into paragraphs to say more than we can fit in one
sentence.  In a computer language we do the same.  In a computer
languag the words are called "tokens" because the basic vocabulary
might include words or symbols (like the plus sign, for example).  In
all languages, English or python included, there are rules that tell
us how we can put the words or tokens together.  These rules are
called the "grammar", or "syntax" of the language.

If you've looked at a typewriter or computer keyboard, you have
probably noticed that it doesn't have keys for common aritmetic
operations like multiplication (×) or division (÷).  Most text based
computer languages use * for multiplication and / for division.


# Baby Steps and Some History

One of the first programs I wrote (computers were much simpler then)
printed out a table of squares and square roots.  Before we had
calculators, scientists and engineers referred to books of tables to
look up numbers.  You may have seen a 10 by 10 multiplication table on
the back cover if a notebook.  Do they still have those?

We can use python to print out a multiplication table.

In the 1800s Charles Babbage (you can ead about him on Wikipedia)
designed a mechanical calculating engine to produce such tables that
would be more accurate than those calculated by hand.  The accuracy of
such tables was important because they were used by ships captains to
navigate across the Atlantic Ocean.


# Interacting With Python

Python is an interpreted language.  You don't need to know what that
means.  Practically though, it means that there's an environment that
you can interact with.  If you start python with

<pre>
python -i
</pre>

then you can use it in interactive mode.  Expressions you type wll be
run (evaluated) and the result printed out.

You can also examine things directly.

The *dir()* function returns a list of all of the properties of whatever
you pass to it.

The *type()* function tells you what the data type of its argument is.
Every object (any data artifact in python) has a data type.

The *help()* function will show you documentation.

Many objects (particularly functions and classes) also have a __doc__
property that contains documentation for that object.  Try _someobject_.__doc__.

