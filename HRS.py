import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Data Preprocessing
hospital_diseases = {
    'Maternity Care Hospital': ['Gynecology'],
    'AMRI Hospital': ['Gynecology', 'Urology', 'Dermatology', 'Cardiology'],
    'Apollo Hospital': ['Gynecology', 'Hematology', 'Neurology', 'Urology', 'Orthopedic', 'Dermatology', 'Cancer', 'Cardiology', 'Gastroenterology'],
    'Care Hospital': ['Gynecology', 'Urology', 'Orthopedic', 'Cardiology', 'Gastroenterology', 'Rheumatology'],
    'Utkal Hospital': ['Gynecology', 'Neurology'],
    'SUM Hospital': ['Hematology', 'Neurology', 'Cancer', 'Cardiology', 'Gastroenterology'],
    'AIIMS Hospital': ['Hematology', 'Gastroenterology'],
    'The Hope Cancer Care': ['Cancer', 'Hematology'],
    'ORAC': ['Hematology', 'Rheumatology'],
    'Sparsh Hospital': ['Neurology', 'Cancer'],
    'SNAYU Neurology Clinic': ['Neurology'],
    'KIIMS Hospital': ['Urology', 'Cancer', 'Cardiology', 'Rheumatology'],
    'ISHA Urology Center': ['Urology'],
    'Kar Clinic': ['Orthopedic', 'Dermatology', 'Rheumatology'],
    'OMKAR Health Care': ['Orthopedic'],
    'Health Village Hospital': ['Orthopedic', 'Dermatology', 'Cancer'],
    'ASHU Skin Care': ['Dermatology'],
    'Sara Gastro & Laparoscopic Hospital': ['Gastroenterology'],
    'Angel Health Care': ['Rheumatology']
}

hospitals = list(hospital_diseases.keys())
diseases = sorted(list(set([disease for diseases in hospital_diseases.values() for disease in diseases])))

# Step 2: Feature Extraction
feature_matrix = np.zeros((len(hospitals), len(diseases)))
for i, hospital in enumerate(hospitals):
    for j, disease in enumerate(diseases):
        if disease in hospital_diseases[hospital]:
            feature_matrix[i, j] = 1

# Step 3: Similarity Calculation
similarity_matrix = cosine_similarity(feature_matrix)

# Step 4: Recommend Hospitals
def recommend_hospitals(disease, top_k=5):
    disease_index = diseases.index(disease)
    similarities = similarity_matrix[:, disease_index]
    
    combined_scores = similarities.copy()
    for hospital, diseases_list in hospital_diseases.items():
        if disease in diseases_list:
            combined_scores[hospitals.index(hospital)] += 1  # Increase score for specialization
            
    top_indices = np.argsort(combined_scores)[-top_k:][::-1]
    recommended_hospitals = [hospitals[i] for i in top_indices if disease in hospital_diseases[hospitals[i]]]
    
    return recommended_hospitals

# Example Usage
disease_input = 'Cancer'
recommended_hospitals = recommend_hospitals(disease_input)
print(f"Recommended hospitals for {disease_input}: {recommended_hospitals}")


import pickle
pickle.dump(hospitals,open('hospitals.pkl', 'wb'))
pickle.dump(diseases,open('diseases.pkl', 'wb'))
pickle.dump(similarity_matrix,open('similarity_matrix.pkl', 'wb'))
pickle.dump(hospital_diseases,open('hospital_diseases.pkl', 'wb'))
