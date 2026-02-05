fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const films = data.results;
    const ulElement = document.getElementById('list_movies');

    films.forEach((film) => {
      const li = document.createElement('li');
      li.textContent = film.title;
      ulElement.appendChild(li);
    });
  })
  .catch(() => {
    
  });