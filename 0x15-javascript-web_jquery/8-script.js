$(function () {
  const listMovies = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (idx, result) {
        listMovies.append('<li>' + result.title + '</li>');
      });
    }
  });
});
