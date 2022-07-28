const = ['h', 'k', 'm', 'n', 'ng', 'p', 'r', 't', 'w', 'wh']
const2 = ['h', 'k', 'm', 'n', 'ng', 'p', 'r', 't', 'w', 'wh','']
vowel = ['a','e', 'i', 'o', 'u','aa','ee','ii','oo','uu']
import random
rand1 = random.randint(0,2)
word = const[random.randint(0,9)]+vowel[random.randint(0,9)]
word2 = const2[random.randint(0,10)]+vowel[random.randint(0,9)]
word3 = const2[random.randint(0,10)]+vowel[random.randint(0,9)]
word4 = const2[random.randint(0,10)]+vowel[random.randint(0,9)]
if rand1 == 0:
  print(word+word2+word3)
elif rand1 == 1:
  print(word+word2)
elif rand1 == 2:
  print(word+word2+word3)
elif rand1 == 3:
  print(word+word2)