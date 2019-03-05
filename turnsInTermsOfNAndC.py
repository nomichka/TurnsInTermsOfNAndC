#N=2 C=2 Turns=4
"""
a=0
for i in range(1, 101):
    a+=(i*2)*0.5**i
print(a)
"""

#N=2 C=3 Turns=9
"""
a=1
for i in range(1, 101):
    a+=(2*i)*(3**(i-1))/(4**i)
print(a)
"""

#N=2 C=4 Turns=16
"""
a=1
b=1
final=1
divider=2
for i in range(1, 101):
    divider*=4
    final+=(1+2*i)*a/divider
    c=a+2*b
    b=c
    a=a+c
print(final)
"""

#N=2 C=6,3 Turns=18
"""
a=3/32
b=1/32
c=9/32
d=5/32
e=5/16
final=3/8
for i in range(1, 1001):
    fina1+=a*(4+i)
    a=b/2
    bb=b
    b=c/2
    cc=c
    c=(bb+d)/2
    dd=d
    d=(cc+e)/2
    e=(dd+e)/2
print(final)
"""
#N=2 C=9,3 Turns=27
"""
a=1/4
b=1/2
c=1/4
final=0
for i in range(1, 1001):
    final+=((1+2*i)*a/2+(37+2*i)*c/2)
    aa=a
    bb=b
    cc=c
    a=(a+b)/4
    b=(aa+2*b+c)/4
    c=(bb+c)/4
print(final)
"""

#IN CONCLUSION: if N=2, then turns=C1*C2

#N=3 C=3 Turns=19.285714285714295, or 19_2/7
"""
final=0
for i in range(1, 40):
    final+=((2/9)**(i-1))*(15)
print(final)
"""

#N=3 C=4 Turns=35.111111111111114, or 31_1/9
"""
final=18+2/3
for i in range(1, 47):
    final+=((4/9)**i)*(i/9+(8/27)*(30+3*i)+(2/9)*(39+3*i))
print(final)
"""



#Enter N (number of players), C (coins per player,and R (how many rounds deep to explore):
N=int(input("N: "))
C=int(input("C: "))
R=int(input("R: "))

final=0 #Number of expected turns
abc=[[]] #All the combos, in the form of: [[round_1_combo], [round_2_combo_a, round_2_combo_b]], etc]
times=[[1]] #Number of ways to get a certain combo after a certain number of rounds

#Creating the initial combo
first=[] 
for i in range(N):
    first.append(C)
abc[0].append(first)

for i in range(1, R):
    #print(i, final, abc[i-1])
    if abc[i-1]==[]:
        break
    abc.append([])
    times.append([])
    if i!=1:
        abc[i-2]=[] #Making sure the super list doesn't get too long; might delete this part
    for j in range(len(abc[i-1])):
        combo=abc[i-1][j]
        old_multiplier=times[i-1][j]
        going=True
        
        #Getting rid of 0s in a combo, adding to final if left with only 1 or 2 nums in combo
        if 0 in combo:
            zeros=0
            for num in combo:
                if num==0:
                    zeros+=1
            while zeros>0:
                zeros-=1
                abc[i-1][j].remove(abc[i-1][j][combo.index(0)])
            if len(abc[i-1][j])==1:
                final+=old_multiplier*(i-1)/(N**(i-1))
                going=False
            elif len(abc[i-1][j])==2:
                final+=old_multiplier*(i-1+abc[i-1][j][0]*abc[i-1][j][1])/(N**(i-1))
                going=False

        #In new round, adding new combo or adding to the "number of ways to get" the new combo if new combo already exists
        #Note: [6, 2, 3] and [6, 3, 2] count as seperate combos
        if going:
            for k in range(len(combo)):
                new_combo=combo.copy()
                for l in range(len(new_combo)):
                    new_combo[l]-=1
                    if l==k:
                        new_combo[l]+=len(new_combo)
                if new_combo in abc[i]:
                    times[i][abc[i].index(new_combo)]+=old_multiplier
                else:
                    abc[i].append(new_combo)
                    times[i].append(old_multiplier)

#Correcting final if there are only two players
if N==2:
    final=C**2

print(final)




