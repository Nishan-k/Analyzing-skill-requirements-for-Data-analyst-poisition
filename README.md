# An ETL data pipeline for Analyzing a Data Analyst Role for all 16 States in Germany

<img src="./images/workflow.png" alt="DE-workflow" title="Data Pipeline Worflow">


## Goal Of The Project:
Extract the vacancies posted for a data analyst role from Indeed using a spider build in Scrapy for all the 16 states and visualize the data in Tableau as a dashboard to show which programming languages, tools, education level, salary, prferred communication language, libraries and packages are needed to be a well-equipped data analyst.

## Table of Contents:
<ol>
    <li><a href="#about_the_data"> <b>About The Data </a></b></li>
        <li><a href="#extract"><b> Extract </a></b></li>
        <li><a href="#transform"><b> Transform </a> </b>
        </li>
        <li><a href="#load"><b> Load </a> </b></li>
        <li><a href="#visualize"><b> Dashboard </a> </b></li>
    </li>
</ol>

<h3 id ="about_the_data">1. About The Data:</h3>
I have built a spider in Scrapy, that extracts the requirement field of the vacancy that has been posted for a data analyst role. So, each time a spider crawls, it focuses on one state and then move on to another, until all the data has been extracted for all the 16 states. 

<li><a href="#extract"><b> Extract </a></b></li>