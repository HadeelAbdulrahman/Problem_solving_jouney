#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#Print the merged string.

w1=input("enter word 1:")
w2=input("enter word 2:")
w3=""
if(len(w2)>len(w1)):
    n=len(w2)-len(w1)
    w1=w1+" "*n

else:
    n=len(w1)-len(w2)
    w2=w2+" "*n
for i in range(len(w1)):
    w3=w3+w1[i]+w2[i]
print(f"Merged:{w3}")
