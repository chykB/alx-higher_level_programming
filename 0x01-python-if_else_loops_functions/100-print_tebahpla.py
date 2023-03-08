#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1:
        print("{0}{1}".format(chr(i).lower() if i % 2 == 1 else chr(i).upper(), "" if i == ord('A') else ""), end="")
