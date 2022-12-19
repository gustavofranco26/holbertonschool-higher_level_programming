$.getJSON('https://stefanbohacek.com/hellosalut/?lang=fry', function (data) {
  const hello = data.hello;
  $('DIV#hello').text(hello);
});
