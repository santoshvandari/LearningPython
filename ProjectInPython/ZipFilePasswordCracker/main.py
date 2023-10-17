# # Write a Program in Python that will crack the password of a zip file.
# # The program should take the name of the zip file as an argument and
# # should try different passwords to crack the zip file.
# # The program should print the password that is used to crack the zip file.
# # If the password is not found, the program should print a message that
# # the password is not found and exit.
# # The program should be able to crack the password in a reasonable time.
# # The Process of Cracking password must be bruteforce

# import zipfile
# import sys
# import time

# if __name__=="__main__":




import zipfile


def crack_password(password_list, obj):
	# tracking line no. at which password is found
	idx = 0

	# open file in read byte mode only as "rockyou.txt"
	# file contains some special characters and hence
	# UnicodeDecodeError will be generated
	with open(password_list, 'rb') as file:
		for line in file:
			for word in line.split():
				try:
					idx += 1
					obj.extractall(pwd=word)
					print("Password found at line", idx)
					print("Password is", word.decode())
					return True
				except:
					continue
	return False


password_list = "rockyou.txt"

zip_file = "gfg.zip"

# ZipFile object initialised
obj = zipfile.ZipFile(zip_file)

# count of number of words present in file
cnt = len(list(open(password_list, "rb")))

print("There are total", cnt,
	"number of passwords to test")

if crack_password(password_list, obj) == False:
	print("Password not found in this file")
