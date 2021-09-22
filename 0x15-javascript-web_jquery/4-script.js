const toggleHeader = $('DIV#toggle_header');
const header = $('header');

toggleHeader.on('click', function (event) {
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
