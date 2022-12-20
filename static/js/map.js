function initMap() {
  // Display the area of the map
  var map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 14.5995, lng: 120.9842 },
    zoom: 12,
  });

  // Get the latitude and longitude from the map (when clicked)
  google.maps.event.addListener(map, 'click', function (event) {
    alert("Latitude: " + event.latLng.lat() + " " + ", longitude: " + event.latLng.lng());
  });
}