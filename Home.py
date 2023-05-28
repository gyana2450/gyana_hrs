import streamlit as st
import numpy as np
import pickle
import pandas as pd

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

HMS = pd.read_csv('HMS_dataset.csv')


def recommend_hospitals(disease, top_k=5):
    disease_index = diseases.index(disease)
    similarities = similarity_matrix[:, disease_index]
    
    combined_scores = similarities.copy()
    recommended_hospital_imgs = []
    recommended_hospital_location = []
    recommended_hospital_phone = []

    for hospital, diseases_list in hospital_diseases.items():
        if disease in diseases_list:
            combined_scores[hospitals.index(hospital)] += 1
            
    top_indices = np.argsort(combined_scores)[-top_k:][::-1]
    recommended_hospitals = [hospitals[i] for i in top_indices if disease in hospital_diseases[hospitals[i]]]

    #fetch images from dataFrame
    recommended_hospital_imgs = [HMS.loc[HMS['hospital'] == hospital, 'img'].values[0] for hospital in recommended_hospitals]

    #fetch locations from dataFrame
    recommended_hospital_location = [HMS.loc[HMS['hospital'] == hospital, 'location'].values[0] for hospital in recommended_hospitals]

    #fetch phone numbers from dataFrame
    recommended_hospital_phone = [HMS.loc[HMS['hospital'] == hospital, 'phone'].values[0] for hospital in recommended_hospitals]


    # if len(recommended_hospital_imgs) != top_k:
    #     raise ValueError("Incorrect number of image URLs/paths.")
    
    return recommended_hospitals, recommended_hospital_imgs, recommended_hospital_location, recommended_hospital_phone

hospitals = pickle.load(open('hospitals.pkl', 'rb'))
diseases = pickle.load(open('diseases.pkl', 'rb'))
similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))
hospital_diseases = pickle.load(open('hospital_diseases.pkl', 'rb'))


st.markdown('<link href="styles.css" rel="stylesheet">', unsafe_allow_html=True)


st.markdown("<h1 style='text-align: left; color: white;'>HOSPITAL RECOMMENDATION SYSTEM</h1>", unsafe_allow_html=True)


selected_disease_name = st.selectbox(
    'Need a Better Hospital ?',
    diseases
)
if st.button('Recommend'):
    recommendations, img, location, phone = recommend_hospitals(selected_disease_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        # st.image(img[0])
        st.markdown(location[0])
        st.markdown(phone[0])
    with col2:
        st.text(recommendations[1])
        # st.image(img[1])
        st.markdown(location[1])
        st.markdown(phone[1])
    with col3:
        st.text(recommendations[2])
        # st.image(img[2])
        st.markdown(location[2])
        st.markdown(phone[2])
    with col4:
        st.text(recommendations[3])
        # st.image(img[3])
        st.markdown(location[3])
        st.markdown(phone[3])
    with col5:
        st.text(recommendations[4])
        # st.image(img[4])
        st.markdown(location[4])
        st.markdown(phone[4])