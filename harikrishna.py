# || Swami-Shriji ||

import logging

logger = logging.getLogger(__name__)

ascii_substitutions = {
  'aa' : 'A',
  'ee' : 'I',
}

ascii_consonants = [
  'b', 'c', 'd', 'D', 'f', 'g', 'h', 'j', 'k','l', 'L', 'm', 'n', 'N', 'p', 'r', 's',
  'S', 't', 'T', 'v', 'w', 'y', 'z']

ascii_vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'R']

harikrishna_vowels = ['a', 'ai']

harikrishna_letters = {

  # Consonants
  'k' : 'k',
  'kh': 'K',
  'g' : 'g',
  'gh': 'G',
  'c' : 'c',
  'ch': 'C',
  'j' : 'j',
  'jh': 'z',
  'z' : 'z',
  'T' : 'T',
  'Th': 'q',
  'D' : 'D',
  'Dh': 'Q',
  'N' : 'N',
  't' : 'Ri',
  'th': 'Y',
  'd' : 'd',
  'dh': 'F',
  'n' : 'n',
  'p' : 'p',
  'ph': 'f',
  'b' : 'b',
  'bh': 'B',
  'm' : 'm',
  'y' : 'y',
  'r' : 'r',
  'l' : 'l',
  'v' : 'v',
  'sh': 'S',
  's' : 's',
  'h' : 'h',
  'Sh': 'P',
  'L' : 'L',

  # Vowels
  ' ' : ' ',
  '.' : '.',
  'a' : 'a',
  'A' : 'ai',
  'i' : 'e',
  'I' : 'E',
  'u' : 'u',
  'U' : 'U',
  'e' : 'a[',
  'E' : 'aƒ',
  'ai': 'a]',
  'o' : 'ai[',
  'O' : 'aiƒ',
  'au': 'ai]',
  'aM': 'a>',
  'aH': 'a:',

  # Conjuncts
  'kk' : 'Ê',
  'kr' : "k|",
  'kl' : '±l',
  'kt' : '±Ri',
  'jj' : 'Ì',
  'jr' : 'Õ',
  'TT' : 'Í',
  'Dr' : 'D^',
  'tt' : '_i',
  'ttv': '_v',
  'tr' : '3i',
  'str': 'A#i',
  'hy' : 'H',
  'hm' : 'M',
  'kSh': 'x',
  'gN' : 'X',
  'ru' : '@',
  'rU' : '$',
  'shv': 'V',
  'dr' : 'W',
  'dR' : 'Ø',
  'dy' : 'w',
  'dv' : 'o',
  'aM' : 'a>',
  'sm' : 'sm',
  'dd' : 'Ñ',
  'ddh': 'Ü',
  'nn' : 'Ò',
  'nm' : 'ºm',
  'nmy': 'ºÀy',
  'vy' : 'Äy',
  'ly' : 'Ãy',
  'ShT': 'Ö',
  'ShN': 'ON',
  'ShTh':'×',
  'shy': b'\xC5\x00'.decode('utf-16')+'y',
  'shv': b'\xC5\x00'.decode('utf-16')+'v',
  'shw': b'\xc5\x00'.decode('utf-16')+'v',
  'shr': '~',
  'sv' : 'Av',
  'sw' : 'Av',
  'pr' : 'p\\',
  'pn' : '¼n',

  'by' : '¾y',
  'br' : 'b|',
  'bhy': '¿y',
  'bhr': 'B\\',


  # r-conjuncts
  'rk':'k<',
  'rkh':'K<',
  'rg':'g<',
  'rgh':'G<',
  'rc':'c<',
  'rch':'C<',
  'rj':'j<',
  'rjh':'z<',
  'rT':'T<',
  'rTh':'q<',
  'rD':'D<',
  'rDh':'Q<',
  'rN':'N<',
  'rt':'Ri<',
  'rth':'y<',
  'rd':'d<',
  'rdh':'f<',
  'rn':'n<',
  'rp':'p<',
  'rph':'f<',
  'rb':'b<',
  'rbh':'B<',
  'rm':'m<',
  'ry':'y<',
  'rr':'r<',
  'rl':'l<',
  'rv':'v<',
  'rsh':'S<',
  'rs':'s<',
  'rh':'h<',
  'rSh':'P<',
  'rL':'L<',

  # Special characters
  '.' : '.',
  ' ' : ' ',
  ',' : ',',
  'M' : '>',
  '+' : '',

}

