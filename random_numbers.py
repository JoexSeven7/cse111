import random


def main():
    numbers = [2,4,6,8,10]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,3)
    print(numbers)
    words = ['Join', 'Love','Joy','Peace']
    print(words)

def append_random_numbers(numlist,quantity=1):
     for _ in range(quantity):
        num = random.uniform(0,100)
        num = round(num,1)
        numlist.append(num)

def append_random_words(wordlist,quantity=1):
    for _ in range(quantity):
        word = random.choice(wordlist)
        word = round(word)
        wordlist.append(word)

if __name__ == "__main__":
    main() 