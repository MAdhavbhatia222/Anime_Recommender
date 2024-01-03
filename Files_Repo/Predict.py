from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)

def load_model_and_data():
    # Load the cosine similarity matrix
    with open('cosine_sim.pkl', 'rb') as f:
        cosine_sim = pickle.load(f)

    # Load the indices mapping
    with open('indices.pkl', 'rb') as f:
        indices = pickle.load(f)

    # Load your dataset here (adjust the path/filename as needed)
    data = pd.read_csv('Anime_Data_Final.csv')

    return cosine_sim, indices, data

cosine_sim, indices, data = load_model_and_data()

def get_recommendations(title, cosine_sim, indices):
    # Get the index of the anime that matches the title
    idx = indices[title]

    # Get the pairwise similarity scores of all anime with that anime
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the anime based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar anime
    sim_scores = sim_scores[1:11]

    # Get the anime indices
    anime_indices = [i[0] for i in sim_scores]
    
    anime_indices = [i for i in anime_indices if i != idx]
    
    # Return the top 10 most similar anime
    return data['NAME'].iloc[anime_indices]
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    query = data['NAME'][data['NAME'].str.contains(search, case=False, na=False)]
    suggestions = query.tolist()
    return jsonify(matching_results=suggestions)


@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title', default='', type=str)
    if title:
        try:
            recommendations = get_recommendations(title, cosine_sim, indices)
            if recommendations.empty:
                raise KeyError
        except KeyError:
            recommendations = pd.Series(["DeathNote", "Attack on Titans", "Naruto", "My Hero Academia", "One Piece"])
    else:
        recommendations = pd.Series(["DeathNote", "Attack on Titans", "Naruto", "My Hero Academia", "One Piece"])

    return render_template('recommendations.html', recommendations=recommendations.tolist())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)