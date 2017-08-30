function btn_Approve(status) {
    var code = $('.field-code')[0].children[0].children[1].children[0].innerHTML;
    var objs = [];
    var trAry = $("table tr");
    for (var i = 1; i < trAry.length; i++) {
        var entity = {};
        entity.code = trAry[i].children[0].innerText.trim();
        entity.purchaseNumber = trAry[i].children[4].children[0].innerHTML;
        entity.warehouse = $('#id_storageordergoods_set-' + (i - 1) + '-warehouse').val();
        objs.push(entity);
    }
    $.post('/api/approve_storage_order/' + code + "/" + status, {
        data: JSON.stringify(objs)
    }, function (rs) {
        window.location.href = "/admin/goods_purchace/storageorder/";
    });
}
django.jQuery(document).ready(function () {
    $('.btn-high').hide();

    if ($('.field-orderstatus')[0].children[0].children[1].children[0].innerHTML == "待入库") {
        $('.submit-row').append("<button type='button'  class='btn' onclick='btn_Approve(1)'>入库</input>");
        $('.submit-row').append("<button class='btn btn-danger' onclick='btn_Approve(0)'>退回</button>");
    } else {
        $('.save-box').hide();
    }
})
