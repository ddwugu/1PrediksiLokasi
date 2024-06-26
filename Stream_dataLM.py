import streamlit as st

# Display prediksi lokasi
def predict_location(x1, x2):
    y = 27.15 - 2.33 * x1 -0.08* x2
    return y

# Main Streamlit app
def main():
    st.title('Pertamina Field Jambi-BJG-TPN')
    st.subheader('Prediksi Lokasi Kebocoran Line BJG-TPN Regresi Model')

    Titik_1_PSI = st.text_input('Input pressure drop di MGS BJG (PSI)')
    Titik_2_PSI = st.text_input('Input pressure drop di BOOSTER (PSI)')

    if st.button('Prediksi Lokasi'):
        try:
            a = 135 - float(Titik_1_PSI) if Titik_1_PSI else None
            b = 86 - float(Titik_2_PSI) if Titik_2_PSI else None
            prediksi_lokasi = predict_location(a, b)
                
            if prediksi_lokasi <= 0: # titik nol
                suspect_loct = 'Pipa Aman, Tidak Terdapat Fluida yang Mengalir'
            elif prediksi_lokasi >= 26.38: # total panjang trunkline
                suspect_loct = 'Tidak Terdapat Kebocoran'
            else:
                suspect_loct = f'Terjadi kebocoran di titik {prediksi_lokasi} KM'
            st.success(suspect_loct)
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
                suspect_loss = f'Terjadi losses sebesar {Hitung_Losses} BBL'
            elif Hitung_Losses > 0: # total panjang trunkline
                suspect_loss = f'Gain sebesar {Hitung_Losses} BBL'
            else:
                suspect_loss = f'Tidak terjadi losses'
            st.success(suspect_loss)
        except Exception as e:
            st.error(f"Error predicting location: {e}")

   

if __name__ == "__main__":
    main()
