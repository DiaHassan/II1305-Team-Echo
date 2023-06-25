import React, {useState} from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import Tabletest from "../Presenters/Tabletest";
import Toberem from "../Presenters/ToBeRem";

export default function Stats() {
  const [instruktionerVisible, setInstruktionerVisible] = useState(true);
  const [tolkningVisible, setTolkningVisible] = useState(true);

  function toggleInstruktioner() {
    setInstruktionerVisible(!instruktionerVisible);
  }

  function toggleTolkning() {
    setTolkningVisible(!tolkningVisible);
  }

  return(
    <>
      <Navbar/>
      <div class="instruktioner">
        <h2>
          Instruktioner
          <button class="closeInstruktioner" onClick={toggleInstruktioner}>
            {instruktionerVisible ? "Stäng" : "Öppna"}
          </button>
        </h2>
        {instruktionerVisible && (
          <ul>
            <p>1. Välj en eller flera plattformar att analysera data från.</p>
            <p>2. Välj mellan att analysera flera olika yrken i ett län, eller analysera ett yrke i flera län.</p>
            <p>3. Välj län.</p>
            <p>4. Välj yrke.</p>
            <p>5. Välj månad från ett år under datum.</p>
            <p>6. Om filtrerad data önskas, öppna filter och välj ett.</p>
          </ul>
        )}
      </div>
      <div className="">
        {/* <Toberem /> */}
        <Tabletest/>
      </div>
      <div class="tolkning">
        <h2>
          Hur man tolkar grafen
          <button class="closeTolkning" onClick={toggleTolkning}>
            {tolkningVisible ? "Stäng" : "Öppna"}
          </button>
        </h2>
        {tolkningVisible && (<ul>
          <li>På x-axeln är antingen flera yrken över ett län, eller flera län med ett yrke.</li>
          <li>På y-axeln är antalet för vald kategori, vilket kan vara filtrerat om man valt det.</li>
        </ul>
        )}
      </div>
      <Footer/>
    </>
  )
}