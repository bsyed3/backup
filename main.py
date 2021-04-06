import os
import os.path
from os import path
import pathlib
import config
import functions
import urllib.request, json 

batchLimit = config.batch() #gets bath limit from config file
apiUrl = config.url() #gets api URL from config file
main_dir = config.mainDirectory() #gets name of main directory
d = 'd' #d for directory
f = 'f' #f for file

dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

jsonData = functions.createJson(apiUrl)

#print(list(jsonData['d'].keys())[1])

functions.createDirectory(main_dir, dir_path)

for i in jsonData[d]:
    new_path = os.path.join(dir_path, main_dir)
    functions.createDirectory(i, new_path)

    for j in jsonData[d][i][d]:
        new_path = os.path.join(dir_path, main_dir, i)
        functions.createDirectory(j, new_path)

        for k in jsonData[d][i][d][j][d]:
            new_path = os.path.join(dir_path, main_dir, i, j)
            functions.createDirectory(k, new_path)

            for l in jsonData[d][i][d][j][d][k][d]:
                new_path = os.path.join(dir_path, main_dir, i, j, k)
                functions.createDirectory(l, new_path)