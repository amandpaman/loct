import streamlit as st
import geocoder
import folium
from streamlit_folium import folium_static

def get_location():
    g = geocoder.ip('me')
    return g.latlng

def create_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup="Your Location").add_to(m)
    return m

def main():
    st.title("Location Sharing App")
    st.subheader("Get Your Current Location")

    if st.button("Access GPS"):
        st.write("Accessing GPS...")
        location = get_location()
        if location:
            lat, lon = location
            st.write(f"Your location: {lat}, {lon}")
            m = create_map(lat, lon)
            folium_static(m, width=700, height=500)
            if st.button("Share Location"):
                st.write("Location shared successfully!")
                # Add your location-sharing logic here
        else:
            st.error("Unable to get your location")

if __name__ == "__main__":
    main()
