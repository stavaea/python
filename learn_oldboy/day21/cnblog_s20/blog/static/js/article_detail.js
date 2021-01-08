$(".action").click(function () {
    if ($(".info").attr("username")) {
        var is_up;
        // is_up ：赞or灭
        is_up = $(this).hasClass("diggit");
        article_id = $(".info").attr("article_id");
        //
        $.ajax({
            url: "blog/digg/",
            type: "post",
            data: {
                is_up: is_up,
                article_id: article_id,
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()

            },
            success: function (data) {
                console.log(data);
                console.log(typeof data);

                if (data.state) {// 点赞或者踩灭成功

                    if (is_up) {
                        var val = $("#digg_count").text();
                        val = parseInt(val) + 1;
                        $("#digg_count").text(val);
                    }
                    else {
                        var val = $("#bury_count").text();
                        val = parseInt(val) + 1;
                        $("#bury_count").text(val);
                    }

                }
                else {   //重复提交
                    console.log(data.first_action);
                    console.log(typeof data.first_action);

                    if (data.first_action) {
                        $("#digg_tips").html("您已经推荐过了");

                        setTimeout(function () {
                            $("#digg_tips").html("");
                        }, 1000)

                    }
                    else {
                        $("#digg_tips").html("您已经反对过了");
                        setTimeout(function () {
                            $("#digg_tips").html("");
                        }, 1000)
                    }

                }
            }
        })

    }
    else{
        var s="<a href='/login/' class='pull-right'>请登陆！</a>";

        $("#div_digg").after(s);

    }

});
















