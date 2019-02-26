# Printing a multiplication table.

# One of the first programs I wrote (computers were much simpler then)
# printed out a table of squares and square roots.  Before we had
# calculators, scientists and engineers referred to books of tables to
# look up numbers.  You may have seen a 10 by 10 multiplication table
# on the back cover if a notebook.  Do they still have those?

# We can use python to print out a multiplication table.

import sys

for a in range(1, 10):
    for b in range(1, 10):
        sys.stdout.write("%3d" % (a * b))
    sys.stdout.write('\n')


# In the 1800s Charles Babbage designed a mechanical calculating
# engine to produce more complicated tables that would be more
# accurate than those calculated by hand.  The accuracy of such tables
# was important because they were used by ships captains to navigate
# across the Atlantic Ocean.

