import os


# print(dir(os))
# print(os.path.expanduser("~\Desktop"))


def arrangefiles(path):
    files = os.listdir(path)
    extension = []
    for file in files:
        file_ext = os.path.splitext(file)[1][1:]
        folder_path = os.path.join(path, file_ext)
        if folder_path not in extension:
            extension.append(folder_path)
    for folder in extension:
        try:
            os.mkdir(folder)
        except:
            print("Folder already exist.")
        for file in files:
            folder_extension = os.path.split(folder)[1]
            file_ext = os.path.splitext(file)[1][1:]
            if folder_extension == file_ext:
                os.rename(os.path.join(path,file),os.path.join(folder,file))


if __name__ == '__main__':
    path = r"C:\Users\Priya\Desktop\fileAutomation"
    arrangefiles(path)
