import streamlit as st

# Sidebar for filters
st.sidebar.title("Filters")

# Price range slider
price_range = st.sidebar.slider("Price Range", 20, 120, (20, 120), step=10)

# Display price range in a styled format (like in the image)
st.sidebar.markdown(f"<h4 style='text-align: right;'>${price_range[0]}-${price_range[1]}</h4>", unsafe_allow_html=True)

# Category selection buttons (using columns for layout)
st.sidebar.markdown("### Categories")
col1, col2, col3 = st.sidebar.columns(3)

with col1:
    art = st.button("🎨 Art")
    music = st.button("🎵 Music")

with col2:
    food = st.button("🍽️ Food")
    sports = st.button("🏅 Sports")

with col3:
    history = st.button("🏛️ History")
    parks = st.button("🌲 Parks")

# Activity selection buttons (Nightlife, Shopping, Sightseeing)
st.sidebar.markdown("### Activities")
col4, col5, col6 = st.sidebar.columns(3)

with col4:
    nightlife = st.button("🌙 Nightlife")

with col5:
    shopping = st.button("🛍️ Shopping")

with col6:
    sightseeing = st.button("👁️ Sightseeing")

# Display selected filters
st.write(f"Selected Price Range: ${price_range[0]} - ${price_range[1]}")
selected_categories = []
if art: selected_categories.append('Art')
if food: selected_categories.append('Food')
if history: selected_categories.append('History')
if music: selected_categories.append('Music')
if sports: selected_categories.append('Sports')
if parks: selected_categories.append('Parks')

selected_activities = []
if nightlife: selected_activities.append('Nightlife')
if shopping: selected_activities.append('Shopping')
if sightseeing: selected_activities.append('Sightseeing')

st.write(f"Selected Categories: {', '.join(selected_categories)}")
st.write(f"Selected Activity: {', '.join(selected_activities)}")

# Placeholder for API integration (GeoApify and Google Places)
st.write("Fetching places based on your selection...")

# Example function to fetch data from GeoApify (you'll need an API key)
def fetch_places_from_geoapify(categories, activity, price_range):
    # Construct your API call here using the GeoApify Places API
    # Example URL: https://api.geoapify.com/v2/places?categories=food&filter=...
    pass

# Example function to fetch data from Google Places (you'll need an API key)
def fetch_places_from_google(categories, activity, price_range):
    # Construct your API call here using the Google Places API
    # Example URL: https://maps.googleapis.com/maps/api/place/nearbysearch/json?...
    pass

# Call the functions to fetch data from APIs (you can use either or both)
places_geoapify = fetch_places_from_geoapify(selected_categories, selected_activities, price_range)
places_google = fetch_places_from_google(selected_categories, selected_activities, price_range)

# Display fetched places (this is just a placeholder)
st.write("Places from GeoApify:")
st.write(places_geoapify)

st.write("Places from Google Places:")
st.write(places_google)