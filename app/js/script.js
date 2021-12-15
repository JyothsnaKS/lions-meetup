function create_event_container(event_data) {
    // var newRow = document.createElement('div');
    // newRow.classList.add("row")
    // var newCol = document.createElement('div');
    // newCol.classList.add("col-lg-4", "col-md-12", "mb-4")
    // newRow.appendChild(newCol)
    // Need to find a better way for this
    var row = `
          <div class="col-lg-4 col-md-12 mb-4">
            <div class="card">
              <div id="`+ event_data["event_id"] +`" class="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
                <img src="`+ event_data["image_url"] +`" class="img-fluid" />
                <a href="#!">
                  <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
                </a>
              </div>
              <div class="card-body">
                <h5 class="card-title">`+ event_data["event_title"] +`</h5>
                <h6 class="card-subtitle mb-2 text-muted">Location: `+ event_data["event_location"] +`</h6>
                <a href="#!" class="btn btn-primary">Read</a>
              </div>
            </div>
          </div>
    `
    document.getElementById("lions-events").innerHTML += row
}

function login() {
  var cog_uri = "https://lionsmeetup.auth.us-east-1.amazoncognito.com/login?" + 
  "client_id=24ci6213vcpi0un21k2b51fh1d&response_type=token&scope=openid+phone+profile+email&redirect_uri="
  // console.log(cog_uri + redirect_uri)
  redirect_uri = location.protocol + '//' + location.host + "/callback.html"
  // console.log(redirect_uri)
  window.location.href = cog_uri + redirect_uri
}

function save_user_data() {
  const queryString = window.location.search;
  console.log(queryString);
}

function view_event(id) {
  // var doc_cookie = document.cookie;
  window.location.href = "/event.html?event_id=" + id // + "&user_id=" + 
}

function create_event() {
  var doc_cookie = document.cookie;
  if (!doc_cookie) {
    alert("Please Login!!"); // need to change , models etc.,
    window.location.href = "/index.html";
  } else {
    cookie_pair = doc_cookie.split("=");
    cookie_json = JSON.parse(cookie_pair[1]);
    user_id = cookie_json["user_data"]["email"]
    data = {
      "start_local": document.getElementById("start_time").value,
      "organizer_id": user_id,
      "name_text": document.getElementById("name").value,
      // "shareable": document.getElementById("sharable").value,
      "end_local": document.getElementById("end_time").value,
      "summary": document.getElementById("description").value,
      "category": document.getElementById("category").value,
      "online_event": document.getElementById("online_event").value
    }
    // console.log(data)
    fetch('https://1ptsftnwde.execute-api.us-east-1.amazonaws.com/test/create-events', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      window.location.href = "/event.html?event_id=" + data["body"]["item_id"]
      console.log(data);
    })
    .catch((error) => {
      // window.location.href = "/event_failure.html"
      console.log(error);
    });
  }
}

function update_profile(user_data) {
  json_data = {
    "email": user_data,
    "first_name": document.getElementById("first_name").value,
    "last_name": document.getElementById("last_name").value,
    "mobile": document.getElementById("mobile").value,
    "email": document.getElementById("email").value,
    "city": document.getElementById("city").value,
    "state": document.getElementById("state").value,
    "zipcode": document.getElementById("zipcode").value,
    "tags": $('#tags').val(),
    "gender": document.getElementById("gender").value,
  }
  console.log(json_data)
  fetch('https://1ptsftnwde.execute-api.us-east-1.amazonaws.com/test/create-users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(json_data),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    // window.location.href = "/profile.html?user_id=" + user_data
  })
  .catch((error) => {
    console.error('Error:', error);
    alert("Error Updating profile!! Please try again")
  });
}

function logout() {
  document.cookie = 'lions_data' + '=; expires=Thu, 01-Jan-70 00:00:01 GMT;';
  window.location.href = "/"
}

function join_event(event_id, user_id) {
  var doc_cookie = document.cookie;
  if (!doc_cookie) {
    alert("Please Login!!"); // need to change , models etc.,
    window.location.href = "/index.html";
  } else {
    new_event_id = event_id.split(".")[0]
    fetch("https://1ptsftnwde.execute-api.us-east-1.amazonaws.com/test/join-event?event_id=" + new_event_id + "&user_id=" + user_id, {
      method: 'GET'
    }).then(response => response.json())
    .then(data => {
      console.log(data)
      alert("Joined!!");
    });
  }
}