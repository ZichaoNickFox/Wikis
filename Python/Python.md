#os
递归遍历目录
```python
def recursiveTravelDir(dir = r"."):
    for file in os.listdir(dir):
        if os.path.isdir(file):
            file = os.getcwd() + os.sep + file
            recursiveTravelDir(file)
        else:
            print(file)
```