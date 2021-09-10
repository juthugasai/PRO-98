def swapFileData():
    f1=input("Name of original file: ")
    f2=input("Name of prank file: ")
    file1 = open(f1, 'r')
    data_a = file1.read()
    file1.close()
    file2 = open(f2, 'r')
    data_b = file2.read()
    file2.close()
    
    pranked = open(f1, 'w')
    pranked.write(data_b)
    pranked.close()

    prank = open(f2, 'w')
    prank.write(data_a)
    prank.close()

swapFileData()