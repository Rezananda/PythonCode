from sys import argv

fileInput=open(argv[1],'r').read()

fileSplit=fileInput.lower().replace('.','').replace(',','').split()
uniqueWord=list(set(list(fileSplit)))
uniqueWord.sort(reverse=True)

print (uniqueWord)