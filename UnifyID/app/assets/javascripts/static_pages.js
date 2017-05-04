// Scrolling activity. Smooth scroll from navigation.
function scrollTo(element) {
    $('html, body').animate({
        scrollTop: $("#" + element).offset().top
    }, 1500);
  }

//Poll the https://www.random.org server for size random numbers
$(document).on("click", "#gen_image", function() {
  console.log("Success!");
});
