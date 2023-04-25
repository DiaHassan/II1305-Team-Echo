import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../style.css";

export default function Navbar() {
  const [navbar, setNavbar] = useState(false);

  // const changeBackground = () => {
  //   console.log(window.scrollY);
  //   console.log("Change")

  //   navbarSet(true)
  //   if (window.scrollY > 1) {
  //     console.log(window.scrollY);
  //     navbarSet(true);
  //   } else {
  //     navbarSet(false);
  //   };
  // };
  // useEffect(() => {
  //   changeBackground()
  //   console.log("Effect")
  // });
  
  const test = () => {
    console.log(window.scrollY);
  }

  window.addEventListener('scroll', test);


  return (
    <>
      <nav className={navbar ? "active" : ""}>
      {/* <nav className="active"> */}
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