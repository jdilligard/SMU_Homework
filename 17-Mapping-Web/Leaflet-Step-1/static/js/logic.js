$(document).ready(function() {

    getMap()

});

function getRadius(mag) {
    var radius = 30000 * mag;
    return radius
}

function getMap() {

    // loading GeoJSON file - Here my html and usa_adm.geojson file resides in same folder
    $.getJSON("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson", function(data) {
        // L.geoJson function is used to parse geojson file and load on to map
        // L.geoJson(data).addTo(mymap);

        console.log(data.features[0].properties)
        console.log(data.features[0].geometry.coordinates.slice(0, 2))
        var date = new Date(data.features[0].properties.time * 1000)
        console.log(date)
            // Loop through the cities array and create one marker
            // for each city object



        for (var i = 0; i < data.features.length; i++) {
            var mag = parseFloat(data.features[i].properties.mag);
            var color = getColor(mag)

            // dateObj = new Date(parseInt(data.features[i].properties.time) * 1000)
            // doTable(data.features[i], i)
            var date = getTime(data.features[i].properties.time)
            L.circle(data.features[i].geometry.coordinates.slice(0, 2).reverse(), {
                fillOpacity: 0.75,
                color: "white",
                fillColor: color,
                // Setting our circle's radius equal to the output of our markerSize function
                // This will make our marker's size proportionate to its population
                // radius: markerSize(data.features[i].properties.mag)
                radius: getRadius(data.features[i].properties.mag)

            }).bindPopup("<h5>" + data.features[i].properties.place + "<br>" + date + " </h5> <hr> <h6>Magnitude: " + data.features[i].properties.mag + "</h6 > ").addTo(mymap);
        }
        var legend;
        legend = L.control({ position: 'bottomright' });

        legend.onAdd = function() {
            var div = L.DomUtil.create("div", "info legend");
            div.innerHTML += "<h4>Magnitudes</h4>";
            div.innerHTML += '<i style="background: #477AC2"></i><span>0-1</span><br>';
            div.innerHTML += '<i style="background: #448D40"></i><span>1-2</span><br>';
            div.innerHTML += '<i style="background: #E6E696"></i><span>2-3</span><br>';
            div.innerHTML += '<i style="background: #E8E6E0"></i><span>3-4</span><br>';
            div.innerHTML += '<i style="background: #FFFFFF"></i><span>4-5</span><br>';
            div.innerHTML += '<i style="background: #FFFFFF"></i><span>5+</span><br>';

            return div;
        }

        legend.addTo(mymap);

    });

}

function getTime(given_seconds) {
    given_seconds = parseInt(given_seconds)
    dateObj = new Date(given_seconds);

    return dateObj.toUTCString();

}

function addMyLed() {
    var legend;
    legend = L.control({ position: 'bottomleft' });

    legend.onAdd = function() {
        var div = L.DomUtil.create("div", "info legend");
        div.innerHTML += "<h4>Magnitudes</h4>";
        div.innerHTML += '<i style="background: #477AC2"></i><span>0-1</span><br>';
        div.innerHTML += '<i style="background: #448D40"></i><span>1-2</span><br>';
        div.innerHTML += '<i style="background: #E6E696"></i><span>2-3</span><br>';
        div.innerHTML += '<i style="background: #E8E6E0"></i><span>3-4</span><br>';
        div.innerHTML += '<i style="background: #FFFFFF"></i><span>4-5</span><br>';
        div.innerHTML += '<i style="background: #FFFFFF"></i><span>5+</span><br>';

        return div;
    }

    legend.addTo(map);
}

function getColor(mag) {
    var color = 'green'; //light green is default

    if (mag < 1) {
        color = 'blue';
    } else if (mag < 2) {
        color = 'green';
    } else if (mag < 3) {
        color = 'yellow';
    } else if (mag < 4) {
        color = 'orange';
    } else if (mag < 5) {
        color = 'red';
    } else {
        color = 'purple';
    }
    return color;


}

function doTable(data, i) {
    var date = getTime(data.features.properties.time)
    var mytable = document.getElementById("table")
    mytable.getElementById("table").insert_Row(i)



    var table_string = `<tr>
    <td>${date}</td>
    <td>${features.properties.place }</td>
    <td>${data.features.properties.mag}</td>
    <td>M${data.features.geometry.coordinates.slice(0, 2)}</td>
    <td>${data.features.geometry.coordinates.slice(2, 3)}</td>
    <td>${data.features.properties.url}</td>
 
  </tr>`;


    console.log(table_string)

}