import React from "react";
import { Link } from "react-router-dom";
import "../style.css";


export default function Footer() {
  return (
    <>
      <footer>
        <div>
          {/* Placeholder */}
          <h2>Subscribe to our news letter</h2>
          <div className="search">
            <input type="text" placeholder="Enter Email" />
            <button type="submit">Subscribe</button>
          </div>
        </div>
        <div className="vertical-line" />
        <div>
          <h3>Navigation</h3>
          <ul>
            <li><Link to="/" className="">Home</Link></li>
            <li><Link to="/statistics" className="">Statistics</Link></li>
            <li><Link to="/about" className="">About</Link></li>
          </ul>
        </div>
        <div className="footer-contact">
          <h3>Contact</h3>
          <a href="mailto:team.echo.kth@gmail.com">team.echo.kth@gmail.com</a>
        </div>
      </footer>
    </>
  )
}