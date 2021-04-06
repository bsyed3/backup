def createJson(url): #function that gathers info from url
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        return data

def createDirectory(dir_name, dir_path): #creates directory
    if os.path.exists(os.path.join(dir_path, dir_name))==False: #creates directory if it doesn't already exist
        path = os.path.join(dir_path, dir_name)
        os.mkdir(path)