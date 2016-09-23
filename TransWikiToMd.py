#-*- coding: UTF-8 -*-

#不支持多级列表
import os
import re


##得到文件名和扩展名
def FileNameAndExt(fileWithExt):
    pos = fileWithExt.rfind(".")
    file = ""
    ext = ""
    if pos == -1:
        file = fileWithExt
    else:
        file = fileWithExt[:pos]
        ext = fileWithExt[pos+1:]
    return file, ext

def joinPathFileExt(path, file, ext):
    return path + "/" + file + "." + ext

def HandleLine(line):
    #去除两边的空格
    line = line.strip()

    #删除Contents段落
    global isInContentParam
    if not isInContentParam:
        if line.startswith("=") and line.endswith("=") and "Contents" in line:
            isInContentParam = True
            line = ""
    else:
        if line == "":
            isInContentParam =False
        line = ""

    #替换{{{class = "brush:xxx"}}}
    # 为```c++
    if "{{{" in line:
        #一行中有指定字符串
        lang = ""
        if "brush" in line:
            #匹配brush和"中间的字符串
            pattern = re.compile(".*brush:(.*)\"")
            lang = pattern.search(line).groups()[0]
            lang = lang.strip()
        line = "```" + lang

    #替换}}}
    #为```
    line = line.replace(r"}}}", r"```")

    #替换wiki列表#space
    #为md列表1.space
    if line.startswith("#") and not line.endswith("#"):
        #截取
        line = line[2:]
        line = "1. " + line

    #替换wiki标题=
    #为md标题#
    if line.startswith("=") and line.endswith("="):
        line = line.replace("=", "#")

    #替换[[path|showString]]
    #为[showString](path.md)
    #替换[[path]]
    #为[path](path.md)
    left = line.find("[[")
    right = line.find("]]")
    if left != -1 and right != -1:
        content = line[left + 2: right]
        path = ""
        showString = ""
        if '|' in content:
            pos = content.find('|')
            path = content[:pos]
            showString = content[pos + 1:]
        else:
            path = content
            showString = content
        mdContent = "[" + showString + "](" + path + ".md" + ")"
        mdLine = line[:left] + mdContent + line[right + 2:]
        line = mdLine

    return line

#将\n作为分隔符的长字符串划分到string中
def ParseLongStringToArray(string):
    line = ""
    lines = []
    for c in string:
        if c!= "\n":
            line = line + c
        else:
            lines.append(line)
            line = ""
    if line != "":
        lines.append(line)
    return lines

def createMd(path, file, ext):
    ext = "md"
    open(joinPathFileExt(path, file, ext), "w+").close()

def removeMd(path, file, ext):
    if ext == "md":
        os.remove(joinPathFileExt(path, file, ext))

def removewiki(path, file, ext):
    if ext == "wiki":
        os.remove(joinPathFileExt(path, file, ext))

def writeMd(path, file):
    assert(os.path.exists(joinPathFileExt(path, file, "md")))
    assert(os.path.exists(joinPathFileExt(path, file, "wiki")))
    fileWiki = open(joinPathFileExt(path, file, "wiki"), "r")
    fileMd = open(joinPathFileExt(path, file, "md"), "w")
    for line in fileWiki:
        line = HandleLine(line)
        fileMd.write(line + "\n")
    fileWiki.close()
    fileMd.close()

#递归文件的回调，会传回来：文件名+扩展名，路径
def TravelHandle(path, file, ext):
    removeMd(path, file, ext)
    createMd(path, file, ext)
    writeMd(path, file)
    pass

#递归遍历文件
def RecursiveTravelDir(path, call):
    for file in os.listdir(path):
        if file.startswith("."):
            continue
        if os.path.isdir(file):
            file = path+ "/" + file
            RecursiveTravelDir(file, call)
        else:
            path = path.replace("\\", "/")
            file = file.replace("\\", "/")
            fileName, fileExt = FileNameAndExt(file)
            if fileExt != "wiki" and fileExt!= "md":
                continue
            call(path, fileName, fileExt)


isInContentParam= False
RecursiveTravelDir(path = ".", call = TravelHandle)
