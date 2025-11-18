import streamlit as st
from datetime import datetime, date
 
st.title("Birthday Counts 🥳")
name= st.text_input("Your Name")
birthday=st.date_input(
                      "Select Your Birthday",
                       min_value=date(1900,1,1),
                       max_value=date.today(),
                       
                       )
if st.button("shows count"):
    today=date.today()
    
    nextbirthday= birthday.replace(year=today.year)
    if nextbirthday < today:
        nextbirthday=birthday.replace(year=today.year+1)

    leftoutdays = (nextbirthday -today).days
    if leftoutdays==0:
        st.success(f"Happy Birthday to {name} 🎂🧁😍")
        st.balloons( )
    else:
        st.info(f"{name} your Bigday  is coming in {leftoutdays} days!🤗")
        st.snow()
