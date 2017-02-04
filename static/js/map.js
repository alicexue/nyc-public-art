function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: {lat: 40.728857, lng: -73.960074},
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