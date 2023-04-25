import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from 'react';
import "../style.css";

export default function Navbar() {


  // const [isScrolled, setIsScrolled] = useState(false);

  // useEffect(() => {
  //   window.addEventListener('scroll', handleScroll);
  //   return () => {
  //     window.removeEventListener('scroll', handleScroll);
  //   };
  // }, [isScrolled]);

  // // return (
  // //   <nav className={`navbar ${isScrolled ? 'small' : ''}`}>
  // //     {/* Navbar content */}
  // //   </nav>
  // // );

  // const handleScroll = (e) => {

  // }

  
  // const stickyNav = () => {
  //   const [navbar, navbarSet] = useState(false)

  //   const changeBackground = () => {
  //     console.log(window.scrollY)
  //     if(window.scrollY > 20) {
  //       navbarSet(true)
  //     } else {
  //       navbarSet(false)
  //     }
  //   }
  //   useEffect(() => {
  //     changeBackground()
  //     // adding the event when scroll change background
  //     window.addEventListener("scroll", changeBackground)
  //   })

  //   {navbar ? "navbar active" : "navbar"}
  // }

  return (
    <>
      <nav /*</>className={`navbar ${isScrolled ? 'small' : ''}`}*/>
        <div>Swedish Talent Observatory</div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li >
            <Link to="/">APP_NEEDS_NAME</Link>
          </li>
          <li  >
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>
    </>
  )
}