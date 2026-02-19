import streamlit as st
import pickle
st.set_page_config(
    page_title="Addiction Prediction",
    page_icon=":smoking:",
    layout="centered",)

st.title("Addiction_Prediction!")


def load_model():
    return pickle.load(open('rf_model.pkl', 'rb'))
    
model=load_model()

Avg_Daily_Usage_Hours = st.number_input("enter Average Daily Usage Hours")
st.write("value entered:", Avg_Daily_Usage_Hours)

Affects_Academic_Performance=st.selectbox("Does it affect Academic Performance?", [1, 0])
st.write("value entered:", Affects_Academic_Performance)

Sleep_Hours_Per_Night = st.number_input("enter sleep hours",)
st.write("value entered:", Sleep_Hours_Per_Night)


Mental_Health_Score = st.selectbox(
    "Enter Mental Health Score",
    [4,5,6,7,8,9]
)
st.write("value entered:", Mental_Health_Score)

Conflicts_Over_Social_Media = st.selectbox(
    "Enter number of conflicts over social media",
    [0,1,2,3,4,5]
)
st.write("value entered:", Conflicts_Over_Social_Media)

if st.button("Predict"):
    prediction = model.predict([[ Avg_Daily_Usage_Hours, Affects_Academic_Performance, Sleep_Hours_Per_Night, Mental_Health_Score, Conflicts_Over_Social_Media]])

    st.success(f"Prediction: {prediction[0]}")
