import React from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import "../style.css";




export default function About() {
  return (
    <>
      <Navbar />

      <div className="about-wrapper">
        <div className="svensk-om">
          <h1>Om Swedish Talent Monitor</h1>
          <hr/>
          <p>
            Swedish Talent Observatory är ett statistiskt hjälpmedel för den svenska arbetsmarknaden baserad på insamlad data från olika arbetsplattformar. Statistiken ger en överblick över antal jobbannonser i relation till yrke och län i Sverige och har sin utgångspunkt i fyra olika plattformar.
            Datan hämtas från från Linkedin, Indeed, Platsbanken och Lediga jobb. Jobtech's API används för att extrahera datan från Platsbanken. Datan kan filtreras och kategoriseras utifrån två urval med flera olika kravspecifikationer. De tillgängliga kravspecifikationerna är yrkestitel, län, anställningstyp, 
            förkunskapskrav, års av erfarenhet och senioritet. Beroende på plattform kan urvalet variera utifrån tillgänglig data. 

            {/*Swedish talent observatory is a statistical tool based on webscraping data from different job boards. The data is extracted to represent the number of applicable job ads in accordance to occupation and county in Sweden from three different job boards. 
            Webscraping data from LinkedIn, Lediga jobb and Platsbanken, the information can be filtered by 7 parameters to find statistics of requirement-needs in job-ads for a specific occupation/profession. The 7 parameters that can be filtered by are occupation, county, employment type, date,
            pre requirements, years of experience and seniority. The 7 parameters might differ depending on the job board.
            Uses Jobtech's API to web scrape data from Platsbanken.
            Swedish talent observatory was an external project made by a student group at KTH for the company Future place leadership.
  which displays the number of applicable job ads in accordance to occupation and county in Sweden. Through a graphical display the statistic can be refined and filtered by different requirements/parameters.*/}
          </p>

          
        </div>
      </div>

      <Footer />
    </>
  )
}