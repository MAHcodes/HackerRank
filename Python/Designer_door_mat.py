# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,input().split())
pattern = ".|."
counter = 1

while counter < N :
    print((pattern * counter).center(M, "-"))
    counter += 2
print("WELCOME".center(M, "-"))
while counter > 1:
    counter -= 2
    print((pattern * counter).center(M, "-"))
