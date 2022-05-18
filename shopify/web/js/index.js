function getAPIURL() {
    var url = window.location.protocol + '//' + window.location.host + '/api/inventory/';
    console.log('Window URL is ', url)
    return url;
}

function displayData(rowData) {
    tableRef = document.getElementById("list_all_table");
    rowData.forEach(function (item, index) {
        const tr = document.createElement('tr');
        tr.innerHTML = "<td>" + item['code'] + "</td><td>" + item['name'] + "</td><td>" + item['type'] + "</td><td>" + item['supplier'] + "</td><td>" + item['quantity'] + "</td><td>" + item['price'] + "</td>";
        tableRef.appendChild(tr);
    });
}

function loadTableData() {
    var url = getAPIURL() + 'list';
    console.log('Formulated URL is ', url);
    fetch(url).then(function (response) {return response.json();}).then(function (json) { console.log('Success!', json); displayData(json.data);}).catch(function (err) {
        console.warn('Something went wrong. Rest call failed', err);
    });
}

function showAlertMessage() {
    containerRef = document.getElementById("display_alert_container");
    msgRef = document.getElementById("display_alert_message");
    if (window.location.href.includes("status=")){
        if (window.location.href.includes("ERROR")){
            containerRef.style.display = 'block';
            msgRef.innerHTML = 'Operation failed! Invalid';
        }
        if (window.location.href.includes("SUCCESS")){
            containerRef.style.display = 'block';
            msgRef.innerHTML = 'Operation successful!';
        }
    }
}

loadTableData();
showAlertMessage();



