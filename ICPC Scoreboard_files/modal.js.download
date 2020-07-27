// Modal Show
// By: Hamid Zarrabi-Zadeh, Hamed Moghimi
// November 2014

var teamNumStart = 1001;
var imageFormat = "jpg";

$(document).ready(function() {
  var fadeTime = 500;

  var guard = $("#guard");
  var modal = $("#modal");
  var img = modal.children("img");

  $("#scoreboard")
    .find("td.team")
    .click(function() {
      var num = $(this).attr("data");
      img.attr("src", "photos/" + (num - teamNumStart + 1) + "." + imageFormat);
      guard.fadeIn(fadeTime);
      modal.fadeIn(fadeTime);
    });

  guard.click(function() {
    modal.fadeOut(fadeTime);
    guard.fadeOut(fadeTime);
  });

  $(document).keypress(function(e) {
    modal.fadeOut(fadeTime);
    guard.fadeOut(fadeTime);
  });
});
