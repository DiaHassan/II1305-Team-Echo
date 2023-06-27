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
        
        <div>
          <a href="https://futureplaceleadership.com/" class="footer-logo">
            <img src="https://cdn.discordapp.com/attachments/713525156160602214/1120408714176888832/logo_salmon.png" alt="logo" class="logo"/>
          </a>
          <div className="footer-contact">
            <h3>Kontakt</h3>
            <p><b>Adress:</b></p>
            <p>Norrsken House</p>
            <p>Birger Jarlsgatan 57 C, 113 56 Stockholm, Sweden</p>
              <p> </p>
            <p>
              <b>Tel:</b>
              <a href="tel:+46 70-867 36 34"> +46 70-867 36 34</a>
            </p>
            <p>
              <b>E-mail:</b>
              <a href="mailto:sk@futureplaceleadership.com"> sk@futureplaceleadership.com</a>
            </p>   
          </div>
        </div>
      </footer>
    </>
  )
}