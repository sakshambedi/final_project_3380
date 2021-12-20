
document.getElementById("btn").addEventListener("click", request_all_players());


function request_all_players(){
  var resp = $.ajax({
    type: "POST",
    url: "/database.py",
    data: { param: input },
    success: callbackFunc
  });

  return resp.responseText;
}

