function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function makeShowUp(dom_element, data) {
    let div = document.createElement("div")
    div.style.display="none"
    let table = document.createElement("table")
    table.className = "table"
    let tr = document.createElement("tr")
    let td1 = document.createElement("td")
    td1.innerHTML = data.employee_id
    let td2 = document.createElement("td")
    td2.innerHTML = data.full_name
    let td3 = document.createElement("td")
    td3.innerHTML = data.position
    let td4 = document.createElement("td")
    td4.innerHTML = data.Employment_date
    let td5 = document.createElement("td")
    td5.innerHTML = data.email
    let tds = [td1, td2, td3, td4, td5]
    tds.forEach((td) => {
        tr.appendChild(td);
    })
    table.appendChild(tr)
    div.appendChild(table)
    dom_element.appendChild(div)
    dom_element.addEventListener("click", () => {
        if (div.style.display === "none") {
            div.style.display = "block"
        } else {
            div.style.display = "none"
        }
    })

}


let bosses_spans = document.getElementsByClassName("boss")
for (let i = 0; i < bosses_spans.length; i++) {
    bosses_spans[i].addEventListener("click", () => {
        let div = document.getElementById(`employees_${bosses_spans[i].id}`)
        if (div.childNodes.length > 0) {
            if (div.style.display === "none") {
                div.style.display = "block"
            } else {
                div.style.display = "none"
            }
        } else {
            $.ajax({
                type: "POST",
                data: {
                    boss_id: bosses_spans[i].id,
                    csrfmiddlewaretoken: getCookie("csrftoken")
                },
                url: "get_worker",
                async: true,
                success: function (data) {
                    ul = document.createElement("ul")
                    ul.classList.add("list-group")
                    for (let j = 0; j < data.length; j++) {
                        let li = document.createElement("li")
                        li.innerHTML = `<span>${data[j].full_name} (${data[j].position})</span>`
                        li.classList.add("list-group-item")
                        li.classList.add("list-group-item-action")
                        makeShowUp(li, data[j])
                        ul.appendChild(li)

                    }
                    div.appendChild(ul)
                    div.style.display = "block"
                }
            })
        }
    })
}