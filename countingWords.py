introString=input("Enter your introduction: ")
characterCount=0
wordCount=1

for i in introString:
    characterCount=characterCount+1
    if (i==" "):
        wordCount=wordCount+1

print("number of words: " + str(wordCount) )
print("number of characters: " + str(characterCount) )        

