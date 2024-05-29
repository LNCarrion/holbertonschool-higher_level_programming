document.addEventListener('DOMContentLoaded', () => {
    const addItem = document.querySelector('#add_item');
    addItem.addEventListener('click', () => {
      const myList = document.querySelector('.my_list');
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      myList.appendChild(newItem);
    });
  });