fetch('http://127.0.0.1:8000/api-auth/get_animal_list/')
    .then(resp => resp.json())
    .then((data) => {
        let animal = document.querySelector('.filter__wrap')
        for (let animal of data) {
            let aAnimal = document.createElement('a')
            aAnimal.classList.add('filter__item')
            aAnimal.setAttribute('href', `http://127.0.0.1:8000/catalog/${animal.id}`)
            aAnimal.innerHTML = `
            <div class="filter__item-img" style="background-image: url(${animal.image});">
                            </div>
                            <h3 class="filter__item-text">${animal.name}</h3>
            `
            document.querySelector('.filter__wrap').append(aAnimal)
        }
    })


const searchInput = document.getElementById('search')
searchInput.addEventListener('input', getSearchResult)
const searchResult = document.querySelector('search_result')



function getSearchResult() {
    if (searchInput.value.length > 2) {
        console.log(searchInput.value)
        fetch(`http://127.0.0.1:8000/api-auth/get_product_list/?search=${searchInput.value}`)
            .then(resp => resp.json())
            .then((data) => {
                searchResult.style.display = 'block'
                searchResult.innerHTML = ''
                for (let item of data) {
                    searchResult.innerHTML += `
                    <a href="http://127.0.0.1:8000/product_description/${item.id}" class="search__drop-down-item">
                    <div class="search__drop-down-item-img">
                    <img src="${item.image_preview}">
                    </div>
                    <p search__drop-down-item-title>${item.name}</p>
                    </a>
                    `
                }
            })
    } else {
        searchResult.style.display = 'none'
        searchResult.innerHTML = ''
    }
}