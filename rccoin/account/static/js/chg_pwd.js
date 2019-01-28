function chk_password() {
    var msg = ""
    var pattern = /^.*(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$]).*$/
    
    // if ( $("#password").val().length < 1) {
    //     msg = "현재 비밀번호를 입력해주세요."
    // }
    // else if ( $("#password1").val().length < 8 )  {
    //     msg = "새 비밀번호는 8자 이상의 길이이어야 합니다."
    // } else if (! pattern.test($("#password1").val()) ) {
    //     msg = "새 비밀번호는 알파벳 대소문자, 숫자, 특수문자(!@#$)를 최소 하나씩 포함해야합니다."
    // } else if ( $("#password").val() == $("#password2").val() ) {
    //     msg = "현재 비밀번호와 같은 비밀번호는 사용할 수 없습니다."
    // } else if ( $("#password1").val() != $("#password2").val() ) {
    //     msg = "새 비밀번호가 일치하지 않습니다."
    // } else {
    //     return true
    // }
    // alert(msg)
    // return false
    return true
}