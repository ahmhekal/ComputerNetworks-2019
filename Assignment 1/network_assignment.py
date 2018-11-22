

def xor(a, b):

    result = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)




def mod2div(divident, divisor):

    pick = len(divisor)

    tmp = divident[0 : pick]

    while pick < len(divident):

        if tmp[0] == '1':

            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0'*pick, tmp) + divident[pick]

        pick += 1


    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword




def Generator(data, key):

    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)

    codeword = data + remainder
    print("Remainder : ", remainder)
    print("Transmitted message (Data + Remainder) : ",
          codeword)
    return codeword




def verifier(codeword, key):
    reminder=mod2div(codeword, key)
    if int(reminder)==0:
        print("correct")

    else:
        print("incorrect")





def alter(index,codeword) :
    bit=int(codeword[index-1])^1
    codeword=codeword[:index-1]+str(bit)+codeword[index:]
    return codeword





def CRC (command,data,key):
    if "alter" in command:
        index=command.find("alter")
        index=index+6
        index=int(command[index])
        codeword=Generator(data, key)
        codeword=alter(index,codeword)
        verifier(codeword, key)

    else:
        codeword=Generator(data, key)
        verifier(codeword, key)



"""
# generator test case

message="1101011111"
key="10011"
Generator(message, key)


# In[27]:


# alter test case
Transmitted_m="11001"
index=3
new=alter(index,Transmitted_m)
new


# In[28]:


# verifier without alter test case
message="1101011111"
key="10011"
codeword=Generator(message, key)
verifier(codeword, key)


# In[29]:


# verifier with alter test case
message="1101011111"
key="10011"
codeword=Generator(message, key)
codeword_after_alter=alter(3,codeword)
print("message after alter",codeword_after_alter)
verifier(codeword_after_alter, key)

"""
# # Program

# In[ ]:

while(True):
    command=input("please enter the command ")
    c=command.split()
    file_name=c[1][1:]
    file = open(file_name, 'r')
    lines = file.readlines()
    message=lines[0][:-1]
    key=lines[1]
    CRC (command,message,key)
    INput=input("enter exit to exit the program or anything else to try another command")
    if(INput=="exit"):
        break
