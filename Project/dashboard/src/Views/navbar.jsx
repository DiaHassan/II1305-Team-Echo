import React from "react";
import {Link} from "react-router-dom";
import "../style.css";

export default function Navbar() {
    return(
      <>
        <nav>
            <div>
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
          </div>
        </nav>
      </>
    )
}