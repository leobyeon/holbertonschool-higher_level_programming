// fetches and prints how to say “Hello” depending of the language
let lang = $('html').attr('lang');
let url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
$.get(url, function (data) { $('#hello').text(data.hello); });
