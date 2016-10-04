$def with (form, text)
 
<!doctype html>
 
<html>
 
    <head>
        <title>Hello</title>
        <link rel="stylesheet" type="text/css" href="/static/tutorial.css" />
         
        <script type="text/javascript" src="/static/jquery.js"></script>
         
        <script type="text/javascript">
                                jQuery(document).ready(function() {
                                jQuery(".button").click(function() {
                                        var input_string = $$("input#textfield").val();
                                        jQuery.ajax({
                                                type: "POST",
                                                data: {textfield : input_string},
                                                success: function(data) {
                                                jQuery('#foo').html(data).hide().fadeIn(1500);
                                                },
                                                });
                                        return false;
                                        });
                                });
         
                        </script>
    </head>
     
    <body>
        <br>
        <form class="form" method="post"> 
        $:form.render()
        <input class="button" type="submit" value="send"/>    
        </form>
 
        <br><br>
        <span id="foo">$text</span>        
    </body>
     
</html>
