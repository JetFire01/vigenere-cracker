alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
    "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"]

english_freq = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256,
    0.0217, 0.0180, 0.0527, 0.0724, 0.0014, 0.0063, 0.0404,
    0.0260, 0.0738, 0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915,
    0.0279, 0.0100, 0.0189, 0.0021, 0.0165, 0.0007,]

print("Input the data: \n \nCiphertext: ")
cipher_text = input()
print("Maximum length the key: ")
key_length_max = int(input())

# Step 1, calculate the key length

# Create a list of matches of the required size

coincidences = []

for i in range(key_length_max):
    coincidences.append([0])

# Calculate the match for each element

for shift in range(key_length_max):
    for lettre in range(len(cipher_text) - (shift + 1)):
        if cipher_text[lettre] == cipher_text[lettre + shift + 1]:
            coincidences[shift][0] += 1
    coincidences[shift][0] = coincidences[shift][0] / (len(cipher_text) - (shift + 1))

key_length = coincidences.index(max(coincidences))
key_length += 1

# Step 2

# Splitting the text into k parts

cipher_text_divided = []

for i in range(key_length):
    cipher_text_divided.append([])

for i in range(key_length):
    for j in range(i, len(cipher_text), key_length):
        cipher_text_divided[i].append(cipher_text[j])

# Finding letter frequency

frequency_dictionary = []

for i in range(key_length):
    frequency_dictionary.append([0] * 26)

for i in range(key_length):
    for j in range(len(cipher_text_divided[i])):
        for m in range(26):
            if alphabet[m] == cipher_text_divided[i][j]:
                frequency_dictionary[i][m] += 1

    for m in range(26):
        frequency_dictionary[i][m] = frequency_dictionary[i][m] / len(
            cipher_text_divided[i]
        )

# Calculate letter frequency with an offset

shifted_frequencies = []

for i in range(key_length):
    shifted_frequencies.append([])
    for j in range(26):
        shifted_frequencies[i].append([])
        for m in range(26):
            shifted_frequencies[i][j].append(frequency_dictionary[i][(m + j) % 26])

# Calculate the Euclidean distance

euclidean_distance = []
for i in range(key_length):
    euclidean_distance.append([0] * 26)

for i in range(key_length):
    for j in range(26):
        for m in range(26):
            euclidean_distance[i][j] += (
                shifted_frequencies[i][j][m] - english_freq[m]
            ) ** 2

# Determining the positions of the letters that serve as keys

key_numbers = []

for i in range(key_length):
    key_numbers.append(euclidean_distance[i].index(min(euclidean_distance[i])))

# Decrypting the ciphertext

key_text = key_numbers * (
    (len(cipher_text) // key_length) + 1
)  # Generating the required key length

plain_text = ""

for i in range(len(cipher_text)):
    c = alphabet.index(cipher_text[i])
    k = key_text[i]
    plain_text += alphabet[(c - k) % 26]

# Finding the keyword

key_word = ""

for i in range(len(key_numbers)):
    key_word += alphabet[key_numbers[i]]

print("Text encrypted: ", plain_text, "\nKey word: ", key_word)