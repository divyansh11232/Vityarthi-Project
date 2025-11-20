name=input("Enter patient's name: ")
id=input("Enter patient's id: ")
gen=input("Enter patient's gender (M/F): ") 
age=float(input("Enter the patient's age: "))
print("TESTS AND THEIR CODES:")
print("ALBUMIN   ---> ALB\nAMMONIA  --->NH3\nBILIRUBIN CONJUGATED  --->BILC\nBILIRUBIN UNCONJUGATED  --->BILUC\nAMYLASE  --->AMYL\nCALCIUM  --->CAL\nCHOLESTROL  --->CHOL\nCO2  --->CO2\nCREATINE KINASE  --->CK\nGLUCOSE  --->GLU\nHAEMOGLOBIN  HAEMOGLOBIN   --->HAEM")
t=input("Enter the test: ")
n=float(input("Enter the value: "))

if 12<=age<18:
    if gen=="M":
        if t=="ALB":
            if 3.7<=n<=5.6:
                print("Your ALBUMIN value is within the NORMAL range.")
            if n<3.7:
                print("Your ALBUMIN value is LOWER than the normal limit.")
            if n>5.6:
                print("Your ALBUMIN value is HIGHER than the normal the normal limit.")
        if t=="NH3":
            if 9<=n<=33:
                print("Your AMMONIA value is within the  NORMAAL range.")
            if n<9:
                print("Your AMMONIA value is LOWER than the normal limit.")
            if n>33:
                print("Your AMMONIA value is HIGHER than the normal limit.")
        if t=="BILC":
            if 0<=n<=0.3:
                print("Your BILIRUBIN CONJUGATED value is within the NORMAL range.")
            if n>0.3:
                print("Your BILIRUBIN CONJUGATED value is HIGHER than the normal range.")
        if t=="BILUC":
            if 0<=n<=1.1:
                print("Your BILIRUBIN UNCONJUGATED value is within the NORMAL range.")
            if n>1.1:
                print("Your BILIRUBIN UNCONJUGATED value is HIGHER than the normal limit.")
        if t=="AMYL":
            if 30<=n<=100:
                print("Your AMYLASE value is within the NORMAL range.")
            if n<30:
                print("Your AMYLASE value is LOWER than the normal limit.")
            if n>100:
                print("Your AMYLASE value is HIGHER than the normal limit.")  
        if t=="CAL":
            if 8.5<=n<=10.5:
                print("Your CALCIUM value is within the NORMAL range.")
            if n<8.5:
                print("Your CALCIUM value is LOWER than the normal limit.")
            if n>10.5:
                print("Your CALCIUM value is HIGHER than the normal limit.")
        if t=="CHOL":
            if 127<=n<=225:
                print("Your CHOLESTROL value is within the NORMAL range.")
            if n<127:
                print("Your CHOLESTROL valuee is LOWER than the normal limit.") 
            if n>225:
                print("Your CHOLESTROL value is HIGHER than the normal limit.")
        if t=="CO2":
            if 20<=n<=26:
                print("Your CO2 value is within the NORMAL range.")
            if n<20:
                print("Your CO2 value is LOWER than the normal limit.")
            if n>26:
                print("Your CO2 value is HIGHER than the normal limit.")
        if t=="CK":
            if 60<=n<=370:
                print("Your CREATINE KINASE value is within the NORMAL range.")
            if n<60:
                print("Your CREATINE KINASE value is LOWER than the normal limit.")
            if n>370:
                print("Your CREATINE KINASE value is HIGHER than the normal limit.")
        if t=="GLU":
            if 70<=n<=106:
                print("Your GLUCOSE value is within the NORMAL range.")
            if n<70:
                print("Your GLUCOSE value is LOWER than the normal limit.")
            if n>106:
                print("Your GLUCOSE value is HIGHER than the normal limit.")
        if t=="HAEM":
            if 3.8<=n<=5.9:
                print("Your HAEMOGLOBIN value is within the NORMAL range.")
            if n<3.8:
                print("Your HAEMOGLOBIN value is LOWER than the normal limit.")
            if n>5.9:
                print("Your HAEMOGLOBIN value is HIGHER than the normal limit.")
        
    if gen=="F":

        if t=="ALB":
            if 3.7<=n<=5.6:
                print("Your ALBUMIN value is within the NORMAL range.")
            if n<3.7:
                print("Your ALBUMIN value is LOWER than the normal limit.")
            if n>5.6:
                print("Your ALBUMIN value is HIGHER than the normal the normal limit.")
        if t=="NH3":
            if 9<=n<=33:
                print("Your AMMONIA value is within the  NORMAAL range.")
            if n<9:
                print("Your AMMONIA value is LOWER than the normal limit.")
            if n>33:
                print("Your AMMONIA value is HIGHER than the normal limit.")
        if t=="BILC":
            if 0<=n<=0.3:
                print("Your BILIRUBIN CONJUGATED value is within the NORMAL range.")
            if n>0.3:
                print("Your BILIRUBIN CONJUGATED value is HIGHER than the normal range.")
        if t=="BILUC":
            if 0<=n<=1.1:
                print("Your BILIRUBIN UNCONJUGATED value is within the NORMAL range.")
            if n>1.1:
                print("Your BILIRUBIN UNCONJUGATED value is HIGHER than the normal limit.")
        if t=="AMYL":
            if 30<=n<=100:
                print("Your AMYLASE value is within the NORMAL range.")
            if n<30:
                print("Your AMYLASE value is LOWER than the normal limit.")
            if n>100:
                print("Your AMYLASE value is HIGHER than the normal limit.")  
        if t=="CAL":
            if 8.5<=n<=10.6:
                print("Your CALCIUM value is within the NORMAL range.")
            if n<8.5:
                print("Your CALCIUM value is LOWER than the normal limit.")
            if n>10.5:
                print("Your CALCIUM value is HIGHER than the normal limit.")
        if t=="CHOL":
            if 126<=n<=215:
                print("Your CHOLESTROL value is within the NORMAL range.")
            if n<126:
                print("Your CHOLESTROL valuee is LOWER than the normal limit.") 
            if n>215:
                print("Your CHOLESTROL value is HIGHER than the normal limit.")
        if t=="CO2":
            if 20<=n<=26:
                print("Your CO2 value is within the NORMAL range.")
            if n<20:
                print("Your CHOLESTROL value is LOWER than the normal limit.")
            if n>26:
                print("Your CHOLESTROL value is HIGHER than the normal limit.")
        if t=="CK":
            if 50<=n<=230:
                print("Your CREATINE KINASE value is within the NORMAL range.")
            if n<50:
                print("Your CREATINE KINASE value is LOWER than the normal limit.")
            if n>230:
                print("Your CREATINE KINASE value is HIGHER than the normal limit.")
        if t=="GLU":
            if 70<=n<=106:
                print("Your GLUCOSE value is within the NORMAL range.")
            if n<70:
                print("Your GLUCOSE value is LOWER than the normal limit.")
            if n>106:
                print("Your GLUCOSE value is HIGHER than the normal limit.")
        if t=="HAEM":
            if 3.8<=n<=5.9:
                print("Your HAEMOGLOBIN value is within the NORMAL range.")
            if n<3.8:
                print("Your HAEMOGLOBIN value is LOWER than the normal limit.")
            if n>5.9:
                print("Your HAEMOGLOBIN value is HIGHER than the normal limit.")

