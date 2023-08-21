
import os
if __name__=='__main__':
    print("welcome to robo-speaker 1.1 Created by Lakshya")
    while True:
        x=input("enter what you want me to say:")
        if(x=="q"):
            os.system("say 'bye bye friend' ")
            break
        command=f"say {x}"
        os.system(command)
