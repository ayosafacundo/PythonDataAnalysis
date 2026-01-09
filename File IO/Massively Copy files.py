import os, shutil

def main():
    directory = r"C:\Users\ayosa\Downloads\a\Students"
    outputDir = r'C:\Users\ayosa\Desktop\Markdown file'

    filenames = os.listdir(directory)
    files = []
    dirs = []
    for file in filenames:
        if (file[-3:] == ".md"):
            files.append(file)
        else:
            dirs.append(file)

    print("file = ", len(files), " dirs = ", len(dirs))

    for index in range(len(files)):
        try: 
            st = files[index]
            fil = " ".join(st.split(" ")[:-1])
            if (fil == 'Untitled'):
                continue
            if index < len(dirs):
                st2 = dirs[index]
                fil2 = " ".join(st2.split(" ")[:-1])
                fromdir = os.path.join(directory, dirs[index])
                todir = os.path.join(outputDir, fil2)
                os.mkdir(todir)
                copytree(fromdir, todir)
            else:
                todir = os.path.join(outputDir, fil)
                os.mkdir(todir)
            fromfile = os.path.join(directory, files[index])
            shutil.copy(fromfile, todir)
            os.rename(os.path.join(todir, files[index]), os.path.join(todir, (fil + ".md")))
        except(FileExistsError):
            continue

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)



main()