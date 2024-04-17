const animal_form = document.querySelector("#animal_add")
const animal_button = document.querySelector("#animal_add_button")
animal_button.addEventListener("click", send_animal)

function send_animal() {
    let data_form = new FormData(animal_form)
    fetch(`http://127.0.0.1:8000/api-auth/animal_add/`, {
        method: "POST", headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        }, body: data_form,

    })
        .then((resp) => resp.json())
        .then((data) => {
            console.log(data)
        })
}

function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}