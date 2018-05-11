// Get references to the tbody element, input field and button
var tbody = document.querySelector("tbody");
var searchInput = document.querySelector("#searchterm");
var searchBtn = document.querySelector("#search");
searchBtn.addEventListener("click", handleSearchButtonClick);
var filteredsearch = dataSet;

function renderTable() {
    tbody.innerHTML = "";
    for (var i = 0; i < filteredsearch.length; i++) {
      
      // Get get the current  object and its fields
      var ufo_search = filteredsearch[i];
      var fields = Object.keys(ufo_search);
      // Create a new row in the tbody,
      var row = tbody.insertRow(i);
      for (var j = 0; j < fields.length; j++) {
        // For every field in the address object, 
        // create a new cell and set its inner text to be the current value
        // at the current value's field
        var field = fields[j];
        var cell = row.insertCell(j);
        cell.innerText = ufo_search[field];
        }
        row.deleteCell(5)
    }
  };


function handleSearchButtonClick() {
    var filtersearch = searchInput.value.trim().toLowerCase();
    filteredsearch = datas.filter(function(objects){
        if(filtersearch == objects.city){
          var data_city = objects.city.toLowerCase();          
          return  filteredsearch = data_city;
        }  
        else if(filtersearch == objects.datetime){
          var data_datetime = objects.datetime.toLowerCase();
          return  filteredsearch = data_datetime;
        }
         else if(filtersearch == objects.state){
          var data_state = objects.state.toLowerCase();
          return  filteredsearch = data_state;
        }
         else if(filtersearch == objects.country){
          var data_country = objects.country.toLowerCase();
          return  filteredsearch = data_country;
        }
         else if(filtersearch == objects.shape){
          var data_shape = objects.shape.toLowerCase();
          return  filteredsearch = data_shape;
        }
         else if(filtersearch == objects.comments){
          var data_comments = objects.comments.toLowerCase();
          return  filteredsearch = data_comments;
        }
    });
    renderTable();
}

renderTable();
