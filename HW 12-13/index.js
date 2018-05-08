// Get references to the tbody element, input field and button
var tbody = document.querySelector("tbody");
var searchInput = document.querySelector("#searchterm");
var searchBtn = document.querySelector("#search");

searchBtn.addEventListener("click", handleSearchButtonClick);
var filteredsearch = dataSet;

function renderTable() {
    tbody.innerHTML = "";
    for (var i = 0; i < 20; i++) {
      // Get get the current  object and its fields
      var ufo_search = filteredsearch[i];
      var fields = Object.keys(ufo_search);
      // Create a new row in the tbody,
      var row = tbody.insertRow(i);
      for (var j = 0; j < 7; j++) {
        // For every field in the address object, 
        // create a new cell and set its inner text to be the current value
        // at the current value's field
        var field = fields[j];
        console.log(field)
        var cell = row.insertCell(j);
        cell.innerText = ufo_search[field];
        console.log(j)
        }
        row.deleteCell(5)
    }
  };


function handleSearchButtonClick() {
    var filtersearch = searchInput.value.trim().toLowerCase();
    // Set filteredAddresses to an array of all addresses whose "state" 
    // matches the filter
    filteredsearch = dataSet.filter(function(objects){
        if(filtersearch == objects.city){
          var data_city = objects.city.toLowerCase();
          return data_city === filteredsearch;
        }
        else if(filtersearch == objects.datetime){
          var data_datetime = objects.datetime.toLowerCase();
          return data_datetime === filteredsearch;
        }
        
        // case objects.state:
        //   var data_state = objects.state.toLowerCase();
        //   return data_state === filteredsearch;
        
        // case objects.country:
        //   var data_country = objects.country.toLowerCase();
        //   return data_country === filteredsearch;
        
        // case objects.shape:
        //   var data_shape = objects.shape.toLowerCase();
        //   return data_shape === filteredsearch;

        // case objects.comments:
        //   var data_comments = objects.comments.toLowerCase();
        //   return data_comments === filteredsearch;

      
    });
    renderTable();
}

renderTable();

// switch(objects){
        
//   case objects.city:
//     filteredsearch = dataSet.filter(function(objects){
//       var data_city = objects.city.toLowerCase();
//       return data_city === filteredsearch;
//     });
//     break;
//   case objects.datetime:
//     filteredsearch = dataSet.filter(function(objects){
//       var data_datetime = objects.datetime.toLowerCase();
//       return data_datetime === filteredsearch;
//     });
//     break;
//   case objects.state:
//     filteredsearch = dataSet.filter(function(objects){
//       var data_state = objects.state.toLowerCase();
//       return data_state === filteredsearch;
//     });
//     break;
//   case objects.country:
//     var data_country = objects.country.toLowerCase();
//     return data_country === filteredsearch;
//     break;
//   case objects.shape:
//     var data_shape = objects.shape.toLowerCase();
//     return data_shape === filteredsearch;
//     break;
//   case objects.comments:
//     var data_comments = objects.comments.toLowerCase();
//     return data_comments === filteredsearch;
//     break;