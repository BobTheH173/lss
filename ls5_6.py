import sys

print("\nPython path - ", sys.executable)
print("\nPython version", sys.version)
print("\nPlatform - ", sys.platform)
print("\nArguments - ", sys.argv)
print("\nMax integer size - ", sys.maxsize)
print("\nMemory used", sys.getsizeof(sys))
print("\nAvailable attributes", dir(sys))
