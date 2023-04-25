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
              <h1>Some title goes here</h1>
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
            </div>
            <img src="https://i.imgur.com/Q55Nhtn.png" alt="home_img" width="300" height="300" />
          </div>
          <div  className="home-body">
            <input type="text" placeholder="Search..." />
            <button type="submit">Search</button>
          </div>
        </div>
          <Footer />
      </div>
    </>
  )
}