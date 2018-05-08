// Get references to the tbody element, input field and button
var tbody = document.querySelector("tbody");
var cityInput = document.querySelector("#city");
var searchBtn = document.querySelector("#search");

searchBtn.addEventListener("click", handleSearchButtonClick);
var filteredcity = dataSet;

function renderTable() {
    tbody.innerHTML = "";
    for (var i = 0; i < filteredcity.length; i++) {
      // Get get the current  object and its fields
      var ufo_cities = filteredcity[i];
      var fields = Object.keys(ufo_cities);
      // Create a new row in the tbody,
      var row = tbody.insertRow(i);
      for (var j = 0; j < 7; j++) {
        // For every field in the address object, 
        // create a new cell and set its inner text to be the current value
        // at the current value's field
        var field = fields[j];
        console.log(field)
        var cell = row.insertCell(j);
        cell.innerText = ufo_cities[field];
        console.log(j)
        }
        row.deleteCell(5)
    }
  };


function handleSearchButtonClick() {
    
    var filterCity = cityInput.value.trim().toLowerCase();
  
    // Set filteredAddresses to an array of all addresses whose "state" 
    // matches the filter
    filteredcity = dataSet.filter(function(cities) {
      var data_city = cities.city.toLowerCase();
  
      // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
      return data_city === filterCity;
    });
    renderTable();
}

renderTable();