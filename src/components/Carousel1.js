import React from "react";
import Carousel from "react-multi-carousel";
import "../CSS/carousel.css"
import person from "../assets/person.png";

function Carousel1() {
  const responsive = {
    superLargeDesktop: {
      // the naming can be any, depends on you.
      breakpoint: { max: 4000, min: 3000 },
      items: 5,
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 4,
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1,
    },
  };
  return (
      <>
      <h3>Recommeded for you</h3>
      <Carousel
       responsive={responsive}
       >
        
          <div className="carousel-card">
            <img className="product--image" src={person} alt="product" />
            <h2>Dress</h2>
            <p className="price">$6.3</p>
            <p>product description..</p>
            <p>
              <button>Add to cart</button>
            </p>
          </div>
        <div className="carousel-card">
          <img className="product--image" src={person} alt="product" />
          <h2>Dress</h2>
          <p className="price">$6.3</p>
          <p>product description..</p>
          <p>
            <button>Add to cart</button>
          </p>
        </div>
        <div className="carousel-card">
          <img className="product--image" src={person} alt="product" />
          <h2>Dress</h2>
          <p className="price">$6.3</p>
          <p>product description..</p>
          <p>
            <button>Add to cart</button>
          </p>
        </div>
        <div className="carousel-card">
          <img className="product--image" src={person} alt="product" />
          <h2>Dress</h2>
          <p className="price">$6.3</p>
          <p>product description..</p>
          <p>
            <button>Add to cart</button>
          </p>
        </div>
        <div className="carousel-card">
          <img className="product--image" src={person} alt="product" />
          <h2>Dress</h2>
          <p className="price">$6.3</p>
          <p>product description..</p>
          <p>
            <button>Add to cart</button>
          </p>
        </div>
        <div className="carousel-card">
          <img className="product--image" src={person} alt="product" />
          <h2>Dress</h2>
          <p className="price">$6.3</p>
          <p>product description..</p>
          <p>
            <button>Add to cart</button>
          </p>
        </div>
      </Carousel>
      </>
  );
}

export default Carousel1;
