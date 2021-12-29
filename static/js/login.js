function check(form)
{
    if(form.id.value == "17011700" && form.pw.value == "1234")
    {
        // location.href="blackboard.html"
        window.open("blackboard.html","_blank")
    }
    else
    {
        alert("잘못된 아이디 혹은 비밀번호입니다.")
        window.open('login.html', '_self')
    }
}

function signup(form)
{
    var type1 = document.getElementById("identify").type;
    var type2 = document.getElementById("Password").type;

    if(type1 == text && type2 == password)
    {
        window.open('login.html', '_blank')
    }
    else{
        alert("잘못된 형식입니다.")
    }
}