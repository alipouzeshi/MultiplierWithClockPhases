def n_bit_adder(a,b):
    sum =[]
    c_out=0
    for i in range(len(a)-1,-1,-1):
        a_bit=int(a[i])
        b_bit=int(b[i])
        sum_out= a_bit ^ b_bit  ^ c_out
        c_out= (a_bit & b_bit) | (a_bit & c_out) | (b_bit & c_out) 
        sum.append(sum_out)
    sum.reverse()
    sum_str = ''.join(map(str, sum))
    return c_out,sum_str


def n_bit_subtractor(a,b):
    diff=[]
    borow=0
    for i in range(len(a)-1,-1,-1):
        a_bit=int(a[i])
        b_bit=int(b[i])
        diff_out = a_bit ^ b_bit ^ borow
        borow = ((not a_bit) & borow) | ((not a_bit) & b_bit) | ( b_bit & borow)
        diff.append(diff_out)
    diff.reverse()
    diff_str=''.join(map(str,diff))
    return diff_str,borow


def two_s_complement(N) :
    if N > 0 :
        return ( "0" + bin(N)[ 2 : ] )
    else: 
        n=bin(-N)[2:]
        result=[]
        count=0
        for i in range(len(n)-1 , -1 , -1 ):
            n_bit=int(n[i])
            if count== 1 :
                if n_bit == 1 :
                    result.append(0)
                else : 
                    result.append(1)            
            if n_bit == 0 and count == 0  :
                result.append(n_bit)
            elif n_bit == 1 and count == 0:
                result.append(n_bit)
                count = 1
        result.reverse()
        result_str= '1' + ''.join(map(str,result))
        return result_str


