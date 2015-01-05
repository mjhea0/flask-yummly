$(function() {

    console.log("dom is ready!");

    $(".retry").hide()
    $("#links").hide()
    $(".save").hide()

    getRecipes();

    $(document).on('click', "#delete", function(event){
        console.log("delete");
        var elementID = $(this).attr("name");
        console.log(elementID);
        deleteRecipe(elementID);
    });

    function getRecipes() {
        $.ajax({
            type: "GET",
            url: "/api/v1/recipes",
            dataType: 'json',
            success: function(result) {
                $.each(result, function(idx, obj) {
                    $.each(obj, function(idx, obj) {
                        // console.log(obj.title, obj.url, obj.recipe_id, obj.recipe_pic, obj.ingredients);
                        $("#recipe_list").append('<tr id='+obj.recipe_id+
                            '><td><img src='+obj.recipe_pic+
                            ' alt="Recipe photo" style="border-radius:50%;"></a></td><td><a href='+obj.url+'>'+obj.title+
                            '  </a></td><td><a class="btn btn-default btn-sm" role="button" id="list" href=/recipe/'+obj.recipe_id+
                            '>List of Ingredients</a></td><td><button type="button" id="delete" class="btn btn-default btn-sm" name="'+
                            obj.recipe_id+'" >Delete</button></td><td id="recipe_ingredients" class="hidden">'+
                            obj.ingredients+'</td></tr>');
                    });
                });
            },
            error: function() {
                console.log("no recipes");
                $("#none").html("<p>You haven't saved any recipes yet.</p>")
            }
        });
    }

    function deleteRecipe(id) {
        console.log("delete function");
        $.ajax({
            type: "POST",
            url: "/api/v1/recipes/"+id,
            success: function(result) {
                console.log(result);
                $('#'+id+'').fadeOut(300);
            },
            error: function(error) {
                console.log(error);
                location.reload();
            },
        });
    }

    $('#post-form').on('submit', function(event){
        console.log("yay!")
        $("#errors").hide()
        $("#results").hide()
        value = $('input[name="ingredient"]').val();
        $(".save").empty();
        $(".save").css('background-color','#fff');
        $(".save").append('Save Recipe');
        $.ajax({
            type: "POST",
            url: "/",
            data : { ingredient_list : value },
            success: function(result) {
                console.log(result);
                $(".boom").hide()
                $(".retry").show()
                $(".save").show()
                $("#links").show()
                $("#errors").hide()
                $("#results").show()
                $("#results").html('<h3><a href="http://www.yummly.com/recipe/'+result.recipe_id+
                    '" id="recipe_title" class='+result.recipe_id+'>'+result.recipe_name+'</a></h3><p>Rating: '+result.recipe_rating+
                    ' out of 5</p><a href="http://www.yummly.com/recipe/'+result.recipe_id+'"><img src='+
                    result.recipe_pic+' alt="Recipe photo" style="border-radius:50%;"></a><p class="hidden">'+
                    result.recipe_ingredients+'</p><br><br>');
            },
            error: function(error) {
                console.log(error);
                $("#errors").show()
                $("#errors").html(error.responseJSON.sorry)
            }
        });
    });

    $('#sms').on('submit', function(event){
        console.log("SMS sending");
        var phone_number = $('input[name="list"]').val();
        if (isNaN(phone_number) || phone_number.length != 10) {
         console.log("not a number");
         alert("Please enter a valid ten-digit phone number.")
        }
        else {
            id = $('button').attr('id');
            $.ajax({
                type: "POST",
                url: "/recipe/"+id+"/sms",
                data : { 'phone_number' : phone_number },
                success: function(result) {
                    console.log(phone_number);
                    console.log(result);
                    alert("Message sent! Check your phone.");
                }
            })
        }    
    });

    $('.new-link').on('click', function(event){
        event.preventDefault();
        $("input").val('').show();
        $(".boom").show()
        $(".retry").hide()
        $("#links").hide()
        $(".save").hide()
        $('#results').html('');
    });

    $('.save').on('click', function(){
        var recipe_url = $("#recipe_title").attr('href');
        var recipe_title = $("#recipe_title").text();
        var recipe_pic = document.getElementsByTagName('img')[0].currentSrc;
        var recipe_ingredients = $(".hidden").text();
        var yummly_id = $("#recipe_title").attr('class');
        console.log(yummly_id);
        $(".save").empty();
        $(this).css('background-color','#5bc0de');
        $(".save").append('Recipe saved!');

        $.ajax({
            type: "POST",
            url: "/api/v1/recipes",
            data : { 'recipe_title' : recipe_title,
                      'recipe_url' : recipe_url,
                      'recipe_pic' : recipe_pic,
                      'recipe_ingredients' : recipe_ingredients,
                      'yummly_id' : yummly_id
                   },
            success: function(result) {
              console.log(result);
            }
            error: function (error) {
              console.log(error);
            }
        });
    });

});
