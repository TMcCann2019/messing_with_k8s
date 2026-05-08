const API_URL = "http://localhost:8000";

async function loadUsers() {
    const response = await fetch(`${API_URL}/users`);
    const users = await response.json();

    const list = document.getElementById("users");
    list.innerHTML = "";

    users.forEach(user => {
        const item = document.createElement("li");
        item.innerText = `${user.name} (${user.email})`;
        list.appendChild(item);
    });
}