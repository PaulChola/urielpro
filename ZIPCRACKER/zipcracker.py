import zipfile
import itertools

z = zipfile.ZipFile("ZIP FILE NAME")
z.printdir()
z.close()

alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
f = open("dict.txt", "w")
for passlen in [6]:
    combinations = itertools.product(alphabets, repeat = passlen)
    for combination in combinations:
        f.write(''.join(combination)+"\n")

alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
f = open("dict.txt", "w")
for passlen in [6]:
    combinations = itertools.product(alphabets, repeat = passlen)
    for combination in combinations:
        f.write(''.join(combination)+"\n")


z = zipfile.ZipFile("secret.zip")
files = z.namelist()
z.setpassword("b1c1e5")
z.extractall()
z.close()
for extracted_file in files:
    print ("File name:"+extracted_file+"\n\nContent:")
    with open(extracted_file) as f:
        content = f.readlines()
        print (''.join(content))
        print ('\n\n')



