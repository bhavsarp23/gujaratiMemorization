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
  'f' : 'f',
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
  'H' : ':',
  'aum':'ú',

  # Conjuncts
  'kk' : 'Ê',
  'kr' : "k|",
  'kl' : '±l',
  'kt' : '±Ri',
  'ky' : '±y',
  'khy': '²y',
  'khr': 'K\\',
  'kSh': 'x',
  'gN' : 'X',
  'gr' : 'g\\',
  'gy' : '³y',
  'cch': 'µC',
  'jA' : 'Ô',
  'jI' : 'J',
  'jj' : 'Ì',
  'jr' : 'Õ',
  'TT' : 'Í',
  'Dr' : 'D^',
  'tt' : '_i',
  'tn' : 'Rn',
  'ttv': '_v',
  'tr' : '3i',
  'tm' : 'Rm',
  'tp' : 'Rp',
  'ty' : 'Ry',
  'ts' : 'Rs',
  'str': 'A#i',
  'hy' : 'H',
  'hm' : 'M',
  'ru' : '@',
  'rU' : '$',
  'shv': 'V',
  'shw': 'V',
  'dhy': '¹y',
  'dr' : 'W',
  'dR' : 'Ø',
  'dy' : 'w',
  'dv' : 'o',
  'aM' : 'a>',
  'sm' : 'Am',
  'dd' : 'Ñ',
  'ddh': 'Ü',
  'nt' : 'ºRi',
  'nn' : 'Ò',
  'nm' : 'ºm',
  'ny' : 'ºy',
  'nmy': 'ºÀy',
  'vy' : 'Äy',
  'ly' : 'Ãy',
  'll' : 'Ãl',
  'lp' : 'Ãp',
  'Ly' : 'Çy',
  'Shp': 'Op',
  'ShT': 'Ö',
  'ShN': 'ON',
  'ShTh':'×',
  'Shy': 'Oy',
  'shy': b'\xC5\x00'.decode('utf-16')+'y',
  'shr': '~',
  'sp' : 'Ap',
  'sv' : 'Av',
  'sw' : 'Av',
  'pr' : 'p\\',
  'pn' : '¼n',
  'py' : '¼y',

  'by' : '¾y',
  'br' : 'b\\',
  'bhy': '¿y',
  'bhr': 'B\\',
  'mb' : 'Àb',
  'mbh': 'ÀB',


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
  '-' : '-',
  "'" : "'",
  '!' : '!',
  '?' : '?',
  '"' : '"',
  "'" : "'",

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
  'R' : 'Z',
  'H' : ':',

}

unicode_diacritics = {

  'A' : 'ા',
  'i': 'િ',
  'I': 'ી',
  'u': 'ુ',
  'U': 'ૂ',
  'e': 'ે',
  'E': 'ૅ',
  'ai': 'ૈ',
  'o': 'ો',
  'au': 'ૌ',
  'O': 'ૉ',
  'aM': 'ં',
  'R': 'ૃ',
  'H': 'ઃ',
  
}


