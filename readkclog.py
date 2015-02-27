#!/usr/bin/env python3

# quick script to better format output from keycount
# pipe keycount's output files into this to produce a
# more legible summary

import sys

syms = {}
digraphs = {}
trigraphs = {}

cursym = None
curdigraph = None

for line in sys.stdin:
    if line.find("#") > -1 or len(line) == 0:
        continue # I'm not going to bother with proper comment parsing for this
    spl = line.split()
    if len(spl) == 1:
        symnum = spl[0].split(":")
        cursym = symnum[0]
        syms[cursym] = syms.get(cursym, 0) + int(symnum[1])
    elif len(spl) == 2:
        symnum = spl[1].split(":")
        curdigraph = cursym+"-"+symnum[0]
        digraphs[curdigraph] = digraphs.get(curdigraph, 0) + int(symnum[1])
    elif len(spl) == 3:
        symnum = spl[2].split(":")
        curtrigraph = curdigraph+"-"+symnum[0]
        trigraphs[curtrigraph] = trigraphs.get(curtrigraph, 0) + int(symnum[1])
    else:
        print("Some weird error:" + line)

print("------- Symbol frequency -------")
symview = sorted( ((v,k) for k,v in syms.items()), reverse=True)
total = 0
for elem in symview:
    total += elem[0]

print("total: "+str(total)+" keypresses")

for elem in symview:
    print("%.3f%% %d %s"%((100*elem[0]/total), elem[0], elem[1]))
    
print("------- digraph frequency -------")
symview = sorted( ((v,k) for k,v in digraphs.items()), reverse=True)
for elem in symview:
    print("%.3f%% %d %s"%((100*elem[0]/total), elem[0], elem[1]))

print("------- trigraph frequency -------")
symview = sorted( ((v,k) for k,v in trigraphs.items()), reverse=True)
for elem in symview:
    print("%.3f%% %d %s"%((100*elem[0]/total), elem[0], elem[1]))

