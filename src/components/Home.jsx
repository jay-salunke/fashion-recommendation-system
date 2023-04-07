import React from "react";

import NavBar from "./NavBar";
import Banner from "./Banner";
import Carousel1 from "./Carousel";
import Footer from "./Footer";

function Home(){
    return <div className="home">
        
        <NavBar/>
        <Banner/>
        <Carousel1/>
        <Footer/>
        

    </div>
}

export default Home;