unicode_letters = {

  # Consonants
  'k' : 'ક',
  'kh': 'ખ',
  'g' : 'ગ',
  'gh': 'ઘ',
  'Z' : 'ઙ',
  'c' : 'ચ',
  'ch': 'છ',
  'j' : 'જ',
  'jh': 'ઝ',
  'J' : 'ઞ',
  'T' : 'ટ',
  'Th': 'ઠ',
  'D' : 'ડ',
  'Dh': 'ઢ',
  'N' : 'ણ',
  't' : 'ત',
  'th': 'થ',
  'd' : 'દ',
  'dh': 'ધ',
  'n' : 'ન',
  'p' : 'પ',
  'ph': 'ફ',
  'f' : 'ફ',
  'b' : 'બ',
  'bh': 'ભ',
  'm' : 'મ',
  'y' : 'ય',
  'r' : 'ર',
  'l' : 'લ',
  'v' : 'વ',
  'sh': 'શ',
  's' : 'સ',
  'h' : 'હ',
  'Sh': 'ષ',
  'L' : 'ળ',

  # Vowels
  ' ' : ' ',
  '.' : '.',
  'a' : 'અ',
  'A' : 'આ',
  'i' : 'ઇ',
  'I' : 'ઈ',
  'u' : 'ઉ',
  'U' : 'ઊ',
  'e' : 'એ',
  'ai' : 'ઐ',
  'o' : 'ઓ',
  'au' : 'ઔ',
  'E' : 'ઍ',
  'O' : 'ઑ',

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
  'H' : ':',
  'aum':'ú',

  # Conjuncts
  'kk' : 'ક્ક',
  'kr' : 'ક્ર',
  'kl' : 'ક્લ',
  'kt' : 'ક્ત',
  'ky' : 'ક્ય',
  'khy': 'ખ્ય',
  'khr': 'ખ્ર',
  'kSh': 'ક્ષ',
  'gN' : 'જ્ઞ',
  'gr' : 'ગ્ર',
  'gy' : 'ગ્ય',
  'cch': 'ચ્ચ',
  'jA' : 'જા',
  'jI' : 'જી',
  'jj' : 'જ્જ',
  'jr' : 'જ્ર',
  'TT' : 'ટ્ટ',
  'Dr' : 'ડ્ડ',
  'tt' : 'ત્ત',
  'tn' : 'ત્ન',
  'tv' : 'ત્વ',
  'ttv': 'ત્ત્વ',
  'tr' : 'ત્ર',
  'tm' : 'ત્મ',
  'tp' : 'ત્પ',
  'ty' : 'ત્ય',
  'ts' : 'ત્સ',
  'str': 'સ્ત્ર',
  'hy' : 'હ્ય',
  'hm' : 'હ્મ',
  'ru' : 'રુ',
  'rU' : 'રૂ',
  'shv': 'શ્વ',
  'shw': 'શ્વ',
  'dhy': 'ધ્ય',
  'dr' : 'દ્ર',
  'dR' : 'દૃ',
  'dy' : 'દ્ય',
  'dv' : 'દ્વ',
  'aM' : 'અં',
  'sm' : 'સ્મ',
  'dd' : 'દ્દ',
  'ddh': 'દ્ધ',
  'nt' : 'ન્ત',
  'nn' : 'ન્ન',
  'nm' : 'ન્મ',
  'ny' : 'ન્ય',
  'nmy': 'ન્મ્ય',
  'vy' : 'વ્ય',
  'ly' : 'લ્ય',
  'll' : 'લ્લ',
  'lp' : 'લ્પ',
  'Ly' : 'ળ્ય',
  'shp': 'શ્પ',
  'Shp': 'ષ્પ',
  'ShT': 'ષ્ટ',
  'ShN': 'ષ્ણ',
  'ShTh':'ષ્ઠ',
  'Shy': 'ષ્ય',
  'shy': 'શ્ય',
  'shr': 'શ્ર',
  'sp' : 'સ્પ',
  'sv' : 'સ્વ',
  'sw' : 'સ્વ',
  'pr' : 'પ્ર',
  'pn' : 'પ્ન',
  'py' : 'પ્ય',
  'by' : 'બ્ય',
  'br' : 'બ્ર',
  'bhy': 'ભ્ય',
  'bhr': 'ભ્ર',
  'mb' : 'મ્બ',
  'mbh': 'મ્ભ',

  # r-conjuncts
  'rk' : 'ર્ક',
  'rkh': 'ર્ખ',
  'rg' : 'ર્ગ',
  'rgh': 'ર્ઘ',
  'rc' : 'ર્ચ',
  'rch': 'ર્છ',
  'rj' : 'ર્જ',
  'rjh': 'ર્ઝ',
  'rT' : 'ર્ટ',
  'rTh': 'ર્ઠ',
  'rD' : 'ર્ડ',
  'rDh': 'ર્ઢ',
  'rN' : 'ર્ણ',
  'rt' : 'ર્ત',
  'rth': 'ર્થ',
  'rd' : 'ર્દ',
  'rdh': 'ર્ધ',
  'rn' : 'ર્ન',
  'rp' : 'ર્પ',
  'rph': 'ર્ફ',
  'rb' : 'ર્બ',
  'rbh': 'ર્ભ',
  'rm' : 'ર્મ',
  'ry' : 'ર્ય',
  'rr' : 'ર્ર',
  'rl' : 'ર્લ',
  'rv' : 'ર્વ',
  'rsh': 'ર્શ',
  'rs' : 'ર્સ',
  'rh' : 'ર્હ',
  'rSh': 'ર્ષ',
  'rL' : 'ર્ળ',

  # Special characters
  '.' : '.',
  ' ' : ' ',
  ',' : ',',
  'M' : '>',
  '+' : '',
  '-' : '-',
  "'" : "'",
  '!' : '!',
  '?' : '?',
  '"' : '"',
  "'" : "'",

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
#VIRAMA = '્'
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
        hk_word += hk_pattern(c) + DUMMY_CHARACTER

      # First letter
      elif i == 0:

        if len(word) > 2 and c + word[i+1] + word[i+2] == 'aum':
          hk_word += hk_pattern(c + word[i+1] + word[i+2]) + DUMMY_CHARACTER
          i += 2

        # ai, au, aM, aH
        elif word[i+1] in ['a,','i', 'u', 'M', 'H']:
          hk_word += hk_pattern(c + word[i+1]) + DUMMY_CHARACTER
          i += 1

        else:
          hk_word += hk_pattern(c) + DUMMY_CHARACTER

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

          if i < len(word) - 3 and c + word[i+1] + word[i+2] == 'aum':
            hk_word += hk_pattern(c + word[i+1] + word[i+2]) + DUMMY_CHARACTER
            i += 2

          # ai, au, aM, aH
          elif word[i+1] in ['i', 'u', 'M', 'H']:
            hk_word += hk_pattern(c + word[i+1]) + DUMMY_CHARACTER
            i += 1
          # a
          else:
            hk_word += hk_pattern(c) + DUMMY_CHARACTER

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
        if len(hk_word.split('+')[-1]) > 1:
          # Add an I
          hk_word = '+'.join(hk_word.split('+')[:-1]) + 'I' + hk_word.split('+')[-1]
        else:
          hk_word = '+'.join(hk_word.split('+')[:-1]) + '(' + hk_word.split('+')[-1]
        #hk_word = hk_word[:-2] + 'I' + hk_word[-2] + hk_word[-1]

        # Add a dummy symbol to prevent additional diacritics to the conjunct;
        # this symbol will be removed at the end
        hk_word += DUMMY_CHARACTER

      # Diacritic for a singular consonant
      elif i > 0 and is_consonant(word[i-1]):
        logger.info(f"Found a singular consonant {word[i-1]} with a dirgai 'i'.")
        # Remove virama
        hk_word = remove_virama(hk_word)
        # Add ( before consonant
        hk_word = '+'.join(hk_word.split('+')[:-1]) + '(' + hk_word.split('+')[-1]

      # Standalone vowel
      else:
        hk_word += hk_pattern(c) + DUMMY_CHARACTER

    # All other vowels
    elif c in ['A', 'I', 'e', 'E', 'o', 'O', 'R', 'u', 'U', 'H']:

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
        hk_word += hk_pattern(c) + DUMMY_CHARACTER

    # --------------- Special characters ----------- #
    elif c in ['.', ' ', '|','M', 'H', ',', '+', '-', "'", '?', '!', "'", '"']:
      hk_word += hk_pattern(c) + DUMMY_CHARACTER

    # ----------------- Digits --------------------- #
    elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
      hk_word += c + DUMMY_CHARACTER

    # --------------- Consonants ------------------- #

  # General case -> all other conjuncts and consonants
    else:

      # 4 consonant combos
      if i < len(word) - 3 and is_consonant(word[i+1]) and is_consonant(word[i+2]) and is_consonant(word[i+3]):
        if(hk_pattern(c + word[i+1] + word[i+2]) + word[i+3]) != '':
          hk_word += hk_pattern(c + word[i+1] + word[i+2] + word[i+3]) + VIRAMA
          i += 3

        elif(hk_pattern(c + word[i+1] + word[i+2])) != '':
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

      # ji and jI
      elif i < len(word) - 2 and c + word[i+1] in ['jA', 'jI']:
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












