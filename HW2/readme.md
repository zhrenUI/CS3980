# US Population Data Viewer

## Overview

This project is a simple HTML/JavaScript web application that retrieves
and displays United States population data from the Data USA API.

When the page loads, the application sends a request to the Data USA
API, retrieves population data by year, parses the returned JSON, sorts
the data, and displays it in a formatted table.

The project demonstrates:

-   Making API requests in JavaScript
-   Parsing JSON data
-   Sorting data dynamically
-   Rendering data in HTML
-   Using the Immediately Invoked Function Expression (IIFE) pattern
-   Making API calls using XMLHttpRequest (XHR)

------------------------------------------------------------------------

## API Source

Data is retrieved from the Data USA API.

API endpoint used:

https://api.datausa.io/tesseract/data.jsonrecords?cube=acs_yg_total_population_5&measures=Population&drilldowns=Year

This endpoint returns population data grouped by year from the American
Community Survey dataset.

Example response structure:

{ "data": \[ { "Year": "2022", "Population": 331449281 }, { "Year":
"2021", "Population": 329725481 } \] }

The application extracts the `data` array and displays the values in a
table.

------------------------------------------------------------------------

## Project Structure

```
.
├── screenshots/
│   ├── USpop_page_output.png
├── index.html 
└── readme.md
```
---

Only one HTML file is required because the JavaScript and styling are
embedded directly in the page.

------------------------------------------------------------------------

## How It Works

### 1. Page Load

When the page loads, the following event listener triggers the API
request:

window.addEventListener('load', fetchPopulationData);

------------------------------------------------------------------------

### 2. IIFE Pattern

All JavaScript logic is wrapped in an Immediately Invoked Function
Expression (IIFE).

(function () { 'use strict'; // application code })();

Benefits of the IIFE pattern:

-   Prevents global namespace pollution
-   Encapsulates variables and functions
-   Improves maintainability
-   Avoids naming conflicts with other scripts

------------------------------------------------------------------------

### 3. API Request with XMLHttpRequest

The application retrieves data using the XMLHttpRequest (XHR) object.

var xhr = new XMLHttpRequest(); xhr.open('GET', API_URL, true);
xhr.responseType = 'json'; xhr.send();

Once the request completes successfully:

xhr.onload = function () { if (xhr.status \>= 200 && xhr.status \< 300)
{ var response = xhr.response; } };

------------------------------------------------------------------------

### 4. Data Parsing

The response contains a `data` array where each object represents one
year.

Example:

response.data

Each element contains:

  Field        Description
  ------------ ---------------------
  Year         Census year
  Population   Total US population

------------------------------------------------------------------------

### 5. Sorting the Data

The application sorts the population records by year (descending) before
displaying them.

var sortedRows = response.data.slice().sort(function (a, b) { return
Number(b.Year) - Number(a.Year); });

------------------------------------------------------------------------

### 6. Rendering the Table

After sorting, the application dynamically generates table rows.

rows.forEach(function (row) { html += '
```{=html}
<tr>
```
' + '
```{=html}
<td>
```
' + row.Year + '
```{=html}
</td>
```
' + '
```{=html}
<td class="right">
```
' + formatNumber(row.Population) + '
```{=html}
</td>
```
' + '
```{=html}
</tr>
```
'; });

The generated rows are inserted into the table body:

tableBodyEl.innerHTML = html;

------------------------------------------------------------------------

## Features

-   Automatically loads population data on page load
-   Uses XHR API requests
-   Uses IIFE pattern for JavaScript
-   Sorts data by year
-   Formats population values with thousands separators
-   Displays loading and error states
-   Clean responsive table layout

------------------------------------------------------------------------

## Running the Project

1.  Download or clone the repository.
2.  Open the project folder.
3.  Double-click index.html or open it in any modern browser.

No additional dependencies or installation steps are required.

------------------------------------------------------------------------

## Author

Zackary Hren