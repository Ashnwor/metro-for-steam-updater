import subprocess
from os import getlogin
from os import listdir
from zipfile import ZipFile

# define some shit
urlAddress = "https://metroforsteam.com/"
urlIndex = urlAddress + "index.html"
urlUnofficial = "https://github.com/redsigma/UPMetroSkin/archive/master.zip"
skinsLocation = "/home" + "/" + getlogin() + "/.steam/steam/skins/metro-for-steam"
unofficialPatchFileName = "unofficial_patch.zip"
linkList = []
actualFileList=[]
search = True
searchForSlash = True

subprocess.run(["wget", urlIndex])
index = open("index.html", "rt")
context = index.read()
index.close()
# Search for certain string in the index file
start = context.find(".zip")
searchIndex = start

while search:
    searchIndex = searchIndex-1
    varIndex = context[searchIndex]
    if searchForSlash == True:
        if varIndex == "/":
            fileNameStart = searchIndex+1
            searchForSlash = False
            print("Filename start:", fileNameStart)
    if varIndex == "\"":
        searchIndex = searchIndex+1
        break
fileStart = searchIndex
print("file start index:", context[fileStart])
print("starting index:", start)
print(context[start])
end = context.find(".zip")+4
for x in range(end-fileNameStart):
    actualFileList.append(context[fileNameStart+x])
actualFile = ''.join(actualFileList)
print(actualFileList)
print(actualFile)
print("ending index:", end)
print(context[end-1])
for x in range(end-fileStart):
    linkList.append(context[fileStart+x])
link = ''.join(linkList)
print(link)
print(unofficialPatchFileName)

# download theme
subprocess.run(["wget", link])
# download unofficial patch
subprocess.run(["wget", "-O", unofficialPatchFileName, urlUnofficial])
# extract theme to temp folder 
with ZipFile(actualFile, "r") as themeZip:
    themeZip.extractall("temp")
# extract unofficial patch to tempPatch folder
with ZipFile(unofficialPatchFileName, "r") as zipUnofficialPatch:
    zipUnofficialPatch.extractall("tempPatch")
ls = listdir("tempPatch")
midFolder = str(ls[0])
print(str(ls[0]))
print(listdir("tempPatch/" + str(ls[0])))
ls = listdir("tempPatch/" + str(ls[0]))
for st in ls:
    if 'Unof' in st:
       folder = st
ls = listdir("tempPatch/" + midFolder + "/" + folder)
print(ls)
for st in ls:
    if 'Main' in st:
       folder1 = st

subprocess.run(["cp", "-avf", "temp/.", skinsLocation])
# subprocess.run(["unalias", "cp"])
subprocess.run(["cp", "-avf", "tempPatch/" + midFolder + "/" + folder + "/" + folder1 + "/.", skinsLocation])
print("tempPatch/" + midFolder + "/" + folder + "/" + folder1)
listdir("tempPatch/" + midFolder + "/" + folder + "/" + folder1)
thisMenu = listdir()
if "Extras" in thisMenu:
    print("Extras folder found")
    subprocess.run(["cp", "-avrfa", "Extras/.", skinsLocation])

# delete unnecessary files
subprocess.run(["rm", "index.html", actualFile, unofficialPatchFileName])
subprocess.run(["rm", "-rf", "temp", "tempPatch"])


