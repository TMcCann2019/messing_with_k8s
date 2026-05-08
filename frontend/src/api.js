const API_URL = import.meta.env.VITE_API_URL;

export async function fetchProducts() {
  const res = await fetch(`${API_URL}/products`);
  return res.json();
}