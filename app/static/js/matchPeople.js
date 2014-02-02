var imported = document.createElement('script');
imported.src = "https://maps.googleapis.com/maps/api/js?sensor=false";
document.head.appendChild(imported);

var imported = document.createElement('script');
imported.src = "/static/js/markerwithlabel.js";
document.head.appendChild(imported);

var map;
var peopleAtLocation = new Array();
var places = [
      ['Skibo',40.443452468900105, -79.94170546531677 ],
      ['Asiana',40.44349329460666, -79.94571805000305],
      ["The UC", 40.443281000661685, -79.94204878807068],
      ['Resnik',40.44253796657429, -79.939945936203],
      ['The Exchange',40.44150097120604, -79.94205951690674 ],
      ['The Underground', 40.44526510638198,  -79.94346499443054]
    ];

function setMarkers(map, locations) {
     var db = new Firebase('https://dxc.firebaseio.com/sell');
    var query = db.limit(50);
    query.on('value', function(snapshot){
    var people = snapshot.val();
      for (var i = 0; i < locations.length; i++) {
      peopleAtLocation[i] = 0;
      var place = locations[i];
      for(key in people){
        if(people[key].location === locations[i][0])
          peopleAtLocation[i]++;}
    var myLatLng = new google.maps.LatLng(place[1], place[2]);
    console.log(peopleAtLocation[i]);

}
}
)}

navigator.geolocation.getCurrentPosition(function(position) {
  makeLabel(position.coords.latitude, position.coords.longitude);
  findClosestFood(position.coords.latitude, position.coords.longitude);

function findClosestFood(latitude, longitude){
var closestFoodArray = new Array();
var minDistance = 0;
var minLocation = -1;
for(var i = 0; i < places.length; i++){
  var otherLatitude = places[i][1];
  var otherLongitude = places[i][2];
  var distance = Math.sqrt(Math.pow(latitude-otherLatitude,2)+Math.pow(longitude-otherLongitude,2));
  if(distance < minDistance || minLocation === -1){
    if(peopleAtLocation[i] > 0){
      closestFoodArray = places[i][0] + closestFoodArray;
    }
    else{
      closestFoodArray = closestFoodArray + places[i][0];
    }
    minDistance = distance;
    minLocation = i;
  }
  else{
    closestFoodArray = closestFoodArray + places[i][0];
  }
}
var studentDatabase = new Firebase('https://dxc.firebaseio.com/sellerMap');
var closestFood = closestFoodArray[0][0];
for(var i = 0; i < locations.length; i++){
    if(locations[i][0] === closestFood){
        var amountOfStudents = peopleAtLocation[i];
    }
    studentDatabase.child('location').set(closestFood);
    studentDatabase.child('amountOfStudents').set(amountOfStudents);

}
}


});