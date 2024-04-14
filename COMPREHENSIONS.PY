# SET COMPREHENSION
# a={x**2 for x in range(10)}
# print(sorted(a))

# n={num for num in a if num>20 and num<50}  # a here is a list or list  having many values
# print(sorted(n))

# # DICTIONARY COMPREHENSION
# d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}   # dictionary would be given 

# d1={k:v**3 for(k,v) in d.items() }
# print(d1)

# d2={k:v**3 for(k,v) in d.items() if v>4}
# print(d2)

# d3={k:('Even'if v%2==0 else 'Odd') for(k,v) in d.items()}
# print(d3)


# PROGRAM THAT GENERATES NUMBERS FROM 2-50 WHICH ARE DIVISIBLE BY 2 AND 4
# lst=[num for num in range(2,51) if num%2==0 and num%4==0]
# print(lst)

#program to flatten the list given    // means in continious form
#   given list= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# flat=[val for a in lst for val in a]
# print(flat)

# Add two 3x4 Matrix using list comprehension

# mat1=[[1,2,3,4],[5,6,7,8],[9,20,11,12]]
# mat2=[[1,2,3,4],[5,6,7,8],[9,20,11,12]]
# el=[element for row in mat1 for element in row]
# print(len(mat1))
# print(el)
# print(mat1[0])
# mat3=[[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1)) ]
# print(mat3)


# Capitalizing each element of the string joining the white sapces 

# sr='dreams may change over the period of time but friends are forever'
# s=["".join(w.capitalize() for w in sr.split())]
# print(s)