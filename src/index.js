import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import router from "./routes/routes";
import Home from "./components/Home";
import './CSS/footer.css';
import './CSS/banner.css';
import './CSS/register.css'
import Register from "./components/Register";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    {/* <RouterProvider router={router} /> */}
    <Home/>
    {/* <Register/> */}
  </React.StrictMode>
);
