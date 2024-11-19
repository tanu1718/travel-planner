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
