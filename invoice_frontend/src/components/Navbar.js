import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <h3>Invoice App</h3>
        </li>
        <li>
          <Link to="/">
            <p>All Invoices</p>
          </Link>
        </li>
        <li>
          <Link to="/addInvoice">
            <p>Add Invoice</p>
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
