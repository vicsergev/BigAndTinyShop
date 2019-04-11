window.onload = function () {
    // console.log("загрузили DOM");
    $(".basket-list").on("change", "input[type='number']", function (event) {
        // console.log(event);
        var target = event.target;        
        $.ajax({
            url: "/basket/update/" + target.name + "/" + target.value + "/",
            success: function (data) {
//                console.log(data);
                $('.basket-list').html(data.result);
            }
        });
    });
}