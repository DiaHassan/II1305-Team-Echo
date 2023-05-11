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
            Swedish Talent Monitor är ett statistiskt hjälpmedel för den svenska arbetsmarknaden baserad på insamlad data från olika arbetsplattformar. Statistiken ger en överblick över antal jobbannonser i relation till yrke och län i Sverige och har sin utgångspunkt i fyra olika plattformar.
            Datan hämtas från från Linkedin, Indeed, Platsbanken och Lediga jobb. Jobtech's API används för att extrahera datan från Platsbanken. Datan kan filtreras och kategoriseras utifrån två urval med flera olika kravspecifikationer. De tillgängliga kravspecifikationerna är yrkestitel, län, anställningstyp, 
            förkunskapskrav, års av erfarenhet och senioritet. Beroende på plattform kan urvalet variera utifrån tillgänglig data. 
          </p>

          
        </div>
      </div>

      <Footer />
    </>
  )
}