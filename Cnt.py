import streamlit as st

st.title('Pertamina Field Jambi')
st.subheader('Prediksi Oil Losses')

# Display the oil loss calculation section
st.subheader('Perhitungan Oil Losses')

def calculate_average(*args):
    # Filter out None or empty values
    valid_values = [arg for arg in args if arg is not None and arg != '']
    
    # Convert valid values to float
    valid_values = [float(value) for value in valid_values]
    
    if not valid_values:
        return None
    
    average = sum(valid_values) / len(valid_values)
    return average

def predict_loss(Rb1, Rb2, Rb3, Rb4, Rb5, Rb6, Tb1, Ab):
    avg = calculate_average(Rb1, Rb2, Rb3, Rb4, Rb5, Rb6)
    if avg is not None and Tb1 is not None and Ab is not None:
        Total = Tb1 * avg
        selisih = Total - Ab
        return selisih
    else:
        return None

TimeB1 = st.text_input('Durasi Shipping', key='TimeB1')
AngkaBJG = st.text_input('Input Angka shipping MGS (BBL)', key='AngkaBJG')
RateB1 = st.text_input('Input Rate (BBL/JAM) - 1', key='RateB1')
RateB2 = st.text_input('Input Rate (BBL/JAM) - 2', key='RateB2')
RateB3 = st.text_input('Input Rate (BBL/JAM) - 3', key='RateB3')
RateB4 = st.text_input('Input Rate (BBL/JAM) - 4', key='RateB4')
RateB5 = st.text_input('Input Rate (BBL/JAM) - 5', key='RateB5')
RateB6 = st.text_input('Input Rate (BBL/JAM) - 6', key='RateB6')

if st.button('Hitung Losses'):
    try:
        Tb1 = float(TimeB1) if TimeB1 else None
        Ab = float(AngkaBJG) if AngkaBJG else None
        Rb1 = float(RateB1) if RateB1 else None
        Rb2 = float(RateB2) if RateB2 else None
        Rb3 = float(RateB3) if RateB3 else None
        Rb4 = float(RateB4) if RateB4 else None
        Rb5 = float(RateB5) if RateB5 else None
        Rb6 = float(RateB6) if RateB6 else None

        Hitung_l = predict_loss(Rb1, Rb2, Rb3, Rb4, Rb5, Rb6, Tb1, Ab)
        
        if Hitung_l is not None:
            st.success(f"Banyaknya Oil losses adalah: {Hitung_l} BBL")
        else:
            st.warning("Input tidak valid untuk menghitung losses.")
    except Exception as e:
        st.error(f"Error predicting location: {e}")

