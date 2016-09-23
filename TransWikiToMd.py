import os

def recursiveTravelDir(dir = r".", callback = None):
	for file in os.listdir(dir):
		if os.path.isdir(file):
			file = os.getcwd() + os.sep + file
			recursiveTravelDir(file)
		else:
			print(file)

# recursiveTravelDir()
print("hello world")