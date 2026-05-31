

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
    occurnce_count=0
    new_seq=set(input_string)
    for x in new_seq:
          for y in input_string:
            if x==y:
                occurnce_count= occurnce_count +1
          if occurnce_count >= 2:
            return x
    return -1   

def main():
    input_string= input("Enter input string \n")
    result=find_non_repeating_character(input_string.lower())
    print(f"Result is : \n{result}")




if __name__=="__main__":
    main()