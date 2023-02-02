function handleOnChange (){
    let passwordfield = document.getElementById("passwordCreate").value
    document.getElementById("passwordCreate2").value = passwordfield;
    console.log(document.getElementById("passwordCreate2").value)
}

function loadmodal() {
    let meta = document.querySelector('meta[name="load-modal-name"]').content
    if(meta == 'show'){        
        let myModal = new bootstrap.Modal(document.getElementById('createUserModal'))
        myModal.show()
    }
}
window.onload = loadmodal;