$(document).on('submit', '#search_city_weather', function (e) {
  e.preventDefault();
  $.ajax({
    url: "/",
    type: "POST",
    data: {
      the_post: $('#post-text').val(),
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },

    success: function (json) {
      $('#post-text').val('');
      var j = JSON.parse(json)[0];
      console.log(j);
      console.log(j.id);
      $('.card').html("<div id='json_content'>" + j.id + " " + j.main + " " + j
          .description + " " + j.icon +
        "</div>");
    },
  });
});

$(document).on('submit', '#save_city_weather', function (e) {
  e.preventDefault();
  $.ajax({
    url: "/",
    type: "POST",
    data: {
      the_post: $('#json_content').data("value"),
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    success: function (json) {
      $('#post-text').val('');
      console.log(json);
      console.log("success");
      var _json = json;
      $('.card').html("<div class='' id='json_content' data-value='1'>" + json + "</div>");
    },
  });
});

$(function () {
  $('#fetch_city_weather').on('click', function (e) {
    e.preventDefault();
    $.ajax({
      url: "/",
      type: "GET",
      data: {
        fetch_city_weather: "weather"
      },
      success: function (json) {
        $('#post-text').val('');
        console.log(json);
        console.log("success");
        $('.card').html("<div>" + json + "</div>");
      },
    });
  });
});

