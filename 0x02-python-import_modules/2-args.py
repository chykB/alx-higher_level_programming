#!/usr/bin/python3
import sys
args = sys.argv[1:]
n_args = len(args)

print(f"{n_args}", end=" ")

if n_args == 0:
    print("Arguments.")
else:
    print(f", Argument: \n")
    for i in range(n_args):
        print(f"{i+1}: {args[i]}")
