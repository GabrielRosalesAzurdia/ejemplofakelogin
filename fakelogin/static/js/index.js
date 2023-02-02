function handleOnChange (){
    let passwordfield = document.getElementById("passwordCreate").value
    document.getElementById("passwordCreate2").value = passwordfield;
    console.log(document.getElementById("passwordCreate2").value)
}

function loadmodal() {
    if('{{showmodal}}' == 'show'){
        document.getElementById("#createUserModal").modal("show")
    }
}
window.onload = codeAddress;