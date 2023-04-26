import React from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import "../style.css";




export default function About() {
  return (
    <>
      <Navbar />

      <div className="about-wrapper">
        <div className="block">
          <h1>About the Product</h1>
          <hr />
          <p>
            Swedish talent observatory is a statistical tool based on webscraping data from different job boards. The data is extracted to represent the number of applicable job ads in accordance to occupation and county in Sweden from three different job boards. Webscraping data from LinkedIn, Lediga jobb and Platsbanken, the information can be filtered by 7 parameters to find statistics of requirement-needs in job-ads for a specific occupation/profession. The 7 parameters that can be filtered by are occupation, county, employment type, date, pre requirements, years of experience and seniority. The 7 parameters might differ depending on the job board.

            Uses Jobtech's API to web scrape data from Platsbanken.

            Swedish talent observatory was an external project made by a student group at KTH for the company Future place leadership.

            which displays the number of applicable job ads in accordance to occupation and county in Sweden. Through a graphical display the statistic can be refined and filtered by different requirements/parameters.

          </p>
        </div>
      </div>

      <Footer />
    </>
  )
}