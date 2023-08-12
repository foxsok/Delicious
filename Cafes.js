// Obtén una referencia al contenedor de menú
const menuContainer = document.getElementById('data');

// Realiza una solicitud GET a la API
fetch('http://127.0.0.1:8000/Cafes')
  .then(response => response.json())
  .then(data => {
    // Itera a través de los datos y crea elementos para cada uno
    data.forEach(item => {
      const menuItem = document.createElement('div');
      menuItem.classList.add('col-lg-6', 'menu-item');
      menuItem.innerHTML = `
        <div class="menu-content">
          <span class="menu-item-name">${item.Nombre}</span><span class="menu-item-des">${item.Descripción}</span><span>${item.Precio}</span>
        </div>
      `;
      menuContainer.appendChild(menuItem);
    });
  })
  .catch(error => console.error('Error:', error));
