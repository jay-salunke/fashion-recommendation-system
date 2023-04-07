import React from "react";
import Banner1 from "./../images/Banner1.jpg";
import Banner2 from "./../images/Banner2.jpg";
import Banner3 from "./../images/Banner3.jpg";

function Banner() {
  return (
    <div>
      <div
        id="carouselExampleControls"
        className="carousel slide"
        data-ride="carousel"
      >
        <div className="carousel-inner" >
          <div className="carousel-item active" data-interval="3000">
            <img className="d-block w-100" src={Banner1} alt="First slide" />
          </div>
          <div className="carousel-item" data-interval="3000">
            <img className="d-block w-100" src={Banner2} alt="Second slide" />
          </div>
          <div className="carousel-item" data-interval="3000">
            <img className="d-block w-100" src={Banner3} alt="Third slide" />
          </div>
        </div>
        <a
          className="carousel-control-prev"
          href="#carouselExampleControls"
          role="button"
          data-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="sr-only"></span>
        </a>
        <a
          className="carousel-control-next"
          href="#carouselExampleControls"
          role="button"
          data-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="sr-only"></span>
        </a>
      </div>
    </div>
  );
}

export default Banner;
