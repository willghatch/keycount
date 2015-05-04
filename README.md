keycount is a key logger that counts the number of:
- presses of any individual key
- digraphs of two given keys
- trigraphs of two given keys

The output format puts the count of individual keys on the first column,
th count for digraphs in the second (nested under the first key of the
digragh), and trigraphs similarly.  This was simply a convenient format.
Output is meant to be read by the included readkclog.py script.

readkclog.py requires python3, and simply takes the output format of
keycount through stdin.  It produces a nice report to stdout.

The idea is to count these things to make a custom keymap.

This program was written by cannibalizing code from the program xcape
written by alols and others.

https://github.com/alols/xcape.git
    
Thanks, alols and friends, for making something I could rip apart rather than starting
from scratch.

Build by running `make`.

Run with --help to see options.


BUGS:
It loses one future digraph and two future trigraphs every time it dumps.
It was easier that way.  It's b-grade software to gather some data quick-like.
