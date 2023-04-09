import { createBrowserRouter } from "react-router-dom";
import Login from "../components/Login";
import Register from "../components/Register";
import Home from "../components/Home";
import NotFound from "../components/NotFound";

const router = createBrowserRouter([
  {
    path: "/home",
    element: <Home />,
   
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/userinfo",
    element: <UserInfo />,
  },
  {
    path: "*",
    element: <NotFound />,
  },
  {
    path: "/cart",
    element: <Cart />,
  },
  {
    path: "/transactions",
    element: <Transactions />,
  },
  {
    path: "/register",
    element: <Register />,
  },
]);

export default router;
