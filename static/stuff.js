function initAutocomplete() {
  console.log("6");
  var mapProp= {
      center:new google.maps.LatLng(40.728857, -73.960074),
      zoom:11,
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
  console.log("6");

  // don't let people pan past NYC
  var allowedBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(40.488482, -74.267916),
    new google.maps.LatLng(41.296556, -73.653525),
  );
  var lastValidCenter = map.getCenter();
  console.log("6");


  map.addListener('center_changed', function() {
    console.log("6")

       if (allowedBounds.contains(map.getCenter())) {
          lastValidCenter = map.getCenter();
       }
       else {
         console.log("6")

         // not valid anymore => return to last valid position
         map.panTo(lastValidCenter);
       }
  });

   // Create the search box and link it to the UI element.
  var input = document.getElementById('pac-input');
  console.log(input + "hi");
  var searchBox = new google.maps.places.SearchBox(input);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  console.log("6");
  // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    console.log("6")
    searchBox.setBounds(map.getBounds());
  });

  searchBox.addListener('places_changed', function() {
    var places = searchBox.getPlaces();
    console.log("7")
    if (places.length == 0) {
      return;
    }

    //   // Clear out the old markers.
    // markers.forEach(function(marker) {
    //   marker.setMap(null);
    //   console.log("6")
    //
    // });
    // markers = [];

      // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
      if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
      }
      var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      markers.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
      }));

      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });


  jQuery.get('http://localhost:8080/facilities.json',function(facilities){
      for (i=0;i<Object.keys(facilities).length;i++) {
      	//add markers
  		var myLatLng = {lat: facilities[i]['lat'], lng: facilities[i]['lng']};
  		var marker = new google.maps.Marker({
    		position: myLatLng,
    		map: map,
    		title: facilities[i]['name']
  		});
  		content = '<p><b>' + facilities[i]['name'] + '</b></p><p>' + facilities[i]['artist'] + '</p><p>' + facilities[i]['from_date'] + ' to ' + facilities[i]['to_date'] + '</p>'
  		photo_link = facilities[i]['photo']
  		photo_description = facilities[i]['description']
  		var infowindow = new google.maps.InfoWindow({
      		content: content
   		 });
   		google.maps.event.addListener(marker,'click', (function(marker,content,infowindow,photo_link,photo_description){
      	return function() {
          	infowindow.setContent(content);
          	infowindow.open(map,marker);
          	console.log(photo_link)
          	console.log(photo_link.substr(0,photo_link.length - 2))
          	console.log(document.getElementById("art-photo"))
          	o_html = photo_link.substr(0,photo_link.length - 2) + " id = \"art-photo\" class=\"img-responsive\"/>";
          	document.getElementById("art-photo").outerHTML = o_html;
          	document.getElementById("art-description").innerHTML = photo_description;
      		};
  		})(marker,content,infowindow,photo_link,photo_description));
      }
  });



}
