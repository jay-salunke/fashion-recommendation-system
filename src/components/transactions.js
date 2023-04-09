import React, { useState, useEffect } from "react";
import axios from "axios";
import Image from "./Image";

const Transactions = () => {
  const [responseData, setResponseData] = useState([]);
  const min = 150;
  const max = 5000;

  useEffect(() => {
    const response = async () => {
      let data = JSON.stringify({
        email: "100@gmail.com",
      });

      let config = {
        method: "post",
        maxBodyLength: Infinity,
        url: "http://myproject.local:8000/users/transactions",
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
        withCredentials: true,
      };

      try {
        const response = await axios.request(config);
        setResponseData(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    response();
  }, []);

  return (
    <>
      <h3 className="font-weight-bold text-center mt-3 mb-3">
        Your Transactions History...
      </h3>
      <div className="container ">
        <div className="row">
          {responseData.map((transaction) => (
            <div key={transaction.transaction_id} className="col-sm-6 col-md-4">
              <div className="card mb-2">
                <div className="card-body">
                  <Image
                    src={`https://frsstoragepavnhe.file.core.windows.net/frs/images/0${transaction.item_id
                      .toString()
                      .substr(0, 2)}/0${
                      transaction.item_id
                    }.jpg?sv=2021-12-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-06-30T19:27:18Z&st=2023-04-09T11:27:18Z&spr=https&sig=wPAoF6tCS%2BoowdD8ztwOMKiE%2BpRU6vAxCKM3ZuerB1Y%3D`}
                    width={"370px"}
                    height={"300px"}
                  />

                  <p>Transaction ID: {transaction.transaction_id}</p>
                  <p>
                    Transaction Date:{" "}
                    {new Date(transaction.transaction_date).toString()}
                  </p>
                  <p>Item Name: {transaction.item_name}</p>
                  <p>Item ID: {transaction.item_id}</p>
                  <p>
                    Item Price:
                    {Math.floor(Math.random() * (max - min + 1)) + min}
                  </p>
                  <p>Item Description: {transaction.item_description}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Transactions;
