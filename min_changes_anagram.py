# Determine the number of changes necessary to make an anagram of two strings
# Pre-condition: strings must be of equal length
# no error checking so this will choke on any bad input

# 1: check length, fails if %2 != 0
# 2: iterate chars of front half +1 to each seen
# 3: iterate chars of back half -1 to each seen
# 4: sum only positive values (negative implies exists in only 1 string and is already accounted for and 0 is appears equally in both)

from string import ascii_lowercase

def count_changes(string):
   letters = {}
   sum = 0
   for c in ascii_lowercase:
      letters[c] = 0

   if len(string) % 2 == 1:
      return -1
   else:
      for c in string[:len(string)/2]:
         letters[c] +=1
      for c in string[len(string)/2:]:
         letters[c] -=1
      for key in letters:
         if letters[key] > 0:
            sum+=letters[key]

      return sum
         


def main():
   num_tests = int(raw_input())
   strings = []
   for i in range(num_tests):
      strings.append(raw_input())

   for s in strings:
      print count_changes(s)


main()
