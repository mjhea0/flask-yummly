$(function() {
    console.log("dom is ready!");

    $(".retry").hide()
    $(".new-link").hide()


    $('#post-form').on('submit', function(event){
   //      event.PreventDefault;
           console.log("yay!")
           value = $('input[name="ingredient"]').val();
           console.log(value)
   //      $('#top').hide()
         $.ajax({
             type: "POST",
             url: "/",
             data : { ingredient_list : value },
             success: function(recipe) {
                console.log(recipe);
                $(".boom").hide()
                $(".retry").show()
                $(".new-link").show()
                // $("#results").html(recipe.recipe_id)
                $("#results").html('<h3><a href="http://www.yummly.com/recipe/'+recipe.recipe_id+'">'+
                    recipe.recipe_name+'</a></h3><br><a href="http://www.yummly.com/recipe/'+recipe.recipe_id+
                    '"><img src='+recipe.recipe_pic+' alt="Recipe photo" style="border-radius:50%;"></a><br><br>');
            },
            error: function(error) {
                console.log(error)
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