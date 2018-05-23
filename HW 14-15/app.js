// Chart Params
var svgWidth = 960;
var svgHeight = 500;

var margin = { top: 20, right: 40, bottom: 60, left: 100 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import data from an external CSV file
d3.csv("combined_data_25_34.csv", function(error, csvData) {
    if (error) throw error;
  
    console.log(csvData);
    console.log([csvData]);

    csvData.forEach(function (data) {
        data.edu_percent = +data.edu_percent;
        data.obesity_percent = +data.obesity_percent;
      });
    
    // Create scaling functions
    var xScale = d3.scaleLinear()
      .domain([0,d3.max(csvData, d => d.edu_percent)+2])
      .range([0, width]);
  
    var yScale = d3.scaleLinear()
      .domain([d3.min(csvData, d => d.obesity_percent)-2,d3.max(csvData, d => d.obesity_percent)+2])
    //   d3.extent(csvData, d => d.obesity_percent_65_plus))
      .range([height, 0]);
  
  
    // Create axis functions
    var bottomAxis = d3.axisBottom(xScale)
    var leftAxis = d3.axisLeft(yScale);

  
    // Add x-axis
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);
  
    // Add y-axis to the left side of the display
    chartGroup.append("g")
      .call(leftAxis);
    
    // Step 5: Create Circles  
    var circlesGroup = chartGroup.selectAll("circle")
        .data(csvData)
        .enter()
        .append("circle")
        .attr("class", "dot")
        .attr("cx", d => xScale(d.edu_percent))
        .attr("cy", d => yScale(d.obesity_percent))
        .attr("r", "5")
        .attr("fill", "red")
        .attr("opacity", "1")
  
    // Create axes labels
    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 40)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Ages 25-34 Obesity %");

    chartGroup.append("text")
        .attr("transform", `translate(${width/2}, ${height + margin.top + 30})`)
        .attr("class", "axisText")
        .text("Ages 25-34 Education %");
       
    //  // Step 6: Initialize tool tip
    var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function (d) {
          return (`${d.State}<br>Education: ${d.edu_percent} <br>Obesity: ${d.obesity_percent}%`);
        });
    
    // Step 7: Create tooltip in the chart
    chartGroup.call(toolTip);

    // Step 8: Create event listeners to display and hide the tooltip
    circlesGroup.on("mouseover", function (data) {
            toolTip.show(data);
    })
    // onmouseout event
        .on("mouseout", function (data, index) {
            toolTip.hide(data);
    });
    
    // Legend
    var legend = chartGroup.append("g")
        .attr("class", "legend")
        

    // draw legend colored rectangles
    legend.append("circle")
        .attr("cx", width - 5)
        .attr("cy", height - 410)
        .attr("r", 5)
        .style("fill", 'red')
        .style('stroke','black')

    // draw legend text
    legend.append("text")
        .attr("x", width - 16)
        .attr("y", 9)
        .attr("dy", ".35em")
        .style("text-anchor", "end")
        .text('obesity vs education in 25-34 year olds')

  });