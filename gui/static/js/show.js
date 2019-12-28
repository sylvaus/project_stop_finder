function show() {
    var checkBox = document.getElementById("show_table");
    var table = document.getElementsByClassName("table");
    for (let index = 0; index < table.length; index++) {
        if (checkBox.checked == true) {
            table[index].style.display = "flex";
        } else {
            table[index].style.display = "none";
        }
    }
}