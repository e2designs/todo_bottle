$def with (form, text, userid)
 
<!doctype html>
 
<html>
 
    <head>
        <title>Hello</title>
        <link rel="stylesheet" type="text/css" href="/static/tutorial.css" />
         
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>     
        <script> 
            jquery(document).ready(function() {
                $("#author").change(function() {
                    .ajax({
                        type: "POST",
                        async: false,
                        data: {author : author},
                        success: function(data) {
                            jquery('#foo').html(data).hide().fadeIn(1500);
                        },
                    });
                    return false;
                });
            });
         
        </script>
    </head>
     
    <body>
        <br>
        <p> Current user $userid</p>
        <form class="form" method="post"> 
        $:form.render()
        <input class="button" type="submit" value="Filter by Author"/>    
        </form>
 
        <br><br>
        <span id="foo">$text</span>        
    </body>
     
</html>
