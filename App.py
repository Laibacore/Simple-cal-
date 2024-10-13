import streamlit as st

# Function to perform basic arithmetic operations
def calculator():
    st.title("Simple Calculator")

    # Create a dropdown for selecting the operation
    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Input fields for the two numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Perform the calculation based on the operation selected
    if operation == "Add":
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {num1} / {num2} = {result}")
        else:
            st.write("Error! Division by zero.")

# Run the calculator function
if __name__ == "__main__":
    calculator()
