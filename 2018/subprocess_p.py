import subprocess


"""subprocess"""
args = ["ping", "www.yahoo.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)

data = process.communicate()
for line in data:
    print(line)

# print(subprocess.Popen("ls", shell=True))

# program = "notepad.exe"
# process = subprocess.Popen(program)
# code = process.wait()
#
# print(code)

# code = subprocess.call(["ping", "www.yahoo.com"])

# code = subprocess.call("notepad.exe")
# if code == 0:
#     print("Success!")
# else:
#     print("Error!")

# subprocess.call("notepad.exe")
