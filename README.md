# Vigenère Cipher Breaker
 
A Python script that recovers the key of a Vigenère cipher and decrypts the ciphertext, without knowing the key in advance. It uses the index of coincidence to find the key length and frequency analysis with Euclidean distance to find each letter of the key.
 
## Requirements
 
- Python 3
- No external libraries
## Usage
 
```bash
python main.py
```
 
The program asks for two inputs:
 
1. **Ciphertext** — the encrypted text.
2. **Maximum key length** — the longest key length to test (for example, `20`).
Example:
 
```
Input the data:
 
Ciphertext:
<your ciphertext>
Maximum length the key:
20
```
 
The program prints the decrypted text and the recovered key word.
 
### Input requirements
 
- The ciphertext must contain **only lowercase Latin letters (a–z)**: no spaces, punctuation, digits or uppercase letters.
- The plaintext must be in **English**, since the letter frequencies used for the analysis are those of English.
- The text should be long enough for statistical analysis. A few hundred characters or more gives reliable results; very short texts may produce a wrong key.
- The maximum key length must be smaller than the length of the ciphertext.
## How it works
 
### Step 1: Finding the key length
 
The ciphertext is compared with itself shifted by 1, 2, …, *max* positions. For each shift *L*, the program counts the positions where the letters match and divides by the number of comparisons:
 
$$
\frac{\sum_{j=1}^{N-L} [a_j = a_{j+L}]}{N-L}
$$
 
When the shift equals the key length (or a multiple of it), letters encrypted with the same key letter line up, so the share of matches is close to that of ordinary English text (about 0.065). For other shifts, it is close to that of random text (about 0.038). The shift with the highest share of matches is taken as the key length.
 
### Step 2: Finding the key letters
 
1. **Split into columns.** The ciphertext is split into *k* columns, where *k* is the key length. Column *i* contains the letters at positions *i*, *i + k*, *i + 2k*, …, all encrypted with the same key letter.
2. **Letter frequencies.** For each column, the frequency of each of the 26 letters is calculated.
3. **Trying all shifts.** For each column, all 26 possible key letters are tried. For key letter number *s*, the frequency vector is rotated so that it matches the frequencies of the column decrypted with that letter.
4. **Euclidean distance.** Each rotated vector is compared with the standard English letter frequencies, using the (squared) Euclidean distance:
$$
d = \sum_{i=1}^{26} (f_i - e_i)^2
$$
 
5. **Choosing the key letter.** The shift with the smallest distance, meaning the decrypted column looks most like English, gives the key letter for that column.
### Step 3: Decryption
 
Each ciphertext letter is decrypted with the corresponding key letter:
 
$$
p_i = (c_i - k_{i \bmod k}) \bmod 26
$$
 
## Limitations
 
- Only lowercase English letters are supported; any other character causes an error.
- The key length is chosen as the shift with the highest coincidence rate. Multiples of the true key length (for example, 16 instead of 8) score similarly high, so if the maximum key length is large, the program may occasionally choose a multiple. The decryption is still correct in that case, but the key word is repeated (for example, `lemonlemon` instead of `lemon`).
- On short texts, individual key letters may be wrong. This shows up as incorrect letters at regular intervals in the decrypted text.