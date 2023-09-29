var linkGlobal;
function get_resolution() {
  const inp = document.getElementById("inp");
  const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  linkGlobal = inp.value;
  const link = inp.value;
  console.log(link);
  const data = {
    link: link,
  };
  console.log(data);
  const response = fetch("/get_resolution/", {
    method: "POST",
    headers: { "X-CSRFToken": csrf },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
        let optionsDiv = document.getElementById("options");
        optionsDiv.innerHTML = "";
        let tempString = ``;
        data.forEach((element) => {
            tempString += `<button class="btn btn-primary option" onclick="download('${element}')">${element}</button>`;
        });
        optionsDiv.innerHTML = tempString;
    });
}


function download(resolution) {
    const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    console.log(linkGlobal)
    const data = {
        link: linkGlobal,
        resolution: resolution,
    };
    console.log(data);
    const response = fetch("/download/", {
        method: "POST",
        headers: { "X-CSRFToken": csrf },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if (data.status == "success") {
                window.location.href = data.url;
            }
        });
}
