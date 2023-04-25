import React from "react";
import {Link} from "react-router-dom";
import "../style.css";


export default function Footer() {
    return(
      <>
      <footer>
        <div>
          <h2>Subscribe to our news letter</h2>
          <input type="text" placeholder="Enter Email" />
          <button type="submit">Search</button>
        </div>
        <div className="div-row">
          <div className="div-col">
            <h3>Navigation</h3>
            <ul>
              <li><Link to="/" className="">Home</Link></li>
              <li><Link to="/" className="">APP_NEEDS_NAME</Link></li>
              <li><Link to="/about" className="">About</Link></li>
            </ul>
          </div>
          <div className="div-col">
            <h3>Contact us:</h3>
            <a href="tel:+1234567890">+1 (234) 567-890</a>
            <a href="mailto:info@example.com">info@example.com</a>
          </div>
        </div>
      </footer>
      </>
    )
}