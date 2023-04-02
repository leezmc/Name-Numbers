# Purpose: Calculates a persons name number
# Author: Michael Lee
# Date: February 15, 2023

# adds adds name numbers togethor
def sumDigits(number):
    while number >= 10:
        sum = 0
        for i in str(number):
            sum += int(i)
        number = sum
    return number
# converts name to number, and returns the sum of name numbers
def nameNumber(name):
    letterToNumber = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1, 'J': 1, 'K': 2, 'L': 3, 'M': 4,
                        'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2, 'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7}
    name = name.upper()
    nameNumber = 0
    for i in name:
        if i in letterToNumber:
            nameNumber += letterToNumber[i]
    nameNumber = sumDigits(nameNumber)
    return nameNumber
# sets predictions based on the number of digits in name
def prediction(number):
    predictions = {1: 'A person who is successful in personal ambitions.',
                   2: 'A gentle and artistic person.',
                   3: 'A success in their professional career.',
                   4: 'An unlucky person who much put in extra work for success.',
                   5: 'A lucky person who leads an unconventional life.',
                   6: 'A person who commands the respect of others.',
                   7: 'A person who has a strong inner spirit.',
                   8: 'A person who is misunderstood by others and is not respected for their success.',
                   9: 'A person who is more successful in matters of the material than spiritual.'}
    if number not in predictions:
        return 'Invalid Input'
    return predictions[number]
# output 
if __name__ == "__main__":
    print("Welcome to Name Number Generator")
    name = input("Enter Your Name: ")
    nameNumber = nameNumber(name)
    print("Your Name Number is", nameNumber)
    print("We predict you are:")
    print(prediction(nameNumber))
