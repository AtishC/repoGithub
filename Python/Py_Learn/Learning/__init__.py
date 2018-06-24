a=7                 #assigns a variable
print(a)
print(a+8)

print(type(a))      #prints the type of the variable
print(type(9.1))
print(type("hello"))

print("Floating Point Division 18/5 - ",18/5)         #carries out floating point division
print("Truncating Division 18/5 - ",18//5)        #carries out truncating division

print(9%5)          #returns the remainder
print(divmod(9, 5)) #returns both quotient and remainder
print(9//5)         #returns quotient only, truncating division

#Examples in Type Conversion
print("Integer value of TRUE  - ",int(True))
print("Integer value of FALSE - ",int(False))

poem='this is a "line"'
print(poem)

s='This is another line.'
print(s[0]+s[1]+s[2]+s[3])

print(s[:])         #Extracts entire sequence from start to end
print(s[:10])       #Extracts from beginning to end offset value minus 1
print(s[5:10])      #Extracts from start offset to end offset value minus 1
print(s[10:20:2])   #Extracts from start offset to end offset value minus 1 with a step 2
print(s[-3:])       #Extracts 3 characters from end
print(s[-10:20])

s="abcdefg"
print(s)
print(s[::-1])      #Reverse a string
print(s[5:2:-1])




