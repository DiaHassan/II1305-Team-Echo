import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from 'react';
import "../style.css";

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    function handleScroll() {
      const scrollPosition = window.scrollY;
      if (scrollPosition > 0 && !isScrolled) {
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

  return (
    <>
      <nav className={`navbar ${isScrolled ? 'small' : ''}`}>
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