

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

def is_anagram(s1, s2):
    """Return True if s1 and s2 are anagrams (same characters, same counts).
    Example: is_anagram("listen", "silent") -> True
    """
    # Hint: compare character-frequency maps, or sorted(s1) == sorted(s2).
    #       Decide whether case/spaces should matter.
    # TODO: implement
    dict1={}
    dict2={}
    for c in s1:
        dict1[c]= dict1.get(c,0)+1
    for c in s2:
        dict2[c]= dict2.get(c,0)+1
    return dict1== dict2


def char_frequency(input_string):
    """Return a dict mapping each character to how many times it appears.
    Example: char_frequency("aab") -> {"a": 2, "b": 1}
    """
    # Hint: same pattern as find_non_repeating_character:
    #       freq[char] = freq.get(char, 0) + 1
    # TODO: implement
    mapping_dict={}
    for c in input_string:
        mapping_dict[c]= mapping_dict.get(c,0)+1
    return mapping_dict


def reverse_words(input_string):
    """Return the string with word order reversed.
    Example: reverse_words("the sky is blue") -> "blue is sky the"
    """
    # Hint: .split() breaks on whitespace, reverse the list, then " ".join(...)
    # TODO: implement
    split_words = input_string.split()
    reversed_words = split_words[::-1]
    return " ".join(reversed_words)


def longest_common_prefix(strings):
    """Return the longest prefix shared by all strings in the list.
    Example: longest_common_prefix(["flower", "flow", "flight"]) -> "fl"
    """
    # Hint: compare characters column-by-column across all strings, or
    #       start with strings[0] as the candidate and shrink it.
    #       Watch out for an empty list or an empty string in the list.
    if not strings:
        return ""

    # Start by assuming the whole first word is the common prefix.
    prefix = strings[0]

    # Shrink the prefix until every word starts with it.
    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]   # drop the last character
            if prefix == "":
                return ""
    return prefix


def run_tests():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "world") is False

    assert char_frequency("aab") == {"a": 2, "b": 1}
    assert char_frequency("") == {}

    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("hello") == "hello"

    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "cat"]) == ""
    assert longest_common_prefix([]) == ""

    print("All tests passed ✅")


def main():
    run_tests()




if __name__=="__main__":
    main()