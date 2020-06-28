# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data,new_record))
print("the shape is",np.shape(census))
#step2
age = np.array(census[:,0])
#print(np.shape(age))

max_age = age.max(axis=0)
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)

#step3
race = np.array(census[:,2])
race_0 =(race==0)
print(race[race_0])
len_0 = len(race[race_0])
print(len_0)
race_1 = (race==1)
len_1 = len(race[race_1])
race_2 = (race==2)
len_2 = len(race[race_2])
race_3 = (race==3)
len_3 = len(race[race_3])
race_4 = (race==4)
len_4 = len(race[race_4])
least_sel = min(len_0,len_1,len_2,len_3,len_4)
length = np.array([len_0,len_1,len_2,len_3,len_4])
minority_race = np.where(least_sel == length) 

print(minority_race)
#step 4



senior_citizens = census[census[:,0]>60]

senior_citizens_len = len(senior_citizens)
print (senior_citizens_len)
working_hours_sum=senior_citizens.sum(axis=0)[6]
avg_working_hours = working_hours_sum/senior_citizens_len
print(round(avg_working_hours,2))
#step 5
edu = np.array(census[:,1])

high = census[census[:,1]>10] 
low = census[census[:,1]<=10]
avg_pay_high = (high.sum(axis=0)[7])/ len(high)
print(round(avg_pay_high,2))
avg_pay_low = (low.sum(axis=0)[7])/len(low)
print(round(avg_pay_low,2))



