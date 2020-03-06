// from data.js
var tableData = data;

// select the table area in the HTML
var tbody = d3.select("tbody");

// fill in the table with data from the data.js file, append for each row and then for each column

function printtable(tableData){
    tbody.html("");
    tableData.forEach((data) => {
        var row = tbody.append("tr");
        Object.entries(data).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });

}

// select the button area in the HTML

var button = d3.select("#filter-btn");

// on click grab the following

button.on("click", function() {
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    var filteredData = tableData.filter(incident => incident.datetime === inputValue);

    printtable(filteredData)

     console.log(filteredData) ;
});

printtable(tableData);
