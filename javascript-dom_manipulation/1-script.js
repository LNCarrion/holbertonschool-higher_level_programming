document.addEventListener('DOMContentLoaded', () => {
  const readHeader = document.querySelector('#red_header');
  readHeader.addEventListener('click', () => {
    document.querySelector('header').style.color = '#ff0000';
  });
});
