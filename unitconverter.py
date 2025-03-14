import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "centimeters": 100,
        "millimeters": 1000,
        "kilometers": 0.001,
        "feet": 3.28084,
        "inches": 39.3701,
        "yards": 1.09361,
        "miles": 0.000621371
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Streamlit UI
st.title("Unit Converter App")

# Select Conversion Type
conversion_type = st.radio("Select Conversion Type:", ("Length"))

if conversion_type == "Length":
    st.header("Length Converter")
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From Unit:", ["meters", "centimeters", "millimeters", "kilometers", "feet", "inches", "yards", "miles"])
    to_unit = st.selectbox("To Unit:", ["meters", "centimeters", "millimeters", "kilometers", "feet", "inches", "yards", "miles"])
    
    if st.button("Convert"):
        if from_unit != to_unit:
            result = length_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        else:
            st.warning("Please select different units for conversion.")


st.write("**Developed by Iffat ul Fatima**")