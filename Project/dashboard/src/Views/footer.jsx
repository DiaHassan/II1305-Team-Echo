import React from "react";
import { Link } from "react-router-dom";
import "../style.css";


export default function Footer() {
  return (
    <>
      <footer>
        <div>
          {/* Placeholder */}
          <h2>Prenumerera på nyhetsbrevet</h2>
          <div className="search">
            <input type="text" placeholder="Ange e-postaddress ..." />
            <button type="Skicka">Prenumerera</button>
          </div>
        </div>
        <div className="vertical-line" />
        <div>
          <h3>Navigation</h3>
          <ul>
            <li><Link to="/" className="">Hem</Link></li>
            <li><Link to="/statistics" className="">Statistik</Link></li>
            <li><Link to="/about" className="">Om</Link></li>
          </ul>
        </div>
        <div className="footer-contact">
          <h3>Kontakt</h3>
          <a href="mailto:team.echo.kth@gmail.com">team.echo.kth@gmail.com</a>
        </div>
      </footer>
    </>
  )
}