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

# Function to fetch data from Tripadvisor API with Referer header
def fetch_places_from_tripadvisor(location, api_key):
    base_url = "https://api.content.tripadvisor.com/api/v1/location/search"
    headers = {
        "Referer": "https://travel-partner.streamlit.app",  # Update as per the requirement in the image
    }
    params = {
        "key": api_key,
        "searchQuery": location,
        "category": ','.join(selected_categories) if selected_categories else None,
        "price": f"{price_range[0]}-{price_range[1]}" if price_range else None,
        "limit": 10  # Number of results to return
    }
    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

# Call the Tripadvisor API
tripadvisor_api_key = "971E6EAC0EAD43D8BB1E1EE2AE713CAD"  # Replace with your actual API key
location_query = "India"  # You can replace this with a dynamic input
places_tripadvisor = fetch_places_from_tripadvisor(location_query, tripadvisor_api_key)

# Display fetched places
st.write("Fetching places from Tripadvisor...")

if "error" in places_tripadvisor:
    st.write(f"Error fetching data: {places_tripadvisor['error']}")
else:
    st.write("Places from Tripadvisor:")
    locations = places_tripadvisor.get("data", [])
    if locations:
        for place in locations:
            st.write(f"**{place.get('name', 'No Name')}**")
            st.write(f"📍 Address: {place.get('address', 'No address available')}")
            st.write(f"💵 Price Level: {place.get('price_level', 'N/A')}")
            st.write(f"🌟 Rating: {place.get('rating', 'N/A')}")
            st.write("---")
    else:
        st.write("No places found for the selected location.")
