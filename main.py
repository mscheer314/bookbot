from sys import argv 
import sys
from stats import report

if len(argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

report(argv[1])
