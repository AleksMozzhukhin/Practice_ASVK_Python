def count_vowels_consonants(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    all_letters = set('abcdefghijklmnopqrstuvwxyz')

    consonants = all_letters - vowels

    letters_in_s = set(filter(lambda c: c.islower() and c.isalpha(), s))

    unique_vowels = letters_in_s & vowels
    unique_consonants = letters_in_s & consonants

    print(f"Гласных - {len(unique_vowels)} ({', '.join(sorted(unique_vowels))})")
    print(f"Согласных - {len(unique_consonants)} ({', '.join(sorted(unique_consonants))})")

s = input()
count_vowels_consonants(s)
