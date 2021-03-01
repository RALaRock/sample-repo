# three ways to do it

# 1 - from module import *
# not a good idea as this will overwrite any of the same
# names in the latest module that exist in earlier modules
# from math import *
# print(dir())

# 2 - import only the specific methods needed from the module
# still overwrites, if a previous module has a same name
# safer than method 1
# from math import log2, log10
# print(log2(10))
# print(log10(10))
# print(dir())

# 3 - import the entire module but using the module name in all
# references, safest method, but have to use specific naming
import math
print(math.log2(20))
print(math.log10(20))
print(dir())
