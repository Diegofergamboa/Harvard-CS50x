import sys
from lib_hello import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])