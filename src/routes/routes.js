import { createBrowserRouter } from "react-router-dom";
import Login from "../components/login";
import UserInfo from "../components/userInfo";
import Home from "../components/Home";
import NotFound from "../components/NotFound";
import Cart from "../components/cart";
import Transactions from "../components/transactions";
import Register from "../components/Register";

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