harikrishna_diacritics = {
  'A' : 'i',
  'aa': 'i',
  'i' : '(',
  'I' : ')',
  'u' : '&',
  'U' : '*',
  'e' : '[',
  'E' : 'ƒ',
  'ai': ']',
  'o' : 'i[',
  'au': 'i]',
  'O' : 'iƒ',
  'aM': '>',
  'R' : 'Z'

}

def hk_pattern(pattern : str) -> str:

  try:
    result = harikrishna_letters[pattern]
    logger.info(f'Found {pattern} in letters dictionary as {result}.')
    return result
  except:
    logger.warning(f'Unable to find {pattern} in letters dictionary.')
    return ''

def hk_diacritic(pattern : str) -> str:
  try:
    result = harikrishna_diacritics[pattern]
    logger.info(f'Found {pattern} in diacritics dictionary as {result}.')
    return result
  except:
    logger.warning(f'Unable to find {pattern} in diacritics dictionary.')
    return ''


def is_consonant(pattern : str) -> bool:
  if pattern in ascii_consonants:
    logger.info(f'{pattern} is a consonant.')
    return True
  logger.info(f'{pattern} is not a consonant.')
  return False

def is_vowel(pattern : str) -> bool:
  if pattern in ascii_vowels:
    logger.info(f'{pattern} is a vowel.')
    return True
  logger.info(f'{pattern} is not a vowel.')
  return False

def remove_virama(input : str) -> str:
  if input[-1] == VIRAMA:
    logger.info(f'Removing last virama from {input}.')
    return input[:-1]
  return input

# def replace_conjunct_r(input : str) -> str:

#   # Get letter values
#   letters = harikrishna_letters.values()

#   i : int = 0

#   flag = False

#   # Iterate and look for 'r`'
#   while i < len(input) - 2:
#     if input[i] + input[i+1] == 'r`':
#       flag = True
#       logger.info('Found a truncated r!')
#     # Find the next vowel

#     i += 1

VIRAMA = '`'
AVAGRAH = 'ઽ'
DUMMY_CHARACTER = '+'
CHANDRA = '<'

