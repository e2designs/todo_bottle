%#template for editing a task
%#the template expects to receive a value for "idnum" as well a "old", the text of the selected ToDo item
<p>Edit the task with ID = {{idnum}}</p>
<form action="/edit/{{idnum}}" method="get">
  <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
  <select name="status">
    <option>open</option>
    <option>closed</option>
  </select>
  <br>
  <input type="submit" name="save" value="save">
</form>
