// import Image from "./Image";
// import img1 from "../assets/f1.jpeg";
// import img2 from "../assets/f2.jpeg";
// import img3 from "../assets/f3.jpeg";
import React from "react";
// import PriceCounter from "./PriceCounter";

const Cart = () => {
  return (
    <>
      <div class="container mt-3">
        <div class="row">
          <div class="col-md-8">
            <div class="card bg-light mb-3">
              <div class="card-body">
                <h5 class="card-title">Left Card Title</h5>
                <p class="card-text">This is the content for the left card.</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card bg-light mb-3">
              <div class="card-body">
                <h5 class="card-title">Right Card Title</h5>
                <p class="card-text">This is the content for the right card.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Cart;
