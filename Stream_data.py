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
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°19'57.98"E, 1°47'59.69"S'
                elif 1 < prediksi_lokasi[0] < 2:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°20'17.93"E, 1°47'58.93"S '
                elif 2 < prediksi_lokasi[0] < 3:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°20'40.53"E, 1°47'48.23"S '
                elif 3 < prediksi_lokasi[0] < 4:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°20'44.55"E, 1°47'24.62"S '
		        elif 4 < prediksi_lokasi[0] < 5:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°21'5.05"E, 1°47'1.34"S '
                elif 5 < prediksi_lokasi[0] < 6:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°21'29.99"E, 1°47'12.91"S '
                elif 6 < prediksi_lokasi[0] < 7:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°22'0.22"E, 1°47'13.11"S '
		        elif 7 < prediksi_lokasi[0] < 8:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°22'32.42"E, 1°47'23.79"S '
                elif 8 < prediksi_lokasi[0] < 9:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°23'4.39"E, 1°47'18.18"S'
                elif 9 < prediksi_lokasi[0] < 10:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°23'39.56"E, 1°47'19.81"S '
		        elif 10 < prediksi_lokasi[0] < 11:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran   103°24'9.91"E, 1°47'27.14"S '
                elif 11 < prediksi_lokasi[0] < 12:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°24'43.64"E, 1°47'38.98"S'
                elif 12 < prediksi_lokasi[0] < 13:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°25'12.39"E, 1°47'43.83"S '
		        elif 13 < prediksi_lokasi[0] < 14:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°25'43.48"E, 1°47'45.28"S '
                elif 14 < prediksi_lokasi[0] < 15:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°26'19.78"E, 1°47'30.72"S '
                elif 15 < prediksi_lokasi[0] < 16:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°26'43.35"E, 1°47'24.01"S '
		        elif 16 < prediksi_lokasi[0] < 17:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°27'18.93"E, 1°47'3.66"S '
                elif 17 < prediksi_lokasi[0] < 18:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°27'40.66"E, 1°47'3.00"S '
                elif 18 < prediksi_lokasi[0] < 19:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°28'11.41"E, 1°47'3.48"S '
		        elif 19 < prediksi_lokasi[0] < 20:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°28'42.61"E, 1°47'19.39"S '
                elif 20 < prediksi_lokasi[0] < 21:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°29'3.89"E, 1°47'29.24"S '
                elif 21 < prediksi_lokasi[0] < 22:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°29'24.99"E, 1°47'8.98"S '
		        elif 22 < prediksi_lokasi[0] < 23:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°29'52.50"E, 1°47'29.88"S'
                elif 23 < prediksi_lokasi[0] < 24:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°30'13.68"E, 1°47'18.40"S'
                elif 24 < prediksi_lokasi[0] < 25:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°30'33.24"E, 1°47'32.16"S '
		        elif 25 < prediksi_lokasi[0] < 26:
                    suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM, koordinat kebocoran 103°30'56.78"E, 1°47'51.58"S'
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
