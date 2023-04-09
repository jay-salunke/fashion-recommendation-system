import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");

  const onFormSubmit = (e) => {
    e.preventDefault();

    const Login = async () => {
      const { Buffer } = require("buffer");
      const credentials = Buffer.from(`${email}:${password}`).toString(
        "base64"
      );
      var config = {
        method: "POST",
        headers: {
          "Authorization": `Basic ${credentials}`,
          "Content-Type": "application/json",
        },
        url: "http://myproject.local:8000/auth/login",
        withCredentials: true,
      };

      const response = await axios(config);
      console.log(response);
      if (
        response.data.status === "success" &&
        response.data.redirect === "True"
      ) {
        navigate("/userinfo", { replace: true });
      } else if (response.data.status === "success") {
        navigate("/home", { replace: true });
      } else {
        alert("Entered Credentials are invalid");
      }
    };

    Login();
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
                            placeholder="Enter the Email ID"
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
                            placeholder="Enter the Password"
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
