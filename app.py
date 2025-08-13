# import streamlit as st
# import random

# # Page config with improved settings
# st.set_page_config(
#     page_title="CineMatch AI 🎬", 
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'About': "### A smart movie recommendation engine powered by AI"
#     }
# )

# # ---- Premium CSS Styling ----
# st.markdown("""
#     <style>
#         :root {
#             --primary: #FF4B4B;
#             --secondary: #FF9E1B;
#             --dark: #0F1117;
#             --darker: #0A0C12;
#             --light: #FFFFFF;
#             --gray: #2B2D42;
#         }
        
#         body {
#             background-color: var(--dark);
#             color: var(--light);
#             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#         }
        
#         .stApp {
#             background: linear-gradient(145deg, var(--darker), #1a1c22);
#             color: var(--light);
#         }
        
#         h1, h2, h3 {
#             font-family: 'Helvetica Neue', sans-serif;
#             font-weight: 700;
#             background: linear-gradient(90deg, var(--primary), var(--secondary));
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#         }
        
#         .title {
#             text-align: center;
#             margin-bottom: 30px;
#             padding-bottom: 15px;
#             border-bottom: 2px solid var(--gray);
#         }
        
#         .stButton>button {
#             background: linear-gradient(90deg, var(--primary), var(--secondary));
#             color: var(--dark);
#             border: none;
#             border-radius: 12px;
#             padding: 0.75em 1.5em;
#             font-weight: bold;
#             font-size: 1.1em;
#             transition: all 0.3s ease;
#             box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         }
        
#         .stButton>button:hover {
#             transform: translateY(-2px);
#             box-shadow: 0 6px 8px rgba(0,0,0,0.15);
#         }
        
#         .stTextInput>div>input {
#             border-radius: 12px;
#             padding: 12px 15px;
#             border: 1px solid var(--gray);
#             background-color: rgba(43, 45, 66, 0.5);
#             color: var(--light);
#         }
        
#         .movie-card {
#             background: linear-gradient(135deg, rgba(43, 45, 66, 0.8), rgba(33, 35, 52, 0.9));
#             padding: 20px;
#             margin: 10px;
#             border-radius: 15px;
#             text-align: center;
#             font-weight: 500;
#             transition: all 0.3s ease;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#             border: 1px solid rgba(255,255,255,0.1);
#             height: 100%;
#         }
        
#         .movie-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 8px 16px rgba(0,0,0,0.3);
#             border: 1px solid var(--secondary);
#         }
        
#         .movie-poster {
#             border-radius: 10px;
#             margin-bottom: 10px;
#             height: 200px;
#             object-fit: cover;
#             width: 100%;
#         }
        
#         .rating {
#             color: var(--secondary);
#             font-weight: bold;
#             margin: 5px 0;
#         }
        
#         .genre {
#             display: inline-block;
#             background: rgba(255, 74, 74, 0.2);
#             padding: 3px 8px;
#             border-radius: 20px;
#             font-size: 0.8em;
#             margin: 3px;
#         }
        
#         .sidebar .sidebar-content {
#             background: linear-gradient(145deg, var(--darker), #1a1c22);
#             border-right: 1px solid rgba(255,255,255,0.1);
#         }
        
#         .footer {
#             text-align: center;
#             margin-top: 50px;
#             padding-top: 20px;
#             border-top: 1px solid var(--gray);
#             color: rgba(255,255,255,0.6);
#             font-size: 0.9em;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Sample movie database (replace with your actual data)
# movie_database = {
#     "Interstellar": {
#         "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
#         "rating": 8.6,
#         "genres": ["Sci-Fi", "Adventure", "Drama"],
#         "year": 2014
#     },
#     "The Shawshank Redemption": {
#         "poster": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
#         "rating": 9.3,
#         "genres": ["Drama"],
#         "year": 1994
#     },
#     "The Dark Knight": {
#         "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
#         "rating": 9.0,
#         "genres": ["Action", "Crime", "Drama"],
#         "year": 2008
#     },
#     "Pulp Fiction": {
#         "poster": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
#         "rating": 8.9,
#         "genres": ["Crime", "Drama"],
#         "year": 1994
#     },
#     "Inception": {
#         "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg",
#         "rating": 8.8,
#         "genres": ["Action", "Adventure", "Sci-Fi"],
#         "year": 2010
#     }
# }

