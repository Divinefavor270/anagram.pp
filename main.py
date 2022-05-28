# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True





# function to check if two strings are
# anagram or not



def checkforang(s1, s2):

#convert both strings to lowercase
    string1=s1.lower()
    string2=s2.lower()
     
    # the sorted strings are checked
    if(sorted(string1)== sorted(string2)):
        result=True
    else:
        result=False
    return result
       
         
# driver code 
s1 ="abyss"
s2 ="byssa"
print(checkforang(s1, s2))

       
         



