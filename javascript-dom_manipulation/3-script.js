document.addEventListener('DOMContentLoaded', () => {
    const toggleHeader = document.querySelector('#toggle_header');
    toggleHeader.addEventListener('click', () => {
      const header = document.querySelector('header');
      if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
      } else if (header.classList.contains('green')) {
        header.classList.remove('green');
        header.classList.add('red');
      }
    });
  });