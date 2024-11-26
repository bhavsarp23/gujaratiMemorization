# || Swami-Shriji ||

guj_hk_standalone_letters = {
  'a' : 'અ',
  'A' : 'આ',
  'i' : 'ઇ',
  'I' : 'ઈ',
  'u' : 'ઉ',
  'U' : 'ઊ',
  'R' : 'ઋ',
  'RR': 'ૠ',
  'E' : 'ઍ',
  'e' : 'એ',
  'ai': 'ઐ',
  'O' : 'ઑ',
  'o' : 'ઓ',
  'au': 'ઔ',
  'aM': 'ૐ',
  'k' : 'ક',
  'kh': 'ખ',
  'g' : 'ગ',
  'gh' : 'ઘ',
  'G' : 'ઙ',
  'c' : 'ચ',
  'ch': 'છ',
  'j' : 'જ',
  'jh' : 'ઝ',
  'J' : 'ઞ',
  'T' : 'ટ',
  'Th' : 'ઠ',
  'D' : 'ડ',
  'Dh' : 'ઢ',
  'N' : 'ણ',
  't' : 'ત',
  'th' : 'થ',
  'd' : 'દ',
  'dh' : 'ધ',
  'n' : 'ન',
  'p' : 'પ',
  'ph' : 'ફ',
  'b' : 'બ',
  'bh' : 'ભ',
  'm' : 'મ',
  'y' : 'ય',
  'r' : 'ર',
  'l' : 'લ',
  'v' : 'વ',
  'sh' : 'શ',
  'Sh' : 'ષ',
  's' : 'સ',
  'h' : 'હ',
  'L' : 'ળ',
  "'" : 'ઽ',
  '.' : '.',
}

guj_hk_diacritics = {
  'M' : b'\x82\x0A',
  'aM': b'\x82\x0A',
  'H' : b'\xB3\x0A',
  "'" : b'\xBD\x0A',
  'A' : b'\xBE\x0A',
  'i' : b'\xBF\x0A',
  'I' : b'\xC0\x0A',
  'u' : b'\xC1\x0A',
  'U' : b'\xC2\x0A',
  'R' : b'\xC3\x0A',
  'RR': b'\xC4\x0A',
  'E' : b'\xC5\x0A',
  'e' : b'\xC7\x0A',
  'ai': b'\xC8\x0A',
  'O' : b'\xC9\x0A',
  'o' : b'\xCB\x0A',
  'au': b'\xCC\x0A'
}

def is_vowel(letter: str) -> bool:
  if letter in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'R', 'RR', 'M', 'H']:
    return True
  return False


patterns = [
  'abc',
  'def',
  'fg',
  'gh',
  'ad'
]

def virama() -> str:
  return b'\xCD\x0A'.decode('utf-16')

def remove_virama(input : str) -> str:
  if input[-1] == virama():
    return input[:-1]
  return input

def hk_pattern(input_pattern : str) -> str:
  try:
    return guj_hk_standalone_letters[input_pattern] + ''
  except:
    print(f'Letter ({input_pattern}) is not present')
    return ''

def hk_diacritic(input: str) -> str:
  return (guj_hk_diacritics[input]).decode('utf-16')

def hk_simplify_patterns():
  pass

def hk_convert_word(word : str) -> str:
  word = word.split(' ')[0]
  i : int = 0
  hk_word : str = ''
  while i < len(word):
    c = word[i]
    # a based vowels
    if c == 'a':

      # Only letter
      if len(word) == 1:
        hk_word += hk_pattern(c)
      # First letter
      elif i == 0:

        # ai, au, aM, aH
        if word[i+1] in ['i', 'u', 'M', 'H']:
          hk_word += hk_pattern(c + word[i+1])
          i += 1
        else:
          hk_word += hk_pattern(c)
      # Last letter
      elif i == len(word) - 1:

        # Diacritic
        if not is_vowel(word[i-1]):
          # Remove virama
          hk_word = remove_virama(hk_word)

        # Regular vowel
        else:
          hk_word += hk_pattern(c)

      # General case
      else:

        # Diacritics
        if not is_vowel(word[i-1]):
          # Remove virama
          hk_word = remove_virama(hk_word)

          # ai, au, aM, aH
          if word[i+1] in ['i', 'u', 'M', 'H']:
            hk_word += hk_diacritic(c + word[i+1])
            i += 1

        # Standalone
        else:
          # ai, au, aM, aH
          if word[i+1] in ['i', 'u', 'M', 'H']:
            hk_word += hk_pattern(c + word[i+1])
            i += 1
          # a
          else:
            hk_word += hk_pattern(c)

    # All other vowels (except RR)

    elif c in ['A', 'i', 'I', 'e', 'E', 'o', 'O', 'R', 'u', 'U']:

      # Only letter or first letter
      if i == 0:
        hk_word += hk_pattern(c)

      # Diacritic
      elif not is_vowel(word[i-1]):
        # Remove virama
        hk_word = remove_virama(hk_word)
        # Add diacritic
        hk_word += hk_diacritic(c)

      # Standalone
      else:
        hk_word += hk_pattern(c)

    # Special case -> avagrah
    elif c == "'":
      hk_word += hk_pattern(c)

    # Special case -> consonants that can be aspirated
    elif c in ['k', 'g', 'j', 'T', 'D', 't', 'd', 'p', 'b', 's', 'S', 'c']:
      # Last letter in word
      if i == len(word) - 1:
        hk_word += hk_pattern(c) + virama()
      # Aspirated consonant
      elif word[i+1] == 'h':
        hk_word += hk_pattern(c + 'h') + virama()
        i += 1
      # Unaspirated consonant
      else:
        hk_word += hk_pattern(c) + virama()

    # General case -> all other standalone consonants
    else:
      # Add the virama to the consonant
      hk_word += hk_pattern(c) + virama()
    i += 1

  return hk_word

def ascii_to_guj(sentence : str) -> str:

  hk_sentence = ''

  for word in sentence.split(' '):
    hk_sentence += ' ' + hk_convert_word(word)

  return hk_sentence


if __name__=="__main__":

  sentence = "shva vaMca artha"

  hk_sentence = ''

  for word in sentence.split(' '):
    hk_sentence += ' ' + hk_convert_word(word)

  print(hk_sentence)




