function btn_Approve(status) {
    var code = $('#id_code').val();
    $.get('/api/approve_purchage_order/' + code + "/" + status, function (rs) {
        window.location.href = "/admin/goods_purchace/purchaseorder/";
    });
}
django.jQuery(document).ready(function () {
    if ($('.field-orderstatus')[0].children[0].children[1].children[0].innerHTML == "待审核") {
        $('.submit-row').append("<button type='button'  class='btn' onclick='btn_Approve(1)'>审批通过</input>");
        $('.submit-row').append("<button class='btn btn-danger' onclick='btn_Approve(0)'>审批驳回</button>");
    } else {
        $('.change-related').hide();
        $('.add-related').hide();
        $('.save-box').hide();
        $('.table-bordered tr').find('th:last-child, td:last-child').remove();
        $('.table-bordered').remove($('.add-row'));
    }

    $('input').live('keyup', function () {
        if (this.name.indexOf("purchaseNumber") != -1) {
            if (this.value != "" && this.parentElement.parentElement.children[4].children[0].value != "") {
                this.parentElement.parentElement.children[5].innerHTML = parseFloat(this.value) *
                    parseFloat(this.parentElement.parentElement.children[4].children[0].value);
            }
        }

        if (this.name.indexOf("buysmoney") != -1) {
            if (this.value != "" && this.parentElement.parentElement.children[3].children[0].value != "") {
                this.parentElement.parentElement.children[5].innerHTML = parseFloat(this.value) *
                    parseFloat(this.parentElement.parentElement.children[3].children[0].value);
            }
        }
    });

    $('input').live('change', function () {
        if (this.name.indexOf("buysmoney") != -1) {
            if (this.value != "" && this.parentElement.parentElement.children[3].children[0].value != "") {
                this.parentElement.parentElement.children[5].innerHTML = parseFloat(this.value) *
                    parseFloat(this.parentElement.parentElement.children[3].children[0].value);
            }
        }
    });

    $('select').live('change', function () {
        var self = this;
        $.get('/api/purchaseordergoods/' + this.value, function (rs) {
            self.parentElement.parentElement.parentElement.children[1].innerHTML = rs.sailsmoney;
            self.parentElement.parentElement.parentElement.children[2].innerHTML = rs.suggesstBuysmoney;
            self.parentElement.parentElement.parentElement.children[4].children[0].value = rs.suggesstBuysmoney;
        })
    })
})
