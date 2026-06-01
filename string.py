

# reverse string
def reverse_string(input_string):
    return input_string[::-1]

def palindrome_check(input_string):
    return input_string == reverse_string(input_string)
def count_vowels(input_string):
    vowels=["a","e","i","o","u"]
    vowels_count= [x for x in input_string if x in vowels]
    print(len(vowels_count))
    return len(vowels_count)
def find_non_repeating_character(input_string):
    char_dict={}
    for char in input_string:
        char_dict[char]= char_dict.get(char,0)+1
    for char in input_string:
        if char_dict[char]==1:
            return char
    return None

def main():
    input_string= input("Enter input string \n")
    result=find_non_repeating_character(input_string.lower())
    print(f"Result is : \n{result}")




if __name__=="__main__":
    main()