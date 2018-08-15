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
         test = len(path) , '---', file
         filename = os.path.join(root, file)
         filename = filename.replace('./','')
       #  filename = filename.replace('www.tidigmodernakonkurser.se','')
         if test.__contains__(1) & test.__contains__('---'):
             substring = 'html'
             if substring in test[2]:
             	print filename
                replaceLinks(filename, test[0])

         if test.__contains__(2) & test.__contains__('---'):
             substring = 'html'
             if substring in test[2]:
             	print filename
                replaceLinks(filename,test[0])

         if test.__contains__(3) & test.__contains__('---'):
             substring = 'html'
             if substring in test[2]:
             	 print filename
                 replaceLinks(filename, test[0])
         if test.__contains__(4) & test.__contains__('---'):
             substring = 'html'
             if substring in test[2]:
             	 print filename
                 replaceLinks(filename, test[0])
         if test.__contains__(5) & test.__contains__('---'):
             substring = 'html'
             if substring in test[2]:
             	 print filename
                 replaceLinks(filename, test[0])        




