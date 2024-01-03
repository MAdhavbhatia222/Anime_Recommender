import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

def create_similarity_matrix(data):
    # Replace NaN in 'GENRE' with an empty string
    data['GENRE'] = data['GENRE'].fillna('')

    # Creating the TF-IDF matrix
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['GENRE'])

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Save the cosine similarity matrix
    with open('cosine_sim.pkl', 'wb') as f:
        pickle.dump(cosine_sim, f)

    # Create and save the indices mapping
    indices = pd.Series(data.index, index=data['NAME']).to_dict()
    with open('indices.pkl', 'wb') as f:
        pickle.dump(indices, f)

# Load data
data = pd.read_csv('Anime_Data_Final.csv')

# Uncomment the following line after loading your data
create_similarity_matrix(data)