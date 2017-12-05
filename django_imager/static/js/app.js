(function () {'use strict';}());

var colors = ['#910DFF', '#246F00', '#E80CB5', '#FF680D', '#B0171F', '#FF0099', '#F3F315', '#83F52C', '#FF6600', '#6E0DD0', '#9DC6D8', '#00B3CA', '#E38690']
var darkColors = ['#002B36', '#073642', '#586E75', '#657B83', '#839496', '#93A1A1', '#EEE8D5', '#FDF6E3']
var randomColor1 = colors[Math.floor(Math.random() * colors.length)]
var randomColor2 = colors[Math.floor(Math.random() * colors.length)]
var randomDarkColor = darkColors[Math.floor(Math.random() * darkColors.length)]
$(document).ready(function(){
    $('.jumbotron').css('background-color', randomColor1);
    $('body').css('background-color', randomColor2);
});
