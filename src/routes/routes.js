import { createBrowserRouter } from "react-router-dom";
import Login from "../components/Login";
import Register from "../components/Register";
import Home from "../components/Home";
import NotFound from "../components/NotFound";
// import ProductSlider from "../components/ProductSlider"

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
   
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/Register",
    element: <Register />,
  },
  {
    path: "*",
    element: <NotFound />,
  },
]);

export default router;
