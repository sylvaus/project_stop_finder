var greenIcon = L.icon({
    iconUrl: '.\/..\/static\/img\/130066.png',
    iconSize: [20, 20], // size of the icon
    iconAnchor: [19, 20], // point of the icon which will correspond to marker's location
    popupAnchor: [-2, -26] // point from which the popup should open relative to the iconAnchor
});
var map = L.map('map').setView([45.55048169934218, -73.64822387695314], 10);
map.addLayer(
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; \
                    <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, \
                    <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © \
                    <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        accessToken: 'pk.eyJ1IjoiamFhc3NiIiwiYSI6ImNrNGt1bGFmaDIxbHkzbW9ic2Jhbm44bjYifQ.ReKnSfsBy5BO_YZvYgIo5A'
    })
);
function onMapClick(e) {
    L.popup()
        .setLatLng(e.latlng)
        .setContent("your current location is " + e.latlng.toString())
        .openOn(map);

    document.getElementById('current_location').value = e.latlng.lat + ', ' + e.latlng.lng;
    current_location_e_lat = e.latlng.lat.toString();
    current_location_e_lng = e.latlng.lng.toString();
    sessionStorage.setItem("current_location_e_lat_key", current_location_e_lat);
    sessionStorage.setItem("current_location_e_lng_key", current_location_e_lng);
}
map.on('click', onMapClick);