def isDouble_Vowel(word):
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i] == word[i + 1]:
            return True
    return False

def main():
    doubleVowel_count = 0
    totalWords = 0

    while True:
        word = input("Enter a word, quit to stop: ").lower()
        if word == "quit":
            break
        totalWords += 1
        if isDouble_Vowel(word):
            doubleVowel_count += 1

    if totalWords > 0:
        percentage = (doubleVowel_count / totalWords) * 100
        print(f"Number of double vowel words entered: {doubleVowel_count}")
        #print("Number of double vowel words entered:", str(doubleVowel_count))
        print(f"Percentage of words entered that have double vowels: {percentage:.2f}%")
        #print("Percentage of words entered that have double vowels: " + str(round(percentage,2)) + "%")
    else:
        print("No words entered.")

main()
