import streamlit as st
import numpy as np
import joblib

# Load Model
model = joblib.load("rfc_model.pkl")

#load the image
st.image("phone_image.jpg", width=2000)  # Make sure the logo is in the same folder

# App Title
st.title("📱 Mobile Price Prediction App")
st.write("Enter Mobile details to predict the price.")

# Layout using columns
col1, col2 = st.columns(2)

#consider 2 column layout
with col1:
    ram = st.number_input("RAM (MB)", min_value=256, max_value=8000, step=128, value=2048)
    battery_power = st.number_input("Battery Power (mAh)", min_value=500, max_value=5000, step=100, value=1500)
    px_width = st.number_input("Pixel Width", min_value=500, max_value=3000, step=50, value=1080)
    px_height = st.number_input("Pixel Height", min_value=500, max_value=3000, step=50, value=1920)
    int_memory = st.number_input("Internal Memory (GB)", min_value=4, max_value=256, step=4, value=32)
    
with col2:
    sc_w = st.number_input("Screen Width (cm)", min_value=0, max_value=20, step=1, value=5)
    pc = st.number_input("Primary Camera (MP)", min_value=0, max_value=50, step=1, value=12)
    three_g = st.radio("Supports 3G?", ['Yes', 'No'])
    sc_h = st.number_input("Screen Height (cm)", min_value=0, max_value=20, step=1, value=10)
   

# Prediction Function
def predict_price_range():
    features = np.array([[ram, 
                          battery_power, 
                          px_width, px_height, 
                          int_memory, 
                          sc_w, 
                          pc, 
                          1 if three_g == 1 else 0, 
                          sc_h]]
                       )
    prediction = model.predict(features)
    return prediction[0]

# Predict Button
if st.button("Predict Price Range"):
    result = predict_price_range()
    st.success(f"Predicted Price Range: {result}")
    if result == 0:
        st.markdown('Low Cost')
    if result == 1:
        st.markdown('Medium Cost')
    if result == 2:
        st.markdown('High Cost')
    if result == 3:
        st.markdown('Very High Cost')
st.markdown(""" ---
⚙️ Build By **Deepak Kumar** \n
📩 **Contact Me:**  
🔗 [LinkedIn](https://www.linkedin.com/in/deepak-kumar8/) 
🔗 [GitHub](https://github.com/Kumard8x)
📧 Email: deepak.kumar030151@gmail.com  
""")



