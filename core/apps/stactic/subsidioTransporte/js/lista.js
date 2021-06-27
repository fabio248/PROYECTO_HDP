$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action':'buscardatos'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "cantidad_subsidio"},
            {"data": "cantidad_buses"},
            {"data": "cantidad_microbuses"},
            {"data": "fecuencia_uso"},
            {"data": "pertenece"},
        ],
        columnDefs: [
            {
                targets: [2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return data;
                }
            },
        ],
        initComplete: function (settings, json) {
            alert('tabla cargada')
        }
    });


})