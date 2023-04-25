import React from "react";
import {Link} from "react-router-dom";

export default function Footer() {
    return(
      <>
        <footer>
      <div>
        <h3>Navigation</h3>
        <ul>
          <li><Link to="/" className="">Home</Link></li>
          <li><Link to="/" className="">APP_NEEDS_NAME</Link></li>
          <li><Link to="/about" className="">About</Link></li>
        </ul>
      </div>
      <div>
        <span>Contact Us:</span>
        <a href="tel:+1234567890">+1 (234) 567-890</a>
        <a href="mailto:info@example.com">info@example.com</a>
      </div>
    </footer>
      </>
    )
}