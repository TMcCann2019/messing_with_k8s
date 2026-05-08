import { useEffect, useState } from "react";
import { fetchProducts } from "./api";

export default function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts().then(setProducts);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Products</h1>

      {products.map(p => (
        <div key={p.id} style={{ marginBottom: 20 }}>
          <h3>{p.name}</h3>
          <p>${p.price}</p>
          <img src={p.image} width="150" />
        </div>
      ))}
    </div>
  );
}