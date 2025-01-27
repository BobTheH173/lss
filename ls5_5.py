import sys

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
