import React from "react";
import { Link } from "react-router-dom";
// import API_URL from "../Constants/Api";
import axios from "axios";
import "./../CSS/login.css";

const Login = () => {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");

  const onFormSubmit = async (e) => {
    e.preventDefault();
    const { Buffer } = require("buffer");
    const credentials = Buffer.from(`${email}:${password}`).toString("base64");
    console.log(`c: ${credentials}`);

    const headers = {
      "Content-Type": "application/json",
      Authorization: `Basic ${credentials}`,
      "Access-Control-Allow-Origin": "*",
    };
    const method = "POST";
    try {
      let response = await axios({
        withCredentials: true,
        method,
        // url: API_URL,
        headers,
      });
      console.log(response.headers["host"]); // The response data from the API
    } catch (error) {
      console.log(error.message); // The error message if the API call fails
    }
  };

  return (
    <div className="body-class">
      <div className="container">
        <div className="row">
          <div className="col-md-6 col-sm-3 col-lg-6 mx-auto">
            <form action=" " onSubmit={onFormSubmit}>
              <div className="card">
                <div className="card-body">
                  {/*Member login */}
                  <div className="row">
                    <div className="col">
                      {/* <center>
                          <h1> Login </h1>
                        </center> */}
                    </div>
                  </div>
                  <br />
                  <br />
                  <div className="row">
                    <div className="col">
                      {/*Email Id InputText */}
                      <div className="mt-3">
                        {/* <label className="Name" htmlFor="email"> */}
                        {/* Email ID */}
                        {/* </label> */}
                        <div className="form-group">
                          <input
                            className="form-control"
                            type="text"
                            id="email"
                            placeHolder="Enter the Email ID"
                            autoComplete="off"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                          />
                        </div>
                      </div>
                      {/*Password InpuText*/}
                      <div className="mt-3">
                        <label className="Name" htmlFor="password">
                          {/* Password */}
                        </label>
                        <div className="form-group">
                          <input
                            className="form-control"
                            type="text"
                            id="password"
                            placeHolder="Enter the Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                          />
                        </div>
                      </div>
                      <br />
                      <br />
                      <div className="mt-2 text-center">
                        Don't have an account yet ?
                        <Link
                          to="/register"
                          className="text-decoration-none text-black-50 mx-2"
                        >
                          Sign up
                        </Link>
                      </div>

                      <div className="mt-3">
                        <div className="form-group">
                          <center>
                            <button className="form-btn btn btn-success text-center">
                              Login
                            </button>
                          </center>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
