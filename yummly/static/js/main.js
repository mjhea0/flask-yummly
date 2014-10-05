$(function() {
    console.log("dom is ready!");

    $(".retry").hide()
    $(".new-link").hide()


    $('#post-form').on('submit', function(event){
   //      event.PreventDefault;
           console.log("yay!")
           $("#errors").hide()
           $("#results").hide()
           value = $('input[name="ingredient"]').val();
           console.log(value)
   //      $('#top').hide()
         $.ajax({
            type: "POST",
            url: "/",
            data : { ingredient_list : value },
            success: function(result) {
               $(".boom").hide()
               $(".retry").show()
               $(".new-link").show()
               $("#results").show()
               $("#results").html('<h3><a href="http://www.yummly.com/recipe/'+result.recipe_id+'">'+
                   result.recipe_name+'</a></h3><p>Recipe Rating: '+result.recipe_rating+' out of 5</p><br>Ingredients you will need: <ul>'+result.recipe_ingredients+'</ul><a href="http://www.yummly.com/recipe/'+result.recipe_id+
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
        $(".new-link").hide()
        $('#results').html('');
    });
});
