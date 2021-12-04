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
  window.location.href = cog_uri + "http://localhost:8080/callback.html"
}

function save_user_data() {
  const queryString = window.location.search;
  console.log(queryString);
}

function view_event(id) {
  window.location.href = "/event.html?event_id=" + id
}