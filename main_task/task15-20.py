basic_salary=float(input("enter basic salary"))
benefits=float(input("enter benefits"))
gross_salary=benefits+basic_salary
nhif=0
relief=2400
if gross_salary<=5999:
    nhif=150
elif  gross_salary>=6000 and gross_salary<=7999:
    nhif=300
elif gross_salary>=8000 and gross_salary<=11999:
    nhif=400
elif gross_salary>=12000 and gross_salary<=14999:
    nhif=500
elif gross_salary>=15000 and gross_salary<=19999:
    nhif=600
elif gross_salary>=20000 and gross_salary<=24999:
    nhif=750   
elif gross_salary>=25000 and gross_salary<=29999:
    nhif=850
elif gross_salary>=30000 and gross_salary<=34999:
    nhif=900
elif gross_salary>=35000 and gross_salary<=39999:
    nhif=950
elif gross_salary>=40000 and gross_salary<=44999:
    nhif=1000
elif gross_salary>=45000 and gross_salary<=49999:
    nhif=1100
elif gross_salary>=50000 and gross_salary<=59999:
    nhif=1200               
elif gross_salary>=60000 and gross_salary<=69999:
    nhif=1300
elif gross_salary>=70000 and gross_salary<=79999:
    nhif=1400
elif gross_salary>= 80000 and gross_salary<=89999:
    nhif=1500          
elif gross_salary>=90000 and gross_salary<=99999:
    nhif=1600
else:
    nhif=1700 
print(nhif)

  #number 16
#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF.
if gross_salary<18000:
    NSSF=gross_salary*0.06
else:
    NSSF=18000*0.06
print(NSSF)


#17
#Continue with the same program and calculate an individual’s NHDF using:
 #i.e NHDF = gross_salary *  0.015
NHDF= gross_salary*0.015
print(NHDF)

#18
#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF) 
taxable_income=gross_salary-(NSSF+NHDF)
print(taxable_income)

#19
#Continue with the same program and find the person's PAYEE using the taxable income above.
#Find the Kenya PAYEE Tax Rate using
if taxable_income>=0 and taxable_income<=24000:
    payee=taxable_income*0.01
elif taxable_income>24000 and taxable_income<=32333:
    payee=(24000*0.1)+(0.25*(taxable_income-24000))-relief
elif taxable_income>32333 and taxable_income<=500000:
    payee=(24000*0.1)+(0.25*8333)+(0.3*(taxable_income-32333))-relief
elif taxable_income>500000 and taxable_income<=800000:
    payee=(24000*0.1)+(0.25*8333)+(0.3*467667)+(0.325*(taxable_income-500000))-relief
else:
    payee=(0.35*(taxable_income-800000))-relief 
print(payee) 

#20
#Continue with the same program and calculate an individual’s Net Salary using:
# net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
net_salary=gross_salary-(nhif+NHDF+NSSF+payee)
print(net_salary)