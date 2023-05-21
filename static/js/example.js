/**
* Carregar ao iniciar a página.
*/
$(document).ready(function() {
    loadExamplesAjax();
});

/**
* Carrega os objetos através de uma request GET para a REST API.
*/
function loadExamplesAjax() {
    $.ajax({
        type: 'GET',
        url: `/api/example/`,
        data: {
        },
        success: function(data) {
            loadExamplesHtml(data);
        }
    });
};

/**
* Cria um objeto através de uma request POST para a REST API.
* OBS: CSRF_TOKEN gerada no arquivo fetch-csrf.js, carregado em base.html. 
*/
function saveTextAjax() {
    const TEXT = document.getElementById('example-text').value;
    $.ajax({
        type: 'POST',
        url: `/api/example/`,
        data: {
            csrfmiddlewaretoken: CSRF_TOKEN,
            "text": TEXT,
        },
        success: function(data) {
            fillHtml(data);
        }
    });
};

/**
* Insere um array de objetos no HTML.
*/
function loadExamplesHtml(data) {
    for (let i=0; i<data.length; i++) {
        fillHtml(data[i]);
    };
};

/**
* Insere um objeto no HTML.
*/
function fillHtml(object) {
    let text = `<div class="d-block">${object['id']} - ${object['text']}</div>`;
    document.getElementById('examples').innerHTML += text;
};