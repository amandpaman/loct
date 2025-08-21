import streamlit as st
import geocoder
import folium

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

    if st.button("Get Location"):
        location = get_location()
        if location:
            lat, lon = location
            st.write(f"Your location: {lat}, {lon}")
            m = create_map(lat, lon)
            folium_static = st_folium(m, width=700, height=500)
        else:
            st.error("Unable to get your location")

    st.subheader("Enter Custom Location")
    lat_input = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=0.0)
    lon_input = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=0.0)

    if st.button("Create Map"):
        m = create_map(lat_input, lon_input)
        folium_static = st_folium(m, width=700, height=500)

def st_folium(m, width=700, height=500):
    import folium
    from streamlit_folium import folium_static
    return folium_static(m, width=width, height=height)

if __name__ == "__main__":
    main()
