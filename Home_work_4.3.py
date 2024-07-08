import pathlib
import sys
a = sys.argv
path = pathlib.Path("a")
for root, dirs, files in path.walk(): 
    print("Root: ") 
    print(root) 
    print("Dirs: ") 
    print(dirs) 
    print("Files: ") 
    print(files) 
    print("")