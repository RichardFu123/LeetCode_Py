sum=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                print(i,j,k)
                sum+=1
print("共",sum,"种")


sum2=0
a=[1,2,3,4]
import itertools
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1

print(sum2)
