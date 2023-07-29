import React from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import "../style.css";




export default function About() {
  return (
    <>
      <div className="wrapper">
        <div className="about-nav-wrapper">
        <Navbar />
        <div className="about-wrapper">
          <div className="svensk-om">
            <h1>Om Swedish Talent Monitor</h1>
            <hr/>
            <p>Swedish Talent Monitor är ett statistiskt hjälpmedel för den svenska arbetsmarknaden baserad på insamlad data från olika arbetsplattformar. Statistiken ger en överblick över antal jobbannonser i relation till yrke och län i Sverige och har sin utgångspunkt i fyra olika plattformar.</p>
            <p>Datan hämtas från Linkedin, Platsbanken och Ledigajobb. Jobtech's API används för att extrahera datan från Platsbanken.</p>
            <p>Datan kan filtreras och kategoriseras antingen utifrån flera yrken inom ett län eller ett specifikt yrke inom alla län med flera olika kravspecifikationer. De tillgängliga kravspecifikationerna är yrkestitel, län, anställningsform, utbildning, krav på antal års erfarenhet samt senioritet. Beroende på plattform kan urvalet variera utifrån tillgänglig data.</p>
          </div>
        </div>
      </div>
      </div>
        

        <Footer />
    </>
  )
}