import "./App.css";
import Navbar from "./components/Navbar";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";


function App() {
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchInvoices = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/invoices/", {
          headers: { "Content-Type": "application/json" },
        });
        if (!response.ok) {
          throw new Error("Server did not respond!");
        }
        const data = await response.json();
        console.log(data);
        setInvoices(data);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchInvoices();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error : {error.message}</div>;
  }
  return (
    <>
      <div>
        <Navbar />
      </div>

      <div>
        <table>
          <thead>
            <tr>
              <th>Title</th>
              <th>Client Name</th>
              <th>Total Amount</th>
              <th>Status</th>
              <th>Items</th>
            </tr>
          </thead>
          <tbody>
            {invoices.map((invoice) => (
              <tr>
                <td>{invoice.title}</td>
                <td>{invoice.clientName}</td>
                <td>{invoice.totalAmount}</td>
                <td>{invoice.status}</td>
                <td>
                  <Link to={`/${invoice.id}/items/`}>
                    <button>Items</button>
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default App;
