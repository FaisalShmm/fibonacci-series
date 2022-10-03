nterms=int(input("How many terms:"))
#declare two numbers
n1,n2=0,1
count=0
#check if nterms is valid
if nterms<=0:
    print("Enter a positive integer")
elif nterms==1:
    print("Fibonacci series upto",nterms,":")
    print(n1)
else:
    print("Fibonacci series:")
    while(count<nterms):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1