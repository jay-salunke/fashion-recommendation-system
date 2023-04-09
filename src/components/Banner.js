import { Carousel } from "react-bootstrap";
import banner01 from "../assets/banner01.jpg"
import banner02 from "../assets/banner02.jpg"
import '../CSS/banner.css'

function CustomCarousel ()  {
  return (
    <Carousel fade className="banner-card">
      <Carousel.Item >
        <img
          className="d-block w-100 h-25"
          src={banner01}
          alt="Random First slide"
        />

        <Carousel.Caption>
          <h1>SUMMER COLLECTION</h1>
          <h3>30% OFF</h3>
          <button className="form-banner-btn">BUY NOW</button>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100 h-25"
          // src="https://source.unsplash.com/mens/fashion/1000x410"
          src={banner02}
          alt="Random First slide"
        />

        <Carousel.Caption>
          <h1>MENS COLLECTION</h1>
          <h3>LIMITED EDITION</h3>

          <button className="form-banner-btn">Buy Now</button>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
};

export default CustomCarousel;
