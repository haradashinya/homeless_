$(function(){
  console.log("called");

  // return type of man/women/okama





  var type = function(){
    var types = ["men","women","okama"];
    var rand = Math.floor(Math.random()  * 3);
    return types[rand];
  };


  // make picture's dir.
  var picDir = function(){

    var idx = Math.floor(Math.random()  * 5) + 1;
    var randType = type();
    var str = "";
    str += "static/img/" + randType +  "/" + randType +idx + ".png"; 
    return str;
    
  };

  var wrappedHtml = function(html){
    html += "<button>men</button>";
    html += "<button>women</button>";
    html += "<button>okama</button>";
    return html;
  };


  var renderPic = function(){
    var el = $("#pictures");

    for(var i = 0 ;  i < 5;i++){
      var html = "";
      var dir = picDir();
      html += "<li><img class='pic' src='";
      html += dir;
      html += "'></li>";
      $(html).addClass("pic");

      el.append(wrappedHtml(html));

    }
    
  };


  renderPic();



});
