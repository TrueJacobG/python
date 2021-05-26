import hashlib
from itertools import permutations
import time
import numpy as np

password = input("Type hashed password here: ")

start_time = time.time()


def decrypt_md5(password):
    chars = "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,!,#,$,%,&,',(,),*,+,,,-,.,/,:,;,<,=,>,?,@,[,\,],^,_,`,{,|,},~"

    list_chars = np.array(chars.split(","))
    test_password = ""

    for length in range(1, 1000):
        for p in permutations(list_chars, length):
            word = "".join(p)
            s_obj = hashlib.md5(word.encode())
            test_password = s_obj.hexdigest()

            print(word + "\033[91m" + " -> " + test_password + "\033[0m")

            if test_password == password:
                return word


word = decrypt_md5(password)

print("Password -> " + "\033[92m" + word + "\033[0m")
print("Time of execution: " +
      "\033[92m" + str(round(time.time() - start_time, 3)) + "\033[0m" + " seconds")
