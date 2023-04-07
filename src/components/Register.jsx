import { FormEvent, useState } from "react";
// import React, { useState} from "react";
import { TextField } from "@mui/material";
import { Button } from "@mui/material";
// import shop from "./shopping.svg";

function Register() {
  const [info, setInfo] = useState({
    name: "",
    username: "",
    age: "",
    postalcode: "",
    password: "",
  });

  const inputEvent = (event) => {
    const name = event.target.name;
    const value = event.target.value;

    setInfo((prev) => {
      event.preventDefault();
      return { ...prev, [name]: value };
    });
  };

  const onSubmits = (event) => {
    event.preventDefault();
  };

  return (
    <div className="p-10">
      <div className="container">
        <div className="left">
          <label className="Projecttitle">Sign up</label>
          {/* <img src={shop} className="shop" alt="shoplogo" /> */}
        </div>
        <div className="right">
          <form onSubmit={onSubmits}>
            <div>
              {/* NAME */}
              <label className="Name">Name: </label>
              <br />
              <TextField
                className="inputbox"
                onChange={inputEvent}
                id="Name"
                name="name"
                variant="outlined"
                autoComplete="off"
              />
            </div>

            <br />

            <div>
              {/* USERNAME */}
              <label className="Name">Username: </label>
              <TextField
                className="inputbox mt-11"
                onChange={inputEvent}
                id="Name"
                name="username"
                variant="outlined"
                autoComplete="off"
              />
            </div>

            <div className="container1">
              <div className="right1">
                {/* Age */}
                <label className="Name">Age: </label>
                <br />

                <TextField
                  className="inputbox1"
                  value={info.regno}
                  onChange={inputEvent}
                  id="age"
                  name="age"
                  variant="outlined"
                  autoComplete="off"
                />
              </div>

              <div className="left1">
                {/* Postal code */}
                <label className="Name">Postal code: </label>
                <br />

                <TextField
                  className="inputbox1"
                  value={info.regno}
                  onChange={inputEvent}
                  id="postalcode"
                  name="postalcode"
                  variant="outlined"
                  autoComplete="off"
                />
              </div>
            </div>
            <br />

            <div>
              {/* Password */}
              <label className="Name">Password: </label>
              <TextField
                className="inputbox"
                input-type="number"
                onChange={inputEvent}
                id="password"
                name="password"
                variant="outlined"
                autoComplete="off"
              />
            </div>

            <div className="container2radio">
              <div className="radio">
                <label>
                  <input type="checkbox" value="option1" />
                  Do you want to be club member?
                </label>
              </div>
              <div className="radio">
                <label>
                  <input type="checkbox" value="option2" />
                  Would you like to recive fashion updates?
                </label>
              </div>
            </div>

            <br />
            <br />
            <div className="inputbox">
              {/* Button */}
              <Button
                className="Confirmbtn self-center"
                type="submit"
                variant="contained"
              >
                CONFIRM
              </Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Register;