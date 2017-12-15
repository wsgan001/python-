 function AjaxSubmit(){
        var host = '1.1.1.1';
        var port = '1111';
        $.ajax({
            url:"/ajax1",
            type:'POST',
            data:{host:host,port:port},
            success: function (arg) {
            }

        });
    }