import React from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import Tabletest from "../Presenters/Tabletest";
import Toberem from "../Presenters/ToBeRem";

export default function Stats() {
    return(
      <>
        <Navbar/>
        <div className="fortable">
          {/* <Toberem /> */}
          <Tabletest/>
        </div>
        <Footer/>
      </>
    )
}