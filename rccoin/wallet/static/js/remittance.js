var id_isValidated = false

function chk_target() {
    let target = $("#target").val()
    msg = ""
    if ( target.length < 1 ) {
        msg = '받는 계정을 입력해주세요.'
        $("#target").prop("focus", true)
    } else if ( target == $("#to").val() ) {
        msg = "자신에게는 송금할 수 없습니다."
    } else {
        $.ajax({
            type: "GET",
            url: "/account/chk_username",
            data: {
                username : target
            },
            dataType : "json",
            async: false,
        }).done(function(res) {
            if ( res['exist'] ) {
                id_isValidated = true
                msg = "송금 가능한 사용자입니다."
            } else {
                msg = "사용자 계정을 확인 할 수 없습니다."
            }        
        });
    }
    alert(msg)
}

function chk_validate() {
    if ( id_isValidated ) {
        return true
    } else {
        alert('받는 계정을 조회해주세요.')
    }
    return false
}

$(function() {
    $("#target").on("change", function() {
        id_isValidated = false
    })
})