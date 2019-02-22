
import sys

for a in range(1, 10):
    for b in range(1, 10):
        sys.stdout.write("%3d" % (a * b))
    sys.stdout.write('\n')

