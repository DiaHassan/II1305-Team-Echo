import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../style.css";

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    function handleScroll() {
      const scrollPosition = window.scrollY;
      if (scrollPosition > 50 && !isScrolled) {
        setIsScrolled(true);
      } else if (scrollPosition === 0 && isScrolled) {
        setIsScrolled(false);
      }
    }

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, [isScrolled]);

  function displayList() {
    setIsVisible(isVisible ? false : true);
  }

  return (
    <>
      <nav className={`navbar ${isScrolled ? 'small' : ''}`}>
        <div className="navTitle">
          <Link to="/">Swedish Talent Observatory</Link>
        </div>
        <img src={"Project/dashboard/src/menuHamburger.png"} alt="<" className="burger" onClick={displayList}/>
        <ul className={`${isVisible ? '' : 'navHidden'}`}>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li >
            <Link to="/statistics">Statistics</Link>
          </li>
          <li  >
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>
    </>
  )
}