//var a;
//a = 10;
//a = "Hello!"
//a = ["hello",1,2,3,"world!"]

//var myButton = document.querySelector('button');
//var myHeading = document.querySelector('h1');
//var myElement = document.getElementById("demo");

/*
var a = 10;
if (a === 10) {
  alert('a is 10');
}
else {
  alert('a is not 10');
}
*/



function hello(){
  alert('Hello world!')
}



/*
var myElement = document.getElementById("mood");
myElement.innerHTML = "Changed!";
*/

function changeMood(){
  var myElement = document.getElementById("mood");

  if (myElement.innerHTML === "Hello, I am in a good mood!"){
    document.getElementById("mood").innerHTML = "Hello, I am in a bad mood!";
  }
  else{
    document.getElementById("mood").innerHTML = "Hello, I am in a good mood!";
  }
}

function hide(){
  var myElement = document.getElementById("ninja");
  if (myElement.style.display == "block"){
    document.getElementById("ninja").style.display = "none";
    document.getElementById("mood").style.color = "blue";
  }
  else{
    document.getElementById("ninja").style.display = "block";
  }


}
