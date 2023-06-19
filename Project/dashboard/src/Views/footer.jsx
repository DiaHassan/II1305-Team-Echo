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
          <h3>Sidor</h3>
          <ul>
            <li><Link to="/" className="">Hem</Link></li>
            <li><Link to="/statistics" className="">Statistik</Link></li>
            <li><Link to="/about" className="">Om</Link></li>
          </ul>
        </div>
        <div class="footer-column">
          <a href="https://futureplaceleadership.com/" class="footer-logo">
            <img src="https://cdn.discordapp.com/attachments/713525156160602214/1120408714176888832/logo_salmon.png" alt="logo" class="logo"/>
          </a>
          <div className="footer-contact">
            <h3>Kontakt</h3>
            <a href="mailto:sk@futureplaceleadership.com">sk@futureplaceleadership.com</a>
          </div>
        </div>
      </footer>
    </>
  )
}