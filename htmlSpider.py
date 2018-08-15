import os
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

def replace(file_path, pattern, subst):
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    remove(file_path)
    
    move(abs_path, file_path)
def replaceLinks(filename,level):

   # toReplace = """<button type="submit" disabled"""
    toRemove =  """ <button type="submit" """
    toReplace = """<button type="submit" disabled s"""
    replace(filename,toRemove,toReplace)



for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    dir = (len(path) - 1) , 'dir', os.path.basename(root)
    for file in files:
         serchedStrings = len(path) , '---', file
         filename = os.path.join(root, file)
         filename = filename.replace('./','')
         if searchedStrings.__contains__(1) & searchedStrings.__contains__('---'):
             substring = 'html'
             if substring in searchedStrings[2]:
             	print filename
                replaceLinks(filename, searchedStrings[0])

         if searchedStrings.__contains__(2) & searchedStrings.__contains__('---'):
             substring = 'html'
             if substring in searchedStrings[2]:
             	print filename
                replaceLinks(filename,searchedStrings[0])

         if searchedStrings.__contains__(3) & searchedStrings.__contains__('---'):
             substring = 'html'
             if substring in searchedStrings[2]:
             	 print filename
                 replaceLinks(filename, searchedStrings[0])
         if searchedStrings.__contains__(4) & searchedStrings.__contains__('---'):
             substring = 'html'
             if substring in searchedStrings[2]:
             	 print filename
                 replaceLinks(filename, searchedStrings[0])
         if searchedStrings.__contains__(5) & searchedStrings.__contains__('---'):
             substring = 'html'
             if substring in searchedStrings[2]:
             	 print filename
                 replaceLinks(filename, searchedStrings[0])        




