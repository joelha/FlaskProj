$(function(){
  periodDropDown = $("#period-choice");
  stationDropDown = $("#station-choice");
  temperatureText = document.getElementById("tempText");
});

$(function(){
  var entry = this;
  $.getJSON('http://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1.json', function(result){
        console.log(result);

        stationsList = [];
        var stations = result.station;
        for (var key in stations) {
          if(stations.hasOwnProperty(key)) {

            var obj = {
              key: key,
              name: stations[key].name, 
              href: stations[key].link[0].href,
            }
            stationsList.push(obj);
            stationDropDown.append("<option>" + stationsList[key].name + "</option>");
          }
        };
       
      }
    );
});

function changedStation () {
  console.log("change station!");
  var stationName = stationDropDown.find(":selected").text();
  console.log(stationName);

  periodDropDown.empty();
  periodDropDown.append("<option>None</option>");
  temperatureText.innerHTML = "-";

  var url = undefined;

  for (var i = 0; i < stationsList.length; i++) {
    if(stationsList[i].name === stationName) {
      url = stationsList[i].href;
    }
  }

  $.getJSON(url, function(result) {

    console.log(result.period[0]);
    console.log(result.period[0].link[0].href);

    periodsList = [];
    var periods = result.period;

    for(var j = 0; j < periods.length; j++) {
      if(periods[j] !== undefined && periods[j].key !== undefined) {
        console.log(periods[j]);

        var obj = {
          key: periods[j].key,
          href: periods[j].link[0].href,
        }
        periodsList.push(obj);
        periodDropDown.append("<option>" + obj.key + "</option>");
      }
    }
  });

  
}

function changedPeriod () {
  console.log("changed period");
  var period = periodDropDown.find(":selected").text();

  var url = undefined;

  for(var i = 0; i < periodsList.length; i++) {
    if(periodsList[i].key == period) {
      url = periodsList[i].href;
      break;
    }
  }

  $.getJSON(url, function(result) {

    console.log(result);
    var href = undefined;
    
    for (var i = 0; i < result.data.length; i++) {
      for (var j = 0; j < result.data[i].link.length; j++) {
          if (result.data[i].link[j].rel === 'data' && result.data[i].link[j].type === 'application/json') {
              href = result.data[i].link[j].href;
          }
      }
    }

    if(href !== undefined) {
      $.getJSON(href, function(data) {
        console.log(data);
        temperatureText.innerHTML = data.value[0].value;
      });
    } else {
      console.log("href undefined");
    }
  });

}


