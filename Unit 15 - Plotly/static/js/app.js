
//bubble chart function to be put into the 'bubble' section of the html

function bubblechart(data){

    //parse through data to get the right values 
    xvalues = data.otu_ids;
    yvalues = data.sample_values;
    markersize = data.sample_values;
    markercolour = data.otu_ids;
    textvalues = data.otu_labels;

 //build the information for the bubble chart and then plot 

    var trace = {
        x: xvalues,
        y: yvalues,
        mode: 'markers',
        marker: {
            color: markercolour,
            size: markersize,
        },
        text: textvalues
    }

    info = [trace];

    Plotly.newPlot('bubble',info);

}

//metadata function to put into the 'sample-metadata' section of the html

function metadata(data){
    var metadatas = d3.select("#sample-metadata");
    
    metadatas.html("")

    Object.entries(data).forEach(([key, value]) => {
        metadatas.append("h6").text(`${key.toUpperCase()}: ${value}`)});
    
  

}


//bar chart function to be put into the 'bar' section of the html

function BarChart(data){

    // get the top 10 values and then reverse those top 10 so that it shows highest to lowest in the bar graph
    values = data.sample_values.slice(0,10);
    labels = data.otu_ids.slice(0,10);
    hovertext = data.otu_labels.slice(0,10);

    labels = labels.reverse();
    hovertext = hovertext.reverse();
    values = values.reverse();

    //add in the text for the labels so that it is more descriptive

    for(var i=0; i <labels.length; i++){
        labels[i] = "OTU " + labels[i];
       } 

    //build the information for the horizontal bar plot and then plot 

    var trace = [{
        type: 'bar',
        x: values,
        y: labels,
        orientation: 'h',
        text: hovertext
    }]

    Plotly.newPlot("bar",trace);

}

// function to find index of the array - yes, there is a better way but i'm crunched for time.... 

function filterforid(data,testno){
    var i = 0;
    while (i <data.length){
        if (data[i] == testno) return i;
        else i= i+1;
    }
    return -1;
}


//listen for a new test id to be changed

function optionChanged(testno){

    //pull all the data into arrays

    d3.json("samples.json").then((importedData) => {
        var biodata = importedData.samples;
        var indivdata = importedData.metadata;
        var idnames = importedData.names;

        //search through the idnames and return the index for that specific datpoint

        var id = filterforid(idnames, testno);

        //use the index for all the functions to display that individuals data

        bubblechart(biodata[id]);
        metadata(indivdata[id]);
        BarChart(biodata[id]);
    });
}


// start of the main program - initialize the page, get the data from the json

d3.json("samples.json").then((importedData) => {
var biodata = importedData.samples;
var indivdata = importedData.metadata;
var idnames = importedData.names;

//send to each of the functions the first datapoint to initialize the displays

bubblechart(biodata[0]);
metadata(indivdata[0]);
BarChart(biodata[0]);

//create the dropdown menu utilizing the idnames array

var select = document.getElementById("selDataset");

for(var index=0; index <idnames.length; index++){
     select.options.add(new Option(idnames[index]));
    }


});




   

