import React from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import "../style.css";




export default function Home() {

  return (
    <>
      <div className="wrapper">
        <div className="front-wrap">
          <Navbar />
          <div className="home-front">
            <div>
              <h1>Hur ser arbetsmarknaden ut i Sverige?</h1>
              <p>Swedish talent monitor ger dig med hjälp utav en visuell graf en statistisk överblick över efterfrågan på Sveriges arbetsmarknad.
                Ta reda på hur många möjliga jobb som finns inom ditt yrke och län!
              </p>
            </div>
            <a href="https://commons.wikimedia.org/wiki/File:Sverigekarta-Landskap.svg#/media/File:Sverigekarta-Landskap.svg">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Sverigekarta-Landskap.svg/1200px-Sverigekarta-Landskap.svg.png" alt="home_img" width="250" height="580" />
            </a>
          </div>
        </div>
        <Footer />
      </div>

    </>
  )
}