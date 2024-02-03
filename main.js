document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const xhr = new XMLHttpRequest();
    // URL do servidor back-end
    const url = "http://localhost:8000/login";

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          const data = JSON.parse(xhr.responseText);
          console.log("Token de autenticação:", data.token);
          alert("Login bem-sucedido!");

          window.location.href = "/pagina.html";
        } else {
          console.error("Erro:", xhr.statusText);
        }
      }
    };

    const formData = JSON.stringify({ username: username, password: password });
    xhr.send(formData);
  });
});
