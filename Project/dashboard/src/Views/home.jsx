import React from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import "../style.css";



export default function Home() {
  return (
    <>
      <div className="wrapper-wrapper">
        <div className="wrapper">
          <Navbar />
          <div className="home-body">
            <div>
              <h1>How does the job market look in Sweden?</h1>
              <p>Swedish talent observatory gives you a graphical visualization of the statistics within your profession. Find out how many applicable jobs there are within your county and profession.</p>
            </div>
            <img src="https://i.imgur.com/Q55Nhtn.png" alt="home_img" width="300" height="300" />
          </div>
          <div className="home-body">
            <div className="search">
              <input type="text" placeholder="Search..." />
              <button type="submit">Search</button>
            </div>
          </div>
        </div>
        <Footer />
      </div>
    </>
  )
}