def unsigned_add_and_shift(A,B):
    outfile.write("unsigned add & shift multiplication\n")
    A_binary=bin(A)[2:]
    B_binary=bin(B)[2:]
    max_len = int_len
    A_binary = A_binary.zfill(max_len)
    B_binary = B_binary.zfill(max_len)
    outfile.write(f"A={A}={A_binary} , B={B}={B_binary}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    count1=0
    M="0"*(len(A_binary)) + B_binary
    outfile.write(f"( {count1} ,   ) M={M[:len(M)//2  + count1]}|{M[len(M) // 2  :]}\n")
    for i in range(len(M)-1,(len(M)//2)-1 ,-1):
        outfile.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")      
        M_bit=int(M[len(M)-1])
        if M_bit:
            res1,res2=n_bit_adder(A_binary,M[:len(M)//2])
            M = res2 + M[len(M) // 2:]
            outfile.write(f"( {count1} , + ) M={M[:len(M)//2 + count1 ]}|{M[len(M) // 2 +count1 :]}\n")
            if res1:
                count1 += 1
                M = "1"+ M[:len(M)-1]
                outfile.write(f'( {count1} , > ) M={M[:len(M)//2  + count1]}|{M[len(M) // 2 + count1 :]}                   overflow ocurred \n')
            else:
               M = "0" + M[:len(M)-1]
               count1 += 1
               outfile.write(f"( {count1} , > ) M={M[:len(M)//2  + count1]}|{M[len(M) // 2 + count1  :]}\n")
        else:
            count1 += 1
            M = "0" + M[:len(M)-1]
            outfile.write(f"( {count1} , > ) M={M[:len(M)//2  + count1]}|{M[len(M) // 2 + count1 :]}\n")
    outfile.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    outfile.write(f"M=AxB={int(A*B)}\n")
    outfile.write(f"-------------------------------------------------------------------------------------------------------------\n")

          

def signed_add_and_shift(A,B):
    outfile.write("signed add & shift multiplication\n")
    A_binary= two_s_complement(A)
    B_binary= two_s_complement(B)
    max_len = int_len
    A_sign_bit = A_binary[0]
    B_sign_bit = B_binary[0]
    A_binary = A_sign_bit * (max_len - len(A_binary)) + A_binary
    B_binary = B_sign_bit * (max_len - len(B_binary)) + B_binary
    count=0
    outfile.write(f"A={A}={A_binary} , B={B}={B_binary}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    M="0"*(len(A_binary)) + B_binary
    outfile.write(f"( {count} ,   ) M={M[:len(M)//2  + count]}|{M[len(M) // 2  :]}\n")
    for i in range(len(M)-1,(len(M)//2)-1 ,-1):
        outfile.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        if i == len(M)//2 :
            M_bit=int(M[len(M)-1])
            if M_bit :
                res1,res2= n_bit_subtractor(M[:len(M)//2],A_binary)
                M = res1 + M[len(M) // 2:]
                outfile.write(f"( {count} , - ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
                if M[0] == "1" :
                    count+=1
                    M = "1" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
                else:
                    count+=1
                    M = "0" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")  
            else :
                 if M[0] == "1" :
                    count+=1
                    M = "1" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
                 else:
                    count+=1
                    M = "0" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
        else:
            M_bit=int(M[len(M)-1])
            if M_bit:
                res1,res2=n_bit_adder(A_binary,M[:len(M)//2])
                M = res2 + M[len(M) // 2:]
                outfile.write(f"( {count} , + ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
                if M[0] == "1" :
                    count+=1
                    M = "1" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
                else:
                    M = "0" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M}\n")
            else:
                if M[0] == "1" :
                    count+=1
                    M = "1" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
                else:
                    count+=1
                    M = "0" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
    outfile.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if A*B >0 :
        outfile.write(f"M=AxB=+{int(A*B)}\n")
    else:
        outfile.write(f"M=AxB={int(A*B)}\n")
    outfile.write(f"--------------------------------------------------------------------------------------------------------------\n")

    
def  signed_booth(A,B):
    outfile.write("Booth multiplication\n")
    A_binary= two_s_complement(A)
    B_binary= two_s_complement(B)
    max_len = int_len
    A_sign_bit = A_binary[0]
    B_sign_bit = B_binary[0]
    A_binary = A_sign_bit * (max_len - len(A_binary)) + A_binary
    B_binary = B_sign_bit * (max_len - len(B_binary)) + B_binary
    count=0
    outfile.write(f"A={A}={A_binary} , B={B}={B_binary}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    M="0"*(len(A_binary)) + B_binary + "0"
    outfile.write(f"( {count} ,   ) M={M[:len(M)//2  + count]}|{M[len(M) // 2  :]}\n")
    for i in range(len(M)-1,(len(M)//2),-1):
        outfile.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        M_bits=M[len(M)-2:len(M)]
        if M_bits == "10" :
            res1,res2= n_bit_subtractor(M[:len(M)//2],A_binary)
            M = res1 + M[len(M) // 2:]
            outfile.write(f"( {count} , - ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
            if M[0] == "1" :
                         count+=1
                         M = "1" + M[:len(M)-1]
                         outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
            else:
                 count+=1
                 M = "0" + M[:len(M)-1]
                 outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
        elif M_bits == "01" :
            res1,res2=n_bit_adder(A_binary,M[:len(M)//2 ])
            M = res2 + M[len(M) // 2:]
            outfile.write(f"( {count} , + ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
            if M[0] == "1" :
                    count+=1
                    M = "1" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
            else:
                 count+=1
                 M = "0" + M[:len(M)-1]
                 outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
        else :
            if M[0] == "1" :
                    count+=1
                    M = "1" + M[:len(M)-1]
                    outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
            else:
                 count+=1
                 M = "0" + M[:len(M)-1]
                 outfile.write(f"( {count} , > ) M={M[:len(M)//2 + count ]}|{M[len(M) // 2 +count :]}\n")
    M=M[:len(M)-1]
    outfile.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if A*B >0 :
        outfile.write(f"M=AxB=+{int(A*B)}\n")
    else:
        outfile.write(f"M=AxB={int(A*B)}\n")
    outfile.write(f"------------------------------------------------------------------------------------------------------------\n")
    
with open("in.txt","r") as infile,open("out.txt","w") as outfile :
    batch_number= int(infile.readline().strip())
    for i in range(1,batch_number +1):

        algoritm_type=int(infile.readline().strip())
        int_len= int(infile.readline().strip())
        S=int(infile.readline().strip())
        A=int(infile.readline().strip())
        B=int(infile.readline().strip())
        outfile.write(f"out-{i}\n")
        if algoritm_type == 0 :
            if S == 0 :
                unsigned_add_and_shift(A,B)
            else : 
                signed_add_and_shift(A,B)
        else: 
            signed_booth(A,B)