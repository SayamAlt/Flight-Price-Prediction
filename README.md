# About Dataset

## INTRODUCTION

The objective of the study is to analyze the flight booking dataset obtained from the “Ease My Trip” website and to conduct various statistical hypothesis tests in order to get meaningful information from it. The 'Linear Regression' statistical algorithm would be used to train the dataset and predict a continuous target variable. 'Easemytrip' is an internet platform for booking flight tickets, and hence a platform that potential passengers use to buy tickets. A thorough study of the data will aid in the discovery of valuable insights that will be of enormous value to passengers.

### Research Questions

The aim of this study is to answer the below research questions:

a) Does the price vary with Airlines? <br>
b) How is the price affected when tickets are bought just 1 or 2 days before departure? <br>
c) Does the ticket price change based on the departure time and arrival time? <br>
d) How does the price change with changes in Source and Destination? <br>
e) How does the ticket price vary between Economy and Business class?

### DATA COLLECTION AND METHODOLOGY

The Octoparse scraping tool was used to extract data from the website. Data was collected in two parts: one for economy class tickets and another for business class tickets. A total of 3,00,261 distinct flight booking options were extracted from the site. Data was collected for 50 days, from February 11th to March 31st, 2022.
The data source was secondary data and was collected from the Ease My Trip website.

### DATASET

The dataset contains information about flight booking options from the website Easemytrip for flight travel between India's top six metro cities. There are 300261 datapoints and 11 features in the dataset.

### FEATURES

The various features of the dataset are explained below:

<table>
  <tr>
    <th>Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Airline</td>
    <td>The name of the airline company is stored in the airline column. It is a categorical feature with six different airlines.</td>
  </tr>
  <tr>
    <td>Flight</td>
    <td>Flight stores information regarding the plane's flight code. It is a categorical feature.</td>
  </tr>
  <tr>
    <td>Source City</td>
    <td>City from which the flight takes off. It is a categorical feature with six unique cities.</td>
  </tr>
  <tr>
    <td>Departure Time</td>
    <td>This is a derived categorical feature, obtained by grouping time periods into bins. It stores information about the departure time and has six unique time labels.</td>
  </tr>
  <tr>
    <td>Stops</td>
    <td>A categorical feature with three distinct values that stores the number of stops between the source and destination cities.</td>
  </tr>
  <tr>
    <td>Arrival Time</td>
    <td>This is a derived categorical feature, obtained by grouping time intervals into bins. It has six distinct time labels and stores information about the arrival time.</td>
  </tr>
  <tr>
    <td>Destination City</td>
    <td>City where the flight will land. It is a categorical feature with six unique cities.</td>
  </tr>
  <tr>
    <td>Class</td>
    <td>A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.</td>
  </tr>
  <tr>
    <td>Duration</td>
    <td>A continuous feature that displays the overall amount of time it takes to travel between cities in hours.</td>
  </tr>
  <tr>
    <td>Days Left</td>
    <td>This is a derived characteristic that is calculated by subtracting the trip date from the booking date.</td>
  </tr>
  <tr>
    <td>Price</td>
    <td>Target variable that stores information of the ticket price.</td>
  </tr>
</table>
