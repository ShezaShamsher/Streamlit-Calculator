import streamlit as st

# setup our web app config
st.set_page_config(page_title="Simple Calculator", layout='wide')

# app title and description
st.title("Simple Calculator")
st.write("Your personal math assistant!")

# Input fields for numbers and operation
num1= st.text_input("Enter your first number")
num2= st.text_input("Enter your second number")
operation = st.selectbox("Select Operator", ["Add", "Subtract", "Multiplication", "Divide"])

result = None

# Convert input to integar
if num1 and num2: 
        num1 = int(num1)  
        num2 = int(num2)  

else :
 st.error("Please enter a valid number")


if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"  
        
    
# display result
if result is not None:
    st.write(f"<h3 style='color:Green'>Result: {result} </h3>", unsafe_allow_html=True)



