# In the past format is used as a adding string. But in the present time f string is introdcued

name="Santosh"
address="Kanakai"
subject="BCA"
college="Mechi"

print(f"My name is {name} and live in {address}. I am Currently Studying {subject} in {college}.")

sentence="My name is {} and live in {}. I am Currently Studying {} in {}.".format(name,address,subject,college)
print(sentence)
print("My name is {} and live in {}. I am Currently Studying {} in {}.".format(name,address,subject,college))