document.addEventListener('DOMContentLoaded', function() {
    // Проверка данных
    if (!window.menuData) {
        console.error('Данные меню не были переданы из Django');
        showErrorMessage('Ошибка загрузки меню. Пожалуйста, обновите страницу.');
        return;
    }

    const menuContainer = document.getElementById('menu');
    if (!menuContainer) {
        console.error('Не найден контейнер меню');
        return;
    }

    // Создаем меню
    try {
        Object.entries(window.menuData).forEach(([sectionName, items]) => {
            const section = document.createElement('section');
            section.className = 'menu-section';

            // Заголовок секции
            const title = document.createElement('h2');
            title.textContent = sectionName;
            section.appendChild(title);

            // Элементы меню
            const itemsContainer = document.createElement('div');
            itemsContainer.className = 'items-container';

            items.forEach(item => {
                const itemElement = document.createElement('div');
                itemElement.className = 'menu-item';
                itemElement.innerHTML = `
                    <div>
                        ${item.name}
                        ${item.desc ? `<div class="item_desc">${item.desc}</div>` : ''}
                    </div>
                    <div class="price_volume">
                        ${item.price ? `<div class="price">${item.price}р.</div>` : ''}
                        ${item.volume ? `<div class="volume">${item.volume}</div>` : ''}
                    </div>
                `;

                itemElement.addEventListener('click', () => openModal(item));
                itemsContainer.appendChild(itemElement);
            });

            section.appendChild(itemsContainer);
            menuContainer.appendChild(section);
        });

        initModalFunctionality();
    } catch (error) {
        console.error('Ошибка создания меню:', error);
        showErrorMessage('Ошибка отображения меню');
    }

    function initModalFunctionality() {
        window.openModal = function(item) {
            const modal = document.getElementById('modal-overlay');
            if (!modal) return;

            document.getElementById('modal-title').textContent = item.name;
            document.getElementById('modal-desc').textContent = item.desc || '';

            const priceVolume = document.querySelector('.modal-price-volume');
            priceVolume.innerHTML = '';

            if (item.price) {
                const priceEl = document.createElement('div');
                priceEl.textContent = `${item.price}р.`;
                priceVolume.appendChild(priceEl);
            }

            if (item.volume) {
                const volumeEl = document.createElement('div');
                volumeEl.textContent = item.volume;
                priceVolume.appendChild(volumeEl);
            }

            const img = document.getElementById('modal-image');
            img.src = `/static/assets/items/${item.item_id}.png`;
            img.onerror = () => img.style.display = 'none';
            img.style.display = 'block';

            modal.classList.add('active');
            document.body.classList.add('modal-active');
        };
    }

    function showErrorMessage(message) {
        const errorDiv = document.createElement('div');
        errorDiv.style.color = 'red';
        errorDiv.style.padding = '20px';
        errorDiv.style.textAlign = 'center';
        errorDiv.innerHTML = `<p>${message}</p>`;
        menuContainer.appendChild(errorDiv);
    }
});