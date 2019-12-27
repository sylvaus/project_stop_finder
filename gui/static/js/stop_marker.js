var stop_marker = (L.marker([parseFloat(stopLat), parseFloat(stopLng)], { icon: greenIcon }))
    .addTo(map)
    .bindPopup(stopName)
    .openPopup();

current_location_e_lat = sessionStorage.getItem('current_location_e_lat_key');
current_location_e_lng = sessionStorage.getItem('current_location_e_lng_key');
var current_location_marker = (L.marker([parseFloat(current_location_e_lat), parseFloat(current_location_e_lng)]))
    .addTo(map)
    .bindPopup("your current location")
    .openPopup();