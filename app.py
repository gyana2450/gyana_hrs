import streamlit as st
import numpy as np
import pickle

def recommend_hospitals(disease, top_k=5):
    disease_index = diseases.index(disease)
    similarities = similarity_matrix[:, disease_index]
    
    combined_scores = similarities.copy()
    for hospital, diseases_list in hospital_diseases.items():
        if disease in diseases_list:
            combined_scores[hospitals.index(hospital)] += 1
            
    top_indices = np.argsort(combined_scores)[-top_k:][::-1]
    recommended_hospitals = [hospitals[i] for i in top_indices if disease in hospital_diseases[hospitals[i]]]
    
    return recommended_hospitals

hospitals = pickle.load(open('hospitals.pkl', 'rb'))
diseases = pickle.load(open('diseases.pkl', 'rb'))
similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))
hospital_diseases = pickle.load(open('hospital_diseases.pkl', 'rb'))


st.markdown('<link href="styles.css" rel="stylesheet">', unsafe_allow_html=True)


st.markdown("<h1 style='text-align: left; color: white;'>HOSPITAL RECOMMENDATION SYSTEM</h1>", unsafe_allow_html=True)


selected_hospital_name = st.selectbox(
    'Need a Better Hospital ?',
    diseases
)


if st.button('Recommend'):
    recommendations = recommend_hospitals(selected_hospital_name)
    for i in recommendations:
        st.write(i)