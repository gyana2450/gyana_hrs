import streamlit as st
import pickle

def recommend(hospital):
    hsp_index = disease_list[disease_list['title'] == hospital].index[0]
    distances = similarity[hsp_index]
    hsp_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_disease = []
    for i in hsp_list:
        recommended_disease.append(disease_list.iloc[i[0]].hospital)
    return recommended_disease

disease_list = pickle.load(open('hospital.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


st.markdown("<h1 style='text-align: left; color: white;'>HOSPITAL RECOMMENDATION SYSTEM</h1>", unsafe_allow_html=True)


selected_hospital_name = st.selectbox(
    'Need a Better Hospital ?',
    disease_list['title'].values
)


if st.button('Recommend'):
    recommendations = recommend(selected_hospital_name)
    for i in recommendations:
        st.write(i)