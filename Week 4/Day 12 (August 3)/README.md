Django (Advanced Features)

Url naming:

```
urls.py


from . import views
urlpatterns = [
  path("url",views.index, name = "some_name"),
]

```

```
{% url 'some_name' %}

{% url 'some_name' argument %}

```

Template Inheritance

```
base.html

SOME HTML CODE
<title>
  {% block title %}
  {% endblock %}
</title>


{% block body %}
{% endblock %}
```


```
some_file.html

{% extends "templates/base.html" %}

{% block title%}
  Some Title
{% endblock %}


{% block body %}
 Some HTML Code
{% endblock %}
```


Database relationships

```
models.py

class Sets:
  #.......
  foods = models.ManyToManyField (Food, blank = True)

```

```
views.py

a = Sets(...)

a.foods.add( Food(...) )

```


Accesing database

```
.filter()
.get()
.all()

```


Handling Forms as POST requests
```
my_form.html

<form action="URL">

  {% csrf_token %}
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>


  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label><br>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label><br>
  <input type="radio" id="other" name="gender" value="other">
  <label for="other">Other</label>


  <select name = "dropdown">
    <option value = "1">Some option</option>
    <option value = "2">Some other option</option>
  </select>


  <input type="submit" value = "Send">

</form>

```

```
views.py

  if request.method == "post":
    #SOME CODE

```




HW 7 /Project 2 (Deadline: August 8)

```
  Build a Web application that connects businesses with customers. It is your choice of which businesses you may want to choose, but the main criteria is to give businesses a chance to add (AND CUSTOMIZE!!!) their products (or services) using your platform, and customers to buy/order some products/services. At every moment businesses must be able to see all their products (and, of course, customize them), add new products/services, delete products/services, view orders from users. On the other hand, must be able to check all available options on market, buy/order some of them and view history of all previous orders.

  Some of the examples to get inspiration from: Wolt/Glovo, Uber/Yandex.Taxi, Chocolife, Krisha. But you can create any other B2C connection website.
```
