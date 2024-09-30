document.addEventListener('DOMContentLoaded', function() {
    var data_list = [
        {"name": "郭志", "salary": 100000, 'role': "CEO"},
        {"name": "卢辉", "salary": 100000, 'role': "CEO"},
        {"name": "赵建先", "salary": 100000, 'role': "CEO"}
    ];

    var tbody = document.getElementById('infoTable').getElementsByTagName('tbody')[0];

    data_list.forEach(function(item) {
        var row = document.createElement('tr');

        for (var key in item) {
            var cell = document.createElement('td');
            var text = document.createTextNode(item[key]);
            cell.appendChild(text);
            row.appendChild(cell);
        }

        tbody.appendChild(row);
    });
});