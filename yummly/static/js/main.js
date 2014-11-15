$(function() {
    console.log("dom is ready!");

    $(".retry").hide()
    $("#links").hide()

    $.ajax({
        type: "GET",
        url: "/api/v1/recipes",
        dataType: 'json',
        success: function(result) {
          // console.log(result);
          $.each(result, function(idx, obj) {
              console.log(obj);
              $.each(obj, function(idx, obj) {
                console.log(obj.title, obj.url, obj.recipe_id);
                $("#recipe_list").append('<p id='+obj.recipe_id+'><a href='+obj.url+'>'+obj.title+'  </a><button type="button" id="delete" class="btn btn-default btn-sm" action="/recipe/'+obj.recipe_id+'/delete" method="post" >Delete</button></p>');
                $('#delete').on('click', function(event){
                  $.ajax({
                    type: "POST",
                    url: "/recipes",
                    data : { 'recipe_id' : recipe_id },
                    success: function(result) {
                    },
                  });
                });
              });
            });
          }
        });


    

    
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
              console.log(result);
               $(".boom").hide()
               $(".retry").show()
               $("#links").show()
               $("#errors").hide()
               $("#results").show()
               $("#results").html('<h3><a href="http://www.yummly.com/recipe/'+result.recipe_id+'" id="recipe_title">'+
                   result.recipe_name+'</a></h3><p>Rating: '+result.recipe_rating+' out of 5</p><a href="http://www.yummly.com/recipe/'+result.recipe_id+
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
            success: function(result) {
              console.log(result);
            }
        });
    });
});
