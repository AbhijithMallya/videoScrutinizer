import os
from pathlib import Path
import glob

file_names= []
file_names_extension= []



path = "E:\\VIDEO_SCRUTINIZER\\faceImages`"
 
# Using '*' pattern
# print('\nNamed with wildcard *:')
# for files in glob.glob(path + '/*[0-9].*'):
#     print(files)
 
# Using '?' pattern
print('\nNamed with wildcard ?:')
for files in glob.glob(path + '?.jpg'):
    print(files)
 



for file in os.listdir('faceImages'):
    file_names_extension.append(file)
    item = Path(file).stem
    file_names.append(item)

for file in glob.glob('faceImages'):
    print(file)


print(file_names_extension)
print(file_names)

