$(function(){
  console.log("called");
  var score = 0;
  var data = [];

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

  var wrapped = function(html){
    html += "<button>men</button>";
    html += "<button>women</button>";
    html += "<button>okama</button>";
    return html;
  };



  var renderPic = function(){
    var str = "";
    var $el = $("#pictures");

    for(var i = 0 ;  i < 5;i++){
      var dir = picDir();
      var correctType = dir.split('\/')[2];

      str += "<li><img class='pic' src='";
      str += dir;
      str += "'></li>";
      str += "<div class='buttons'>";
      if (correctType === "men"){
        str += "<button class='correct' >men</button>";
        data.push(0);
      }else{
        str += "<button class=''>men</button>";
      }
      if (correctType === "women"){
        str += "<button class='correct' >women</button>";
        data.push(1);
      }else{
        str += "<button class=''>women</button>";
      }
      if (correctType === "okama"){
        str += "<button class='correct'>okama</button>";
        data.push(2);
      }else{
        str += "<button>okama</button>";
      }
      str += "</div>";

    }

    $el.html(str);
  };


  renderPic();
  console.log(data);

  var renderScore = function(){
    var $res = $("#res");
    $res.html("score: " + score);
  };

  $("button").bind("click",function(e){
    var target = $(this).attr("class");


    $closest = $(this).closest(".buttons");
    $correct = $(".correct");
    $closest.html($correct.html());

    if (target === "correct"){
      score += 1;
      renderScore();
    }else{
      renderScore();
    }
    $(this).attr("clicked",true);

  });




});
