function myMap() {
var mapProp= {
    center:new google.maps.LatLng(40.728857, -73.960074),
    zoom:11,
};
var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

//add markers
//var myLatLng = new google.maps.LatLng(latitudes[i], longitudes[i]);
var myLatLng = {lat: 40.728857, lng: -73.960074};
var marker = new google.maps.Marker({
  position: myLatLng,
  map: map,
  title: 'Hello World!'
});

// don't let people pan past NYC
var allowedBounds = new google.maps.LatLngBounds(
  new google.maps.LatLng(40.488482, -74.267916),
  new google.maps.LatLng(41.296556, -73.653525)
);
var lastValidCenter = map.getCenter();


map.addListener('center_changed', function() {
     if (allowedBounds.contains(map.getCenter())) {
        lastValidCenter = map.getCenter();
     }
     else {
       // not valid anymore => return to last valid position
       map.panTo(lastValidCenter);
     }
});


}
