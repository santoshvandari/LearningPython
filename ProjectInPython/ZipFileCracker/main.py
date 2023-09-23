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




    import zipfile
import itertools

def crack_password(zip_file, max_length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?~"
    
    # Try all possible password combinations up to the specified max length
    for length in range(1, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            password = ''.join(combination)
            
            try:
                with zipfile.ZipFile(zip_file, 'r') as zf:
                    zf.extractall(pwd=password.encode())
                print("Password found:", password)
                return password
            except Exception:
                continue
    
    return None

zip_file = "gfg.zip"
result = crack_password(zip_file)

if result is None:
    print("Password not found.")
