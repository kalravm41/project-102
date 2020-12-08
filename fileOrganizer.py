import os
import shutil

directory = input("Name The Directory To Be Sorted : ")

listOfFiles = os.listdir(directory)

for file in listOfFiles:
    name,extension = os.path.splitext(file)
    extension = extension[1:]    

    if extension == ' ':
        continue

    if os.path.exists(directory + '/'+ extension):
        shutil.move(directory + '/' + file, directory + '/' + extension + '/' + file)

    else:
        os.mkdir(directory + '/' + extension)
        shutil.move(directory + '/' + file , directory + '/' + extension + '/' + file)    
            
 