import pickle
import streamlit as st

# Load the model
try:
    with open('Pred_lokasi11.sav', 'rb') as file:
        LokasiKM = pickle.load(file)
except Exception as e:
    st.error(f"Error loading the model: {e}")
    LokasiKM = None  # Assign None if there is an error loading the model

# Web Title
st.title('Pertamina Field Jambi')
st.subheader('Prediksi Lokasi Kebocoran Line BJG-TPN')
# User Inputs for leak prediction
Titik_1_PSI = st.text_input('Input Pressure di MGS BJG (PSI)')
Titik_2_PSI = st.text_input('Input Pressure di BOOSTER (PSI)')
a = 135 - float(Titik_1_PSI) if Titik_1_PSI else None
b = 86 - float(Titik_2_PSI) if Titik_2_PSI else None

# Code prediction
suspect_loct = ''

# Prediction Button for leak prediction
if LokasiKM is not None and st.button('Prediksi Lokasi'):
    try:
        if a is not None and b is not None:
            prediksi_lokasi = LokasiKM.predict([[a, b]])
            if prediksi_lokasi[0] == 0: # titik nol
                suspect_loct = 'It is safe that there is no fluid flowing'
            elif prediksi_lokasi[0] >= 26.3: # total panjang trunkline
                suspect_loct = 'Safe, there are no leaks'
            else:
                suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM'
                if 0 < prediksi_lokasi[0] < 1:
                    suspect_loct = 'koordinat kebocoran -1.675007, 103.684710'
                elif 1 < prediksi_lokasi[0] < 2:
                    suspect_loct = 'koordinat kebocoran -1.675207, 103.684710'
                elif 2 < prediksi_lokasi[0] < 3:
                    suspect_loct = 'koordinat kebocoran -1.675007, 103.884710'
                elif 3 < prediksi_lokasi[0] < 30:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran -1.635007, 103.884710 '
            st.success(suspect_loct)
        else:
            st.warning("Masukkan tekanan yang valid untuk kedua titik.")
    except Exception as e:
        st.error(f"Error predicting location: {e}") 

# Display the oil loss calculation section
st.subheader('Perhitungan Oil Losses')

def predict_loss(R1, P1, P2, s):
    R2 = P2 * R1 / P1
    los = R2 - R1
    y = los * s
    return y

Rate1 = st.text_input('Input rate awal(BBL/Jam)')
Pressure1 = st.text_input('Input pressure 1 saat rate awal (PSI)')
Pressure2 = st.text_input('Input pressure 2 saat terjadi pressure drop (PSI)')
Durasi = st.text_input('Durasi pressure drop (Jam)')

if st.button('Hitung Losses'):
    try:
        R1 = float(Rate1)
        P1 = float(Pressure1)
        P2 = float(Pressure2)
        s = float(Durasi) # Perbaikan pada nama variabel
        Hitung_Losses = predict_loss(R1, P1, P2, s) # Perbaikan pada argumen

        if Hitung_Losses < 0: # titik nol
            suspect_loss = f'Terjadi losses sebesar {Hitung_Losses} BBL '
        elif Hitung_Losses > 0: # total panjang trunkline
            suspect_loss = f'Gain sebesar {Hitung_Losses} BBL'
        else:
            suspect_loss = f'Tidak terjadi losses'
        st.success(suspect_loss)
    except Exception as e:
        st.error(f"Error predicting location: {e}")
st.markdown("[Opsi 2 : Prediksi Linear Model](https://1prediksilokasi-eld9x5crdkcrc69g3nzbgv.streamlit.app/)")
