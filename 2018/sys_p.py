import sys


os = sys.platform
if os == "win32":
    # windows registry
    import winreg
elif os.startswith('linux'):
    # linux command
    import subprocess
    subprocess.Popen(["ls, -l"])

# print(sys.platform)
# print(sys.path)
# sys.exit(0)
# print(sys.executable)
# print(sys.argv)
