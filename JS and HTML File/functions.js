function getCustomer_by_id(id) {

    var xhReq = new XMLHttpRequest();
    xhReq.open("GET", "http://127.0.0.1:8000/customer/" + id, false);
    xhReq.send(null);
    if (xhReq.status == 200) {

        // 1.  fetch JSON and map it json object
        var jsonObject = JSON.parse(xhReq.responseText);
        console.log(jsonObject);

        // 2. go through all addresses and concat the mapped address to one HTML String
        var addressHtml = "";
        for (let i = 0; i < jsonObject["addresses"].length; ++i) {
            addressHtml += `<h5>Addresse Nr. ${i + 1} </h5>` + map_address(jsonObject["addresses"][i]) + " <hr></br>";
        }

        // 3. Prepare table
        var htmltable = `
        <thead class="thead-dark">
                <tr>
                  <th scope="col">Anrede</th>
                  <th scope="col">Vorname</th>
                  <th scope="col">Nachname</th>
                  <th scope="col">Adressen</th>
                </tr>
              </thead>
        `;
        // 4. create customer overview table with all prepared data
        var table_body = `<tbody>
        <td>${jsonObject["salutation"]}</td>
        <td>${jsonObject["firstname"]}</td>
        <td>${jsonObject["lastname"]}</td>
        <td>${addressHtml}</td>
        </tbody>`

        document.getElementById("resulttable").innerHTML = htmltable + table_body;

    } else {
        document.getElementById("resulttable").innerHTML = "";
        document.getElementById("warningarea").innerText = "Der Kunde mit der ID " + id + " wurde nicht gefunden";
        document.getElementById("warningarea").hidden = false;
    }


}

function map_address(jsonaddress) {
    return `<b>Anrede</b>:${jsonaddress["salutation"]} </br>` +
        `<b>Vorname</b>:${jsonaddress["first_name"]} </br>` +
        `<b>Nachname</b>:${jsonaddress["last_name"]} </br>` +
        `<b>StraÃŸe</b>:${jsonaddress["street"]} </br>` +
        `<b>Hausnummer</b>:${jsonaddress["house_number"]} </br>` +
        `<b>PLZ</b>:${jsonaddress["zip"]} </br>` +
        `<b>Stadt</b>:${jsonaddress["city"]} </br>` +
        `<b>Liefergebiet</b>:${jsonaddress["delivery_zone"]} </br>`
}