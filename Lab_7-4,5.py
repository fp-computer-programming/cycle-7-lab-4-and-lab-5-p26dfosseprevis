
#Create a Python file named lab_7-4.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Copy your lab 7-2 code into the file
#Add 4 test cases to the end of the file, with comments
#Ensure your lab runs accurately

def find_sum(num1,num2):
    """Finds the sum of the two inputed numbers"""
    num_sum = num1 + num2
    return num_sum
    
print(find_sum(111,222) == 333)
print(find_sum(1,2) == 3)
print(find_sum(1.5,1.5) == 3)
print(find_sum(2763,2763) == 5526)


#________________________________________________________________________________

#Create a Python file named lab_7-5.py


#Copy the code from your labs 6-5 through 6-8
#Turn each of the programs into a function
#Add 4 test cases to the functions
#Ensure your code runs accurately

def hilo(list):
    i = 1
    re = [list[0],list[0]]
    while i < len(list):
        if list[i] > re[0]:
            re[0] = list[i]
        if list[i] < re[1]:
            re[1] = list[i]    
        i += 1    
    return re if len(list) >= 2 else "error: list does not meet specifications"   

print(hilo([1,2,3,4,5]) == [5, 1])
print(hilo([1]) == "error: list does not meet specifications")
print(hilo([5,6,7,8]) == [8, 5])
print(hilo([2,7,6,3]) == [7, 2])


def six(q,w,e,r,t):
    return str(len(q))+" "+str(len(w))+" "+str(len(e))+""+str(len(r))+" "+str(len(t))
print(six("red","blue","orange","purple","grey") == "3 4 66 4")
print(six("frdeas","trdrgre","frdgttdv","gftdbdxfgbt","fdgtbtr") == "6 7 811 7")
print(six("fdgrtvdrtgb","fvgdrvbgftr","dfgbtrdvg","fgtbgftbgft","fbcvfgtb") == "11 11 911 8")
print(six("drftgtffrt","grftdg","grtdgvrt","rgftdvfrtdv","rgtffgtrf") == "10 6 811 9")


def seven(a,s,d):
    return(str(int(a)*2)+" "+str(int(s)*2)+" "+str(int(d)*2))
print(seven(1,3,4) == "2 6 8")
print(seven(34,8,4) == "68 16 8")
print(seven(23,7,34) == "46 14 68")
print(seven(2,5,8) == "4 10 16")

def evenodd(z,x,c):
    list = [int(z),int(x),int(c)]
    return "even" if list[0]/2 == int(list[0]/2) and list[1]/2 == int(list[1]/2) and list[2]/2 == int(list[2]/2) else "odd" if list[0]/2 != int(list[0]/2) and list[1]/2 != int(list[1]/2) and list[2]/2 != int(list[2]/2) else "mixed"
print(evenodd(1,3,5) == "odd")
print(evenodd(2,4,6) == "even")
print(evenodd(3,6,9) == "mixed")
print(evenodd(2,7,6) == "mixed")