def ascii_to_harikrishna(word : str) -> str:

  hk_word = ''
  i = 0
  r_flag = False
  # Iterate through each letter
  while i < len(word):

    c = word[i]

    # --------------- Vowels -------------------

    # a based vowels
    if c == 'a':

      # Only letter
      if len(word) == 1:
        hk_word += hk_pattern(c)

      # First letter
      elif i == 0:

        # ai, au, aM, aH
        if word[i+1] in ['a,','i', 'u', 'M', 'H']:
          hk_word += hk_pattern(c + word[i+1])
          i += 1

        else:
          hk_word += hk_pattern(c)

      # Last letter
      elif i == len(word) - 1:
        # Diacritics
        if is_consonant(word[i-1]):
          # Remove virama
          hk_word = remove_virama(hk_word)
          hk_word += DUMMY_CHARACTER
        else:
          hk_word += hk_pattern(c)
          hk_word += DUMMY_CHARACTER

      # General case
      else:
        # Diacritics
        if is_consonant(word[i-1]):
          # Remove virama
          hk_word = remove_virama(hk_word)

          # ai, au, aM, aH
          if word[i+1] in ['i', 'u', 'M', 'H']:
            hk_word += hk_diacritic(c + word[i+1])
            i += 1
            hk_word += DUMMY_CHARACTER

          else:
            hk_word += DUMMY_CHARACTER

        # Standalone
        else:
          # ai, au, aM, aH
          if word[i+1] in ['i', 'u', 'M', 'H']:
            hk_word += hk_pattern(c + word[i+1])
            i += 1
          # a
          else:
            hk_word += hk_pattern(c)

    # i
    elif c == 'i':

      # First or only letter
      if i == 0:
        hk_word += hk_pattern(i)

      # Diacritic for a conjunct consonant
      # TODO: if all conditions are checked before branching, this will throw a
      # runtime exception if i is less than 2; in that case, add another if
      # statement
      elif i > 1 and is_consonant(word[i-1]) and is_consonant(word[i-2]):
        logger.info(f"Found a two consonant conjunct {word[i-2]} + {word[i-1]} with a dirgai 'i'.")

        # Remove virama
        hk_word = remove_virama(hk_word)

        # Add I before both consonants
        hk_word = '+'.join(hk_word.split('+')[:-2]) + 'I' + hk_word.split('+')[-1]
        #hk_word = hk_word[:-2] + 'I' + hk_word[-2] + hk_word[-1]

        # Add a dummy symbol to prevent additional diacritics to the conjunct;
        # this symbol will be removed at the end
        hk_word += DUMMY_CHARACTER

      # Diacritic for a singular consonant
      elif i > 0 and is_consonant(word[i-1]):
        logger.info(f"Found a singular consonant {word[i-1]} with a dirgai 'i'.")
        # Remove virama
        hk_word = remove_virama(hk_word)
        hk_word = hk_word[:-1] + '(' + hk_word[-1] + DUMMY_CHARACTER

      # Standalone vowel
      else:
        hk_word += hk_pattern(c)

    # All other vowels
    elif c in ['A', 'I', 'e', 'E', 'o', 'O', 'R', 'u', 'U']:

      # Only letter or first letter
      if i == 0:
        hk_word += hk_pattern(c)

      # Diacritic
      elif is_consonant(word[i-1]):
        # Remove virama
        hk_word = remove_virama(hk_word)
        # Add diacritic
        hk_word += hk_diacritic(c)
        hk_word += DUMMY_CHARACTER

      # Standalone
      else:
        hk_word += hk_pattern(c)

    # --------------- Special characters ----------- #
    elif c in ['.', ' ', '|','M', ',', '+']:
      hk_word += hk_pattern(c)

    # ----------------- Digits --------------------- #
    elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
      hk_word += c

    # --------------- Consonants ------------------- #

  # General case -> all other conjuncts and consonants
    else:

      # 4 consonant combos
      if i < len(word) - 3 and is_consonant(word[i+1]) and is_consonant(word[i+2]) and is_consonant(word[i+3]):
        if(hk_pattern(c + word[i+1] + word[i+2]) + word[i+3]) != '':
          hk_word += hk_pattern(c + word[i+1] + word[i+2] + word[i+3]) + VIRAMA
          i += 3

        if(hk_pattern(c + word[i+1] + word[i+2])) != '':
          hk_word += hk_pattern(c + word[i+1] + word[i+2]) + VIRAMA
          i += 2

        elif (hk_pattern(c + word[i+1])) != '':
          hk_word += hk_pattern(c + word[i+1]) + VIRAMA
          i += 1

        else:
          hk_word += hk_pattern(c) + VIRAMA

      # 3 consonant combos
      if i < len(word) - 2 and is_consonant(word[i+1]) and is_consonant(word[i+2]):
        if(hk_pattern(c + word[i+1] + word[i+2])) != '':
          hk_word += hk_pattern(c + word[i+1] + word[i+2]) + VIRAMA
          i += 2

        elif (hk_pattern(c + word[i+1])) != '':
          hk_word += hk_pattern(c + word[i+1]) + VIRAMA
          i += 1

        else:
          hk_word += hk_pattern(c) + VIRAMA

      # 2 consonant combos
      elif i < len(word) - 1 and is_consonant(word[i+1]):
        if(hk_pattern(c + word[i+1])) != '':
          hk_word += hk_pattern(c + word[i+1]) + VIRAMA
          i += 1

        else:
          hk_word += hk_pattern(c) + VIRAMA

      # ru and rU
      elif i < len(word) - 2 and c + word[i+1] in ['ru', 'rU']:
        hk_word += hk_pattern(c + word[i+1])
        i += 1

      # Aspirated consonants
      elif c in ['k', 'g', 'j', 'T', 'D', 't', 'd', 'p', 'b']:
        # Last letter in word
        if i == len(word) - 1:
          hk_word += hk_pattern(c) + VIRAMA
        # Aspirated consonant
        elif word[i+1] == 'h':
          hk_word += hk_pattern(c + 'h') + VIRAMA
          i += 1
        # Unaspirated consonant
        else:
          hk_word += hk_pattern(c) + VIRAMA

      else:
        # Add the virama to the consonant
        hk_word += hk_pattern(c) + VIRAMA

    i += 1
    logger.info(f'So far {hk_word}.')

  # Get rid of dummy characters
  hk_word = hk_word.replace('+','')
  logger.info("Removing dummy characters.")
  return hk_word



if __name__ == "__main__":

  logging.basicConfig(level=logging.INFO)
  logger.info('Running harikrishna.py as the main file.')

  print(ascii_to_harikrishna("artha"))












