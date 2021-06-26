# To get file name
print('Enter file name')
filename = str(input())

#To check File Name
if(filename == "" or filename=="con" or filename == "aux"):
    print('Error in your file name \n       You cant use file names like con or aux');

else:
    # To get maximum number 
    print("\nEnter maximum number")
    outputNumber = int(input())

    # To check number
    if(outputNumber==0 or outputNumber > 20000):
        print('Error in your number. \n     Make Sure you have not used 0 or number maximum than 20000')

    else:
        # Main Logic
        f = open(filename + '.txt', "w")
        for i in range(0, outputNumber):
            f.write(str(i+1) + '\n')
        f.close()