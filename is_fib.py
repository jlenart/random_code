'''
First reads N, the number of tests
For each following line (up to N), determines if the integer entered appears in the fibonacci sequence

quick and dirty, easy recursive practice
'''
import sys

def fib(n,m,number):
   if m > number:
      print "IsNotFibo"
   elif (number==n or number==m):
      print "IsFibo"
   else:
      fib(m,n+m,number)

def iterate(num_tests):
   if num_tests == 0:
      exit(0)
   else:
      candidate = sys.stdin.readline()
      fib(0,1,int(candidate))
      iterate(num_tests-1)

def main():
   num_tests = sys.stdin.readline()
   iterate(int(num_tests))

main()
