function handleOnChange (){
    let passwordfield = document.getElementById("passwordCreate").value
    document.getElementById("passwordCreate2").value = passwordfield;
    console.log(document.getElementById("passwordCreate2").value)
}