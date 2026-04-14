text="Software develOper"
#capitalize used to make the first letter uppercase
text.upper()
print(text)
#count used to count the number of appearance of a character
text2=text.count('o')
print(text2)

message="ruth wanjiku "
print(message.upper())

#casefold
#lower
text3=text.casefold()
print(text3)
text4=text.lower()

#count- counts te number of appearance of a specif character in  string
print(text.count("e"))
print(text.find("e"))

#find - returns the first occurence of a character
text="Software DevelOper"
print(text.find("d"))

#index - returns the index of the first occurence of a character returns an error if the character is not availabe
text="Software DevelOper"
print(text.index("d"))

text="Software DevelOper"
print(text.replace("software, python"))

#split - it splits a string using a specific character
email ="ruthwanjiku@gmail.com"
split_email=email.split("@")
print(split_email)
text="Software DevelOper"
txt=text.split()
print(txt)



#strip() -remove leading and trailing spaces
text_strip= "      data science"
print(len(text_strip))
text_strip=text_strip.strip()
print(len(text_strip))