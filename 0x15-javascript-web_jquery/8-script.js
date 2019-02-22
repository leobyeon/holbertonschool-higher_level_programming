// fetches and replaces the name of the url
let url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  for (let i = 0; i < data.results.length; i++) {
    $('#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
