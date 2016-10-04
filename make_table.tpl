%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td><a href="/edit/{{row[0]}}">{{col}}</a></td>
  %end
  </tr>
%end
</table>
<form action="/new" method="GET"> 
    <input type="submit" name='new_task' value='new_task'>
</form>
