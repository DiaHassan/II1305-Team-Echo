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
              <h1>How does the job market look in Sweden?</h1>
              <p>Swedish talent observatory gives you a graphical visualization of the statistics within your profession. Find out how many applicable jobs there are within your county and profession.</p>
            </div>
            <a href="https://commons.wikimedia.org/wiki/File:Sverigekarta-Landskap.svg#/media/File:Sverigekarta-Landskap.svg">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Sverigekarta-Landskap.svg/1200px-Sverigekarta-Landskap.svg.png" alt="home_img" width="250" height="580" />
            </a>
          </div>
        </div>
        <div className="home-content">

          <h1>Title</h1>
          <p>Some text here?</p>
          <div className="search">
            <input type="text" placeholder="Search..." />
            <button type="submit">Search</button>
          </div>
        </div>
        <Footer />
      </div>

    </>
  )
}