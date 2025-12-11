print("kaç sayi gireceksin?")
a=int(input())
prev=0
current=1

for i in range (0,a):
    nextone=prev+current
    
    prev=current
    current=nextone
print(current)
