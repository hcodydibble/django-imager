(function () {'use strict';}());

var colors = ['#910DFF', '#246F00', '#E80CB5', '#FF680D']
var randomColor1 = colors[Math.floor(Math.random() * colors.length)]
var randomColor2 = colors[Math.floor(Math.random() * colors.length)]
var randomColor3 = colors[Math.floor(Math.random() * colors.length)]
$(document).ready(function(){
    $('.jumbotron').css('background-color', randomColor1);
    $('body').css('background-color', randomColor2);
});
