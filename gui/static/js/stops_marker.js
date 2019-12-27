var stop_marker = (L.marker([parseFloat(latitude), parseFloat(longitude)], { icon: greenIcon }))
    .addTo(map)
    .bindPopup(name)
    .openPopup();
