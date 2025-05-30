import numpy as np
dt = np.dtype([('stno',(np.int32)),('stname',(np.str_, 10)),('s1',np.float64),('s2',np.float64),('s3', np.float64)])
a = np.array([(1,'name1',35.2,35.3,35.4),(2,'name2',95.2,99.3,98.4)], dtype=dt)
print(a)
#print("Names:", a['stname'])
#print("st1Marks:", a['s1'])
#print("st2Marks:", a['s2'])
total_marks = a['s1']+ a['s2']+a['s3']
avg = total_marks/3;
print(total_marks);
print(avg);
# print headers
print(f"{'stno': <6} {'stname': <10} {'s1':<6} {'s2':<6} {'s3': <6} {'totalmarks': <10} {'Average': <7}")
print("-" * 60)
for i in range(len(a)):
    print(f"{a['stno'][i]:<6} {a['stname'][i]:<10} {a['s1'][i]:<6.1f} {a['s2'][i]:<6.1f} {a['s3'][i]:<6.1f} {total_marks[i]:10.1f} {avg[i]:<7.1f}")

#open file for writing
with open("students.txt", "w") as f:
    f.write(f"{'stno': <6} {'stname': <10} {'s1':<6} {'s2':<6} {'s3':<6} {'totalmarks':<10} {'Average':<7}\n")
    f.write("-" * 60 + "\n")
#write each row
for i in range(len(a)):
    f.write(f"{a['stno'][i]:<6} {a['stname'][i]:<10} {a['s1'][i]:<6.1f} {a['s2'][i]:<6.1f} {a['s3'][i]:<6.1f} {total_marks[i]:<10.1f} {avg[i]:<7.1f}\n")


