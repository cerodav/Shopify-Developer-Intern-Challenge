function getAPIURL() {
    var url = window.location.protocol + '//' + window.location.host + '/api/inventory/';
    console.log('Window URL is ', url)
    return url;
}

function displayData(rowData) {
    tableRef = document.getElementById("list_all_table");
    rowData.forEach(function (item, index) {
        const tr = document.createElement('tr');
        tr.innerHTML = "<td>" + item['code'] + "</td><td>" + item['comment'] + "</td>";
        tableRef.appendChild(tr);
    });
}

function loadTableData() {
    var url = getAPIURL() + 'undeletelist';
    console.log('Formulated URL is ', url);
    fetch(url).then(function (response) {return response.json();}).then(function (json) { console.log('Success!', json); displayData(json.data);}).catch(function (err) {
        console.warn('Something went wrong. Rest call failed', err);
    });
}

loadTableData();



