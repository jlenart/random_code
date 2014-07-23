def reversebinary(n):
   return int(bin(n)[:1:-1],2)

def main():
   num = raw_input()
   print reversebinary(int(num))

main()
