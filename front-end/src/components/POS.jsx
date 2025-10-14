import React, { useEffect, useState } from "react";

export default function POS() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/products")
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch(() => alert("Cannot fetch products"));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Point of Sale</h2>
      <table border="1" width="100%">
        <thead>
          <tr>
            <th>SKU</th>
            <th>Name</th>
            <th>Price</th>
            <th>Stock</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.id}>
              <td>{p.sku}</td>
              <td>{p.name}</td>
              <td>{p.price}</td>
              <td>{p.stock}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
