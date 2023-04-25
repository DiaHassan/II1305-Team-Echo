import React from "react";
import {Link} from "react-router-dom";

export default function Navbar() {
    return(
      <>
        <nav className="navbar">
          <div className="navbar-div">
              <ul className="nav-ul">
                <li className="nav-li">
                  <Link to="/" className="nav-links">Progress</Link>
                </li>
                <li className="nav-li">
                  <Link to="/about" className="nav-links">About</Link>
                </li>
                <li className="nav-li">
                  <Link to="/contact" className="nav-links">Contact</Link>
                </li>
                {/* <li className="nav-li">
                  <Link   to="/" className="navbar-logo">HELOOOOO</Link>
                </li> */}
              </ul>
          </div>
        </nav>
      </>
    )
}