var $messages = $(".messages-content");
var serverResponse = "wala";

var suggession;
//speech reco
try {
  var SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;
  var recognition = new SpeechRecognition();
} catch (e) {
  console.error(e);
  $(".no-browser-support").show();
}

$("#start-record-btn").on("click", function (e) {
  recognition.start();
});

recognition.onresult = (event) => {
  const speechToText = event.results[0][0].transcript;
  document.getElementById("MSG").value = speechToText;
  //console.log(speechToText)
  insertMessage();
};

function listendom(no) {
  console.log(no);
  //console.log(document.getElementById(no))
  document.getElementById("MSG").value = no.innerHTML;
  insertMessage();
}

$(window).load(function () {
  $messages.mCustomScrollbar();
  setTimeout(function () {
    serverMessage(
      "Welcome to GMU"
    );
  }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar("scrollTo", "bottom", {
    scrollInertia: 10,
    timeout: 0,
  });
}

function insertMessage() {
  msg = $(".message-input").val();
  if ($.trim(msg) == "") {
    return false;
  }
  $('<div class="message message-personal">' + msg + "</div>")
    .appendTo($(".mCSB_container"))
    .addClass("new");
  fetchmsg()

  $(".message-input").val(null);
  updateScrollbar();
}

document.getElementById("mymsg").onsubmit = (e) => {
  e.preventDefault();
  insertMessage();
  // This below server message displays response from server to interface
  //  serverMessage();
  // speechSynthesis.speak(new SpeechSynthesisUtterance("hello"));
};

function extractLink(text) {
  const urlRegex = /(https?:\/\/[^\s]+)/g;
  const urlMatches = text.match(urlRegex);
  if (urlMatches && urlMatches.length > 0) {
    const url = urlMatches[0];
    const buttonText = text.split("|")[0].trim();
    const link = `<a href="${url}" target="_blank" class="link-button">${buttonText}</a>`;
    return link;
  }
  return text;
}

function serverMessage(response2) {
  if ($(".message-input").val() != "") {
    return false;
  }
  let responseText = extractLink(response2);
  $(
    '<div class="message loading new"><figure class="avatar"><img src="css/BOTLOGO.jpg" /></figure><div class="response-box"></div></div>'
  ).appendTo($(".mCSB_container"));
  updateScrollbar();

  setTimeout(function () {
    $(".message.loading").remove();

    $(
      '<div class="message new"><figure class="avatar"><img src="css/BOTLOGO.jpg" /></figure><div class="response-box">' +
        responseText +
        "</div></div>"
    )
      .appendTo($(".mCSB_container"))
      .addClass("new");
    updateScrollbar();
  }, 100 + Math.random() * 20 * 100);
}


function fetchmsg() {
  var url = "http://localhost:5000/send-msg";

  const data = new URLSearchParams();
  for (const pair of new FormData(document.getElementById("mymsg"))) {
    data.append(pair[0], pair[1]);
    console.log(pair);
  }

  console.log("abc", data);

  fetch(url, {
    method: "POST",
    body: data,
  })
    .then((res) => res.json())
    .then((response) => {
      console.log(response);
      serverMessage(response.Reply);
      speechSynthesis.speak(new SpeechSynthesisUtterance(response.Reply));
    })
    .catch((error) => console.error("Error h:", error));
}
