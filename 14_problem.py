#Q. Write a function that counts vowels in a string.
def count_vowel(text):
    vowels="a,e,i,o,u"
    count=0
    for chr in text:
        if chr in vowels:
            count+=1
            return count
print(count_vowel("Rama is a Good boy"))