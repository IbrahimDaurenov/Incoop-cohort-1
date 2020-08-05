Static Files, Media Files, Django Forms, JavaScript


- Static Files in Django


Create new folders in each of your app:

```
  my_app/static/my_app/
```

Using static Files
```
my_file.html

{% load static %}

<img src= " {% static 'my_app/pic.jpg' %} ">

```


- Media files setup

```
settings.py

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```


Adding ImageField to model

```
models.py


image = models.ImageField(upload_to='gallery/', null=True, blank=True, default = None)
```

Handling media:

```
my_file.html


<img src = "{{my_object.image.url}}">
```


- Django Forms:

Create forms.py file (for each app where needed):

```
forms.py

from django import forms

class NewForm(forms.Form):
  login = forms.CharField(label='Your login', max_length=50)
  password = forms.CharField(label='Your password', max_length=50, widget=forms.PasswordInput)
  def clean(self):
        cleaned_data = super(NewForm, self).clean()
        login = cleaned_data.get("login")
        password = cleaned_data.get("password")

        error_context = dict()


        try:
          users_login = Account.objects.get(login=login)
          is_valid = False
          error_context['login'] = 'Login had been taken'
        except Exception:
          is_valid = True

        if not is_valid:
          raise forms.ValidationError(error_context)

        return cleaned_data
```

Add handler in views files

```
views.py

if request.method == 'POST':
  form = NewForm(request.POST, request.FILES)
  if form.is_valid():
    login = form.cleaned_data['login']
    password = form.cleaned_data['password']
    user = MyUser(login = login, password = password)
    user.save()
    return render (request, 'my_file.html', context)
  else:
    return render(request, 'registration.html', {'form':form})
else:
  form = NewForm()
  return render(request, 'registration.html', {'form':form})

```


- JavaScript

linking html and js files

```
my_file.html

<body>
.....
<script src="scripts/main.js"></script>
</body>
```


JavaScript Variables

```
var a;
a = 10;

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');
var myElement = document.getElementById("demo");


```


if statements

```
var a = 10;
if (a === 10) {
  alert('a is 10');
} else {
  alert('a is not 10');
}
```

functions/methods/arguments

```
.onclick = function(){}
.innerHTML
.textContent




```




Changing elements on button click


```
my_file.html


<h1 id = "changeMe">Hello!</h1>

<button onclick = "foo()">Change heading</button>

```

```
js file


function foo(){
  a = document.getElementById("changeMe").innerHTML;


  if (a=="Hi"){
    document.getElementById("changeMe").innerHTML = "Bye";
  }
  else{
    document.getElementById("changeMe").innerHTML = "Hi";
  }

}

```


Styling elements


```
function hide(){
  document.getElementById("ninja").style.display = "block"; #show element
  document.getElementById("ninja").style.display = "none"; #hide element
  document.getElementById("ninja").style.color = "blue"; #coloring
}
```
