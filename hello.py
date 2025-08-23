# Simple Python program
def greet(name="Rishita"):
    print(f"Hello, GitHub from Python! Hi {name} 👋")
if __name__ == "__main__":
 greet()


#Write the program to find & count character enter by user
a=input("Enter string=")
print("string is : ",a)

ch=input("Enter character which you want to find:")
le=len(a)
count=0

for i in range(0,le):
    if(a[i]==ch):
        count=count+1
if(count==0):
    print("Character is not present")
else:
    print("Character present",count,"times")
