import random
import string

def generate_password(l):
    ch=string.ascii_letters+string.digits+'_'  #or use string.punctuation
    pwd=''.join(random.choice(ch) for _ in range(l))
    return pwd

def main():
    l=int(input('Enter the desired length of password:'))
    password=generate_password(l)
    print('Generate password:',password)

if __name__ == '__main__':
    main()
    
