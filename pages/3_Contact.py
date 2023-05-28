import streamlit as st

st.title("Contact Us")
st.subheader("Get in touch with us")

# Address
address_line = "<i class='fas fa-map-marker-alt'></i> Address:&nbsp;&nbsp;&nbsp;<i class='fas fa-location-arrow'></i>Plot No: 1 Xavier Road Dist, Rail Vihar, Chandrasekharpur, Bhubaneswar, Odisha 751013"
st.markdown(address_line, unsafe_allow_html=True)

# Phone number
st.markdown("<i class='fas fa-phone'></i> Phone No:&nbsp;&nbsp;&nbsp;077351 21328", unsafe_allow_html=True)

# Email
st.markdown("<i class='far fa-envelope'></i> Email:&nbsp;&nbsp;&nbsp;gpbbsr@gmail.com", unsafe_allow_html=True)