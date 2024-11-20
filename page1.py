import streamlit as st
import requests

# Sidebar for filters
st.sidebar.title("Filters")

# Price range slider
price_range = st.sidebar.slider("Price Range", 20, 120, (20, 120), step=10)

# Display price range in a styled format
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

# Activity selection buttons
st.sidebar.markdown("### Activities")
col4, col5, col6 = st.sidebar.columns(3)

with col4:
    nightlife = st.button("🌙 Nightlife")

with col5:
    shopping = st.button("🛍️ Shopping")

with col6:
    sightseeing = st.button("👁️ Sightseeing")

# Display selected filters
selected_categories = []
if art: selected_categories.append('Art')
if music: selected_categories.append('Music')
if food: selected_categories.append('Food')
if sports: selected_categories.append('Sports')
if history: selected_categories.append('History')
if parks: selected_categories.append('Parks')

selected_activities = []
if nightlife: selected_activities.append('Nightlife')
if shopping: selected_activities.append('Shopping')
if sightseeing: selected_activities.append('Sightseeing')

st.write(f"Selected Price Range: ${price_range[0]} - ${price_range[1]}")
st.write(f"Selected Categories: {', '.join(selected_categories)}")
st.write(f"Selected Activities: {', '.join(selected_activities)}")

# Placeholder function to generate an itinerary
def generate_itinerary(categories, activities, budget):
    # Placeholder: Example itinerary logic
    itinerary = []
    if "Art" in categories:
        itinerary.append("Morning: Visit the Modern Art Museum.")
    if "Food" in categories:
        itinerary.append("Lunch: Enjoy local cuisine at a popular downtown eatery.")
    if "Parks" in categories:
        itinerary.append("Afternoon: Relax at the Central City Park.")
    if "Nightlife" in activities:
        itinerary.append("Evening: Explore the vibrant downtown nightlife.")
    if "Shopping" in activities:
        itinerary.append("Optional: Shop for souvenirs at the city center.")
    
    itinerary.append(f"Budget consideration: Your daily budget is ${budget[0]} - ${budget[1]}.")
    return itinerary

# Generate an itinerary based on user input
if selected_categories or selected_activities:
    st.write("Generating your travel itinerary...")
    itinerary = generate_itinerary(selected_categories, selected_activities, price_range)
    for step in itinerary:
        st.markdown(f"📌 {step}")
else:
    st.write("Please select at least one category or activity to generate an itinerary.")
# Placeholder for API integration
st.write("Fetching places based on your selection...")

# Function to fetch data from TripAdvisor API
def fetch_places_from_tripadvisor(categories, activities, price_range, api_key):
    base_url = "https://api.tripadvisor.com/v2/places"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Construct parameters for the request
    params = {
        "categories": ','.join(categories),
        "activities": ','.join(activities),
        "price_min": price_range[0],
        "price_max": price_range[1],
        "location": "San Francisco"  # Change to dynamic location based on user input
    }
    
    try:
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

# Call the function to fetch data from the TripAdvisor API
tripadvisor_api_key = "971E6EAC0EAD43D8BB1E1EE2AE713CAD"
places_tripadvisor = fetch_places_from_tripadvisor(selected_categories, selected_activities, price_range, tripadvisor_api_key)

# Display fetched places
if "error" in places_tripadvisor:
    st.write(f"Error fetching data: {places_tripadvisor['error']}")
else:
    st.write("Places from TripAdvisor:")
    for place in places_tripadvisor.get("data", []):
        st.write(f"**{place.get('name')}** - {place.get('description', 'No description available')}")
