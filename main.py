import string

with open("/usr/share/dict/words", "r") as words: ## *nix systems (macOS in my case) already have a wordlist by default ##
    wordlist = words.read().split()

alphabet = list(string.ascii_lowercase)  ## ["a", "b" ....] ##

ciphertext = input("Enter ciphertext(min 5 words)> ")
cipherwords = ciphertext.split()

### Threshold to accept as correct ###
threshold = 70

trystep = 0
while True:
    correctwords = 0
    trystep += 1
    for word in cipherwords:
        tryword = ""
        for char in word: tryword += alphabet[(alphabet.index(char) - trystep) % len(alphabet)]
        if tryword in wordlist:
            correctwords += 1
    percaccuracy = round(correctwords/len(cipherwords) * 100, 3)
    print(f"The percentage accuracy for shift by {trystep} is {percaccuracy}%")
    if percaccuracy >= threshold:
        break
print(f"Accuracy for this shift is over the threshold, stopping...")
newstring = ""
for char in ciphertext:
    if char == " ": newstring += " "
    else: newstring += alphabet[(alphabet.index(char) - trystep) % len(alphabet)]
print("Your decoded text seems to be:")
print(newstring)
