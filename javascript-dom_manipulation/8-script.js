document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      const helloElement = document.querySelector('#hello');
      helloElement.textContent = data.hello;
    })
    .catch(() => {
      
    });
});
