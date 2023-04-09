import React from "react";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import FavoriteIcon from "@mui/icons-material/Favorite";
import "../CSS/navbar.css";
function NavBar() {
  return (
    <div className="navv">
      <div className="logo">Logo</div>
      <ul className="navbar">
        <a href="/#">Women</a>
        <a href="/#">Men</a>
        <a href="/#">Kids</a>
      </ul>
      <div className="left-nav">
        <div className="icons">
          <a href="/#" className="flex-1">
            <ShoppingCartIcon style={{color:'black'} }/>
          </a>
        </div>

        <div className="icons">
          <a href="/#" className="flex-1">
            <FavoriteIcon style={{color:'black'} } />
          </a>
        </div>
      </div>
    </div>
  );
}

export default NavBar;
