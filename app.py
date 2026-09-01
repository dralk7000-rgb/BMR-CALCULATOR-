
st.title("BMR Calculator")
name=str(st.text_input("Enter the username:"))
dob1=int(st.number_input("enter your date of birth: "))
dob2=int(st.number_input("enter the month of dob: "))
dob3=int(st.number_input("enter the year of dob: "))
age=2026-dob3
 
gender=str(st.text_input("male or female: "))
height=int(st.number_input("enter your height: "))
weight=float(st.number_input("enter your body weight: "))
if st.button("GET RESULT"):
    mbmr=(10*weight)+(6.25*height)-(5*age)+5
    fbmr=(10*weight)+(6.25*height)-(5*age)-161
old=st.write("your actual age is: ",age,"years", 12-dob2,"months", 30-dob1,"days" )
if gender=="male":
    st.write("HI",name,"YOUR BMR=",mbmr)

elif gender=="female":
    st.write("HI",name,"YOUR BMR=",fbmr)     
    if mbmr>1800:
        st.write("High BMR needs fitness advice")
    if fbmr>1400:
        st.write("High BMR needs fitness advice")
         
else:
    st.write("Invalid data entered. Check gender Please type 'male' or 'female'.")    


  ]
