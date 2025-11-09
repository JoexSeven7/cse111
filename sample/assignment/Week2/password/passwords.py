# my Assignment for the week i added the try and except block to catch any error incase the code doen't run as planned. and i also added a break point where the code stops running all the user needs to do is to just press the Q or q to stop the code from running.
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"]

def word_in_file(word, filename,case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                 file_word = line.strip()
                 if case_sensitive:
                      if word == file_word:
                           return True
                 else:
                    if word.lower() == file_word.lower():
                         return True
            return False
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")  
        return False  
        

def word_has_character(word,character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    total_complexity = 0
    if word_has_character(word, LOWER):
        total_complexity += 1
    if word_has_character(word, UPPER):
        total_complexity += 1
        
    if word_has_character(word, DIGITS):
        total_complexity += 1
        
    if word_has_character(word, SPECIAL):
        total_complexity += 1
    return total_complexity
    
        



def password_strength(password, min_length=10,strong_length=20):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    elif word_in_file(password,"toppasswords.txt",case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0 
    elif len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    else:
        complexity = word_complexity(password)
        
    return 1 + complexity
    
    



def main():
    print("Type 'q' or 'Q' to quit at any time.")

    while True:
        user_password = input("Enter a password to check: ")
        if user_password == "q" or user_password =="Q":
            print("Goodbye!")
            break
        score = password_strength(user_password)
        print(f"Your password strength score is: {score}")



if __name__ == "__main__":

 main()