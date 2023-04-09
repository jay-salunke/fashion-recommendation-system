import React, { useState, useEffect } from "react";
import axios from "axios";

const Transactions = () => {
  const [responseData, setResponseData] = useState([]);

  useEffect(() => {
    const response = async () => {
      let data = JSON.stringify({
        email: "101@gmail.com",
      });

      let config = {
        method: "post",
        maxBodyLength: Infinity,
        url: "http://127.0.0.1:8000/users/transactions/",
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
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
                  <p>Transaction ID: {transaction.transaction_id}</p>
                  <p>Transaction Date: {transaction.transaction_date}</p>
                  <p>Item Name: {transaction.item_name}</p>
                  <p>Item ID: {transaction.item_id}</p>
                  <p>Item Price: {transaction.item_price}</p>
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