#Scrapped programs that try working with only three numbers;
#possible reference for some ideas of reducing redundancy
"""
a=20
b=20
c=20
final=0
abc=[[[a, b, c]]]
times=[[1]]
for i in range(1, 5000):
    #print(i, final, abc[i-1], times[i-1]) 
    #print(i, times[i-1], abc[i-1])
    if abc[i-1]==[]:
        break
        
    abc.append([])
    times.append([])
    for combo in abc[i-1]:
        a=combo[0]
        b=combo[1]
        c=combo[2]
        old_multiplier=times[i-1][abc[i-1].index(combo)]
        if a==0 and b==0 or a==0 and c==0 or b==0 and c==0:
            final+=old_multiplier*(i-1)/(3**(i-1))
        elif a==0:
            final+=old_multiplier*(i-1+b*c)/(3**(i-1))
        elif b==0:
            final+=old_multiplier*(i-1+a*c)/(3**(i-1))
        elif c==0:
            final+=old_multiplier*(i-1+a*b)/(3**(i-1))
        
        #elif a==b and b==c and i!=1:
        #    multiplier=old_multiplier/(3**(i-1))
        #    final1=final
        #    for j in range(1, 100):
        #        final+=(multiplier**j)*(final1)
        
        else:
            a_not_in=True
            b_not_in=True
            c_not_in=True
            #If the new version is already in the new level, don't make a new one; instead, add to the old one
            if [a+2, b-1, c-1] in abc[i]:
                times[i][abc[i].index([a+2, b-1, c-1])]+=old_multiplier
                a_not_in=False
            elif [a+2, c-1, b-1] in abc[i]:
                times[i][abc[i].index([a+2, c-1, b-1])]+=old_multiplier
                a_not_in=False
            elif [b-1, a+2, c-1] in abc[i]:
                times[i][abc[i].index([b-1, a+2, c-1])]+=old_multiplier
                a_not_in=False
            elif [c-1, a+2, b-1] in abc[i]:
                times[i][abc[i].index([c-1, a+2, b-1])]+=old_multiplier
                a_not_in=False
            elif [c-1, b-1, a+2] in abc[i]:
                times[i][abc[i].index([c-1, b-1, a+2])]+=old_multiplier
                a_not_in=False
            elif [b-1, c-1, a+2] in abc[i]:
                times[i][abc[i].index([b-1, c-1, a+2])]+=old_multiplier
                a_not_in=False
                
            if [b+2, a-1, c-1] in abc[i]:
                times[i][abc[i].index([b+2, a-1, c-1])]+=old_multiplier
                b_not_in=False
            elif [b+2, c-1, a-1] in abc[i]:
                times[i][abc[i].index([b+2, c-1, a-1])]+=old_multiplier
                b_not_in=False
            elif [a-1, b+2, c-1] in abc[i]:
                times[i][abc[i].index([a-1, b+2, c-1])]+=old_multiplier
                b_not_in=False
            elif [c-1, b+2, a-1] in abc[i]:
                times[i][abc[i].index([c-1, b+2, a-1])]+=old_multiplier
                b_not_in=False
            elif [c-1, a-1, b+2] in abc[i]:
                times[i][abc[i].index([c-1, a-1, b+2])]+=old_multiplier
                b_not_in=False
            elif [a-1, c-1, b+2] in abc[i]:
                times[i][abc[i].index([a-1, c-1, b+2])]+=old_multiplier
                b_not_in=False

            if [c+2, b-1, a-1] in abc[i]:
                times[i][abc[i].index([c+2, b-1, a-1])]+=old_multiplier
                c_not_in=False
            elif [c+2, a-1, b-1] in abc[i]:
                times[i][abc[i].index([c+2, a-1, b-1])]+=old_multiplier
                c_not_in=False
            elif [b-1, c+2, a-1] in abc[i]:
                times[i][abc[i].index([b-1, c+2, a-1])]+=old_multiplier
                c_not_in=False
            elif [a-1, c+2, b-1] in abc[i]:
                times[i][abc[i].index([a-1, c+2, b-1])]+=old_multiplier
                c_not_in=False
            elif [a-1, b-1, c+2] in abc[i]:
                times[i][abc[i].index([a-1, b-1, c+2])]+=old_multiplier
                c_not_in=False
            elif [b-1, a-1, c+2] in abc[i]:
                times[i][abc[i].index([b-1, a-1, c+2])]+=old_multiplier
                c_not_in=False
            
            if a_not_in:
                abc[i].append([a+2, b-1, c-1])
                times[i].append(old_multiplier)
            if b_not_in:
                if a_not_in:
                    z=abc[i][len(abc[i])-1]
                    if z==[b+2, a-1, c-1] or z==[b+2, c-1, a-1] or z==[a-1, b+2, c-1] or z==[c-1, b+2, a-1] or z==[a-1, c-1, b+2] or z==[c-1, a-1, b+2]:
                        times[i][len(times[i])-1]+=old_multiplier
                    else:
                        abc[i].append([a-1, b+2, c-1])
                        times[i].append(old_multiplier)
                else:
                    abc[i].append([a-1, b+2, c-1])
                    times[i].append(old_multiplier)
            if c_not_in:
                if a_not_in:
                    z=abc[i][len(abc[i])-1]
                    if b_not_in:
                        zz=abc[i][len(abc[i])-2]
                        if z==[c+2, b-1, a-1] or z==[c+2, a-1, b-1] or z==[b-1, c+2, a-1] or z==[a-1, c+2, b-1] or z==[b-1, a-1, c+2] or z==[a-1, b-1, c+2]:
                            times[i][len(times[i])-1]+=old_multiplier
                        elif zz==[c+2, b-1, a-1] or zz==[c+2, a-1, b-1] or zz==[b-1, c+2, a-1] or zz==[a-1, c+2, b-1] or zz==[b-1, a-1, c+2] or zz==[a-1, b-1, c+2]:
                            times[i][len(times[i])-2]+=old_multiplier
                        else:
                            abc[i].append([a-1, b-1, c+2])
                            times[i].append(old_multiplier)
                    else:
                        z=abc[i][len(abc[i])-1]
                        if z==[c+2, b-1, a-1] or z==[c+2, a-1, b-1] or z==[b-1, c+2, a-1] or z==[a-1, c+2, b-1] or z==[b-1, a-1, c+2] or z==[a-1, b-1, c+2]:
                            times[i][len(times[i])-1]+=old_multiplier
                        else:
                            abc[i].append([a-1, b-1, c+2])
                            times[i].append(old_multiplier)
                else:
                    abc[i].append([a-1, b-1, c+2])
                    times[i].append(old_multiplier)
print(final)
"""
"""
a=10
b=10
c=10
final=0
def recursion(a, b, c, num):
    global final
    if a==0 and b==0 or a==0 and c==0 or b==0 and c==0:
        final+=num/(3**num)
    elif a==0:
        final+=(num+b*c)/(3**num)
    elif b==0:
        final+=(num+a*c)/(3**num)
    elif c==0:
        final+=(num+a*b)/(3**num)
    elif num<15:
        recursion(a+2, b-1, c-1, num+1)
        recursion(a-1, b+2, c-1, num+1)
        recursion(a-1, b-1, c+2, num+1)
recursion(a, b, c, 0)
print(final)
"""









    
