name = "   JOhn  ."
clean_name = name.lower().strip().replace("."," ")
print(clean_name)

#second question
sentence_one="The Dog Breed is German Shepherd" 
print(sentence_one[8:23])

sentence_two=" Defeats for the Clinton forces,this was her moment of triump"
print(sentence_two[17:31])

#third question
text = "The lazy dog; ran so fast; it hit the wall."

parts = text.split(";")
print(parts)
print(len(parts))

#forth question
first_name = "  john  "
last_name = "  doe  "

full_name = first_name.strip().capitalize() + " " + last_name.strip().capitalize()
print(full_name)

#fifth question
text = "[E, W, C]"
clean_text = text.strip("[]").replace(", ", "")
print(clean_text)