# # ---- Sidebar ----
# with st.sidebar:
#     st.markdown("## 🔍 Filters")
    
#     # Genre filter
#     all_genres = list(set(genre for movie in movie_database.values() for genre in movie["genres"]))
#     selected_genres = st.multiselect(
#         "Select genres:",
#         options=all_genres,
#         default=all_genres[:2]
#     )
    
#     # Rating filter
#     min_rating = st.slider(
#         "Minimum rating:",
#         min_value=0.0,
#         max_value=10.0,
#         value=7.0,
#         step=0.1
#     )
    
#     # Year range filter
#     year_range = st.slider(
#         "Release year range:",
#         min_value=1950,
#         max_value=2023,
#         value=(1990, 2020)
#     )

# # ---- Main Content ----
# st.markdown("<h1 class='title'>🍿 CineMatch AI</h1>", unsafe_allow_html=True)
# st.markdown("### Discover your next favorite movie with AI-powered recommendations")

# # Movie input box with improved placeholder
# movie_name = st.text_input(
#     "Search for a movie you like:",
#     placeholder="e.g. Interstellar, The Dark Knight, Pulp Fiction...",
#     key="movie_search"
# )

# # Recommendation button with loading state
# if st.button("Find Similar Movies 🚀", key="recommend_btn"):
#     if movie_name:
#         # Simulate recommendation logic (replace with your actual model)
#         with st.spinner('🔍 Finding the perfect recommendations...'):
#             # Filter movies based on sidebar selections
#             filtered_movies = [
#                 title for title, data in movie_database.items()
#                 if any(genre in selected_genres for genre in data["genres"]) and
#                 data["rating"] >= min_rating and
#                 year_range[0] <= data["year"] <= year_range[1]
#             ]
            
#             # Get 5 random movies from filtered list (or all if less than 5)
#             recommended_movies = random.sample(
#                 filtered_movies, 
#                 min(5, len(filtered_movies))
#             ) if filtered_movies else list(movie_database.keys())[:5]
            
#             # Display recommendations
#             st.markdown("### 🎬 Recommended For You")
#             st.markdown(f"<p style='color: rgba(255,255,255,0.7);'>Based on your selection: <strong>{movie_name}</strong></p>", unsafe_allow_html=True)
            
#             # Display movie cards in a grid
#             cols = st.columns(5)
#             for i, movie in enumerate(recommended_movies):
#                 with cols[i]:
#                     movie_data = movie_database.get(movie, {})
#                     st.markdown(f"""
#                         <div class='movie-card'>
#                             <img src='{movie_data.get("poster", "https://via.placeholder.com/200x300?text=No+Poster")}' class='movie-poster'>
#                             <h4>{movie}</h4>
#                             <div class='rating'>⭐ {movie_data.get("rating", "N/A")}/10</div>
#                             <div>{movie_data.get("year", "")}</div>
#                             <div>
#                                 {''.join([f'<span class="genre">{g}</span>' for g in movie_data.get("genres", [])])}
#                             </div>
#                         </div>
#                     """, unsafe_allow_html=True)
#     else:
#         st.warning("Please enter a movie name to get recommendations")

# # Footer
# st.markdown("""
#     <div class='footer'>
#         <p>CineMatch AI © 2023 | Powered by Machine Learning</p>
#         <p>Data from TMDB | Recommendations based on collaborative filtering</p>
#     </div>
# """, unsafe_allow_html=True)


import streamlit as st
import pickle
import pandas as pd

# Load movie dict file
with open('movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)

# Convert to DataFrame
movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎥 Movie Recommendation App")
st.markdown("Select a movie and get similar recommendations.")

# Dropdown to select movie
selected_movie = st.selectbox("Choose a Movie", movies['original_title'].values)

# Dummy recommend function (you can replace this with real logic)
def recommend(movie):
    # For now: return 5 random movies
    return movies['original_title'].sample(5).values

if st.button("Show Recommendations"):
    st.markdown("### Recommended Movies:")
    recommended_movies = recommend(selected_movie)
    for movie in recommended_movies:
        st.write(f"📌 {movie}")
    
