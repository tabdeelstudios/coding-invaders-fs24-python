import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Navbar from "./Navbar";

function InvoiceDetails() {
  const { id } = useParams();
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/invoices/${id}/items/`,
          {
            headers: { "Content-Type": "application/json" },
          }
        );
        if (!response.ok) {
          throw new Error("Server did not respond!");
        }
        const data = await response.json();
        console.log(data);
        setItems(data);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchItems();
  }, []);
  return (
    <div>
      <Navbar />
      <p>Invoice details here</p>
    </div>
  );
}

export default InvoiceDetails;
