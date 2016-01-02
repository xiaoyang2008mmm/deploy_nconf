$(document).ready(function() {
    $('body').on('click', 'button[id*=v_edit]', function() {
            alert("111");
    });
    $('body').on('click', 'button[id*=v_test]', function() {
            alert("2222");
    });
    $('body').on('click', 'button[id*=v_reload]', function() {
            alert("3333");
    });
});