if age>18:
    if gen=="M":
        if t=="ALB":
            if 3.5<=n<=5.5:
                print("Your ALBUMIN value is within the NORMAL range.")
            if n<3.5:
                print("Your ALBUMIN value is LOWER than the normal limit.")
            if n>5.5:
                print("Your ALBUMIN value is HIGHER than the normal the normal limit.")
        if t=="NH3":
            if 26<=n<=94:
                print("Your AMMONIA value is within the  NORMAAL range.")
            if n<26:
                print("Your AMMONIA value is LOWER than the normal limit.")
            if n>94:
                print("Your AMMONIA value is HIGHER than the normal limit.")
        if t=="BILC":
            if 0<=n<=0.3:
                print("Your BILIRUBIN CONJUGATED value is within the NORMAL range.")
            if n>0.3:
                print("Your BILIRUBIN CONJUGATED value is HIGHER than the normal range.")
        if t=="BILUC":
            if 0.2<=n<=0.8:
                print("Your BILIRUBIN UNCONJUGATED value is within the NORMAL range.")
            if n<0.2:
                print("Your BILIRUBIN UNCONJUGATED value is LOWER than the normal limit ")
            if n>0.8:
                print("Your BILIRUBIN UNCONJUGATED value is HIGHER than the normal limit.")
        if t=="AMYL":
            if 30<=n<=110:
                print("Your AMYLASE value is within the NORMAL range.")
            if n<30:
                print("Your AMYLASE value is LOWER than the normal limit.")
            if n>110:
                print("Your AMYLASE value is HIGHER than the normal limit.")  
        if t=="CAL":
            if 8.5<=n<=10.2:
                print("Your CALCIUM value is within the NORMAL range.")
            if n<8.5:
                print("Your CALCIUM value is LOWER than the normal limit.")
            if n>10.5:
                print("Your CALCIUM value is HIGHER than the normal limit.")
        if t=="CHOL":
            if 200<=n<=239:
                print("Your CHOLESTROL value is within the NORMAL range.")
            if n<200:
                print("Your CHOLESTROL valuee is LOWER than the normal limit.") 
            if n>239:
                print("Your CHOLESTROL value is HIGHER than the normal limit.")
        if t=="CO2":
            if 23<=n<=30:
                print("Your CO2 value is within the NORMAL range.")
            if n<23:
                print("Your CHOLESTROL value is LOWER than the normal limit.")
            if n>30:
                print("Your CHOLESTROL value is HIGHER than the normal limit.")
        if t=="CK":
            if 30<=n<=135:
                print("Your CREATINE KINASE value is within the NORMAL range.")
            if n<30:
                print("Your CREATINE KINASE value is LOWER than the normal limit.")
            if n>135:
                print("Your CREATINE KINASE value is HIGHER than the normal limit.")
        if t=="GLU":
            if 70<=n<=99:
                print("Your GLUCOSE value is within the NORMAL range.")
            if n<13.5:
                print("Your GLUCOSE value is LOWER than the normal limit.")
            if n>106:
                print("Your GLUCOSE value is HIGHER than the normal limit.")
        if t=="HAEM":
            if 13.5<=n<=18:
                print("Your HAEMOGLOBIN value is within the NORMAL range.")
            if n<13.5:
                print("Your HAEMOGLOBIN value is LOWER than the normal limit.")
            if n>18:
                print("Your HAEMOGLOBIN value is HIGHER than the normal limit.")
    if gen=="F":
        if t=="ALB":
            if 3.5<=n<=5.5:
                print("Your ALBUMIN value is within the NORMAL range.")
            if n<3.5:
                print("Your ALBUMIN value is LOWER than the normal limit.")
            if n>5.5:
                print("Your ALBUMIN value is HIGHER than the normal the normal limit.")
        if t=="NH3":
            if 26<=n<=94:
                print("Your AMMONIA value is within the  NORMAAL range.")
            if n<26:
                print("Your AMMONIA value is LOWER than the normal limit.")
            if n>94:
                print("Your AMMONIA value is HIGHER than the normal limit.")
        if t=="BILC":
            if 0<=n<=0.3:
                print("Your BILIRUBIN CONJUGATED value is within the NORMAL range.")
            if n>0.3:
                print("Your BILIRUBIN CONJUGATED value is HIGHER than the normal range.")
        if t=="BILUC":
            if 0.2<=n<=0.8:
                print("Your BILIRUBIN UNCONJUGATED value is within the NORMAL range.")
            if n<0.2:
                print("Your BILIRUBIN UNCONJUGATED value is LOWER than the normal limit ")
            if n>0.8:
                print("Your BILIRUBIN UNCONJUGATED value is HIGHER than the normal limit.")
        if t=="AMYL":
            if 30<=n<=110:
                print("Your AMYLASE value is within the NORMAL range.")
            if n<30:
                print("Your AMYLASE value is LOWER than the normal limit.")
            if n>110:
                print("Your AMYLASE value is HIGHER than the normal limit.")  
        if t=="CAL":
            if 8.5<=n<=10.2:
                print("Your CALCIUM value is within the NORMAL range.")
            if n<8.5:
                print("Your CALCIUM value is LOWER than the normal limit.")
            if n>10.5:
                print("Your CALCIUM value is HIGHER than the normal limit.")
        if t=="CHOL":
            if 200<=n<=239:
                print("Your CHOLESTROL value is within the NORMAL range.")
            if n<200:
                print("Your CHOLESTROL value is LOWER than the normal limit.") 
            if n>239:
                print("Your CHOLESTROL value is HIGHER than the normal limit.")
        if t=="CO2":
            if 23<=n<=30:
                print("Your CO2 value is within the NORMAL range.")
            if n<23:
                print("Your CHOLESTROL value is LOWER than the normal limit.")
            if n>30:
                print("Your CHOLESTROL value is HIGHER than the normal limit.")
        if t=="CK":
            if 30<=n<=135:
                print("Your CREATINE KINASE value is within the NORMAL range.")
            if n<30:
                print("Your CREATINE KINASE value is LOWER than the normal limit.")
            if n>135:
                print("Your CREATINE KINASE value is HIGHER than the normal limit.")
        if t=="GLU":
            if 70<=n<=99:
                print("Your GLUCOSE value is within the NORMAL range.")
            if n<70:
                print("Your GLUCOSE value is LOWER than the normal limit.")
            if n>99:
                print("Your GLUCOSE value is HIGHER than the normal limit.")
        if t=="HAEM":
            if 12<=n<=15:
                print("Your HAEMOGLOBIN value is within the NORMAL range.")
            if n<12:
                print("Your HAEMOGLOBIN value is LOWER than the normal limit.")
            if n>15:
                print("Your HAEMOGLOBIN value is HIGHER than the normal limit.")
    
