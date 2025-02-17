# || Swami-Shriji ||

from difflib import SequenceMatcher, ndiff
import harikrishna

def similar(a,b):
  return SequenceMatcher(None,a,b).ratio()

def compare(a,b) -> [str, float]:
  diff_str = ''.join(ndiff(a,b))
  ratio = SequenceMatcher(None,a,b).ratio()
  return diff_str, ratio

def open_mp_file(file_path : str) -> list:
  with open(file_path, 'r') as f:
    return f.readlines()

def test_fx():
  a = 'aj[ yXp&@Pn[ oir ni[bRi'
  b = 'aj[ yXp&@Pn[ oa ni[bRi'
  diff = ndiff(a,b)

  print(''.join(diff))
  print(similar(a,b))


if __name__ == "__main__":

  # Mukhpath lines
  mukhpath = []

  # Open sample.txt
  with open('sample.txt', 'r') as f:
    mukhpath = f.readlines()

  print(mukhpath)
