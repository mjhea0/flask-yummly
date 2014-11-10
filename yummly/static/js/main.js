$(function() {
    console.log("dom is ready!");

    $(".retry").hide()
    $("#links").hide()


    $('#post-form').on('submit', function(event){
   //      event.PreventDefault;
           console.log("yay!")
           $("#errors").hide()
           $("#results").hide()
           value = $('input[name="ingredient"]').val();
           console.log(value)
         $.ajax({
            type: "POST",
            url: "/",
            data : { ingredient_list : value },
            success: function(result) {
               $(".boom").hide()
               $(".retry").show()
               $("#links").show()
               $("#errors").hide()
               $("#results").show()
               $("#results").html('<h3><a href="http://www.yummly.com/recipe/'+result.recipe_id+'" id="recipe_title">'+
                   result.recipe_name+'</a></h3><p>Recipe Rating: '+result.recipe_rating+' out of 5</p><a href="http://www.yummly.com/recipe/'+result.recipe_id+
                   '"><img src='+result.recipe_pic+' alt="Recipe photo" style="border-radius:50%;"></a><br><br>');
            },
            error: function(error) {
                console.log(error);
                $("#errors").show()
                $("#errors").html(error.responseJSON.sorry)
            }
        });
    });
    $('.new-link').on('click', function(event){
        event.preventDefault();
        $("input").val('').show();
        $(".boom").show()
        $(".retry").hide()
        $("#links").hide()
        $('#results').html('');
    });
    $("#save").on('click', function(){
      var recipe_url = $("#recipe_title").attr('href');
      var recipe_title = $("#recipe_title").text();
      console.log(recipe_title);
      console.log(recipe_url);

      $.ajax({
            type: "POST",
            url: "/api/v1/recipes",
            data : { 'recipe_title' : recipe_title,
                      'recipe_url' : recipe_url
                   },
            });
    });
});
