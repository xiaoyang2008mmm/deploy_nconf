$(document).ready(function() {
    $('body').on('click', 'button[id*=v_edit]', function() {
	    var $this = $(this);
	    var $host = $($this.parent().parent().find('strong')).text();
	    var $select_index = $($this.parent().parent().find('select'));
	    var $select_file = $select_index.find("option:selected").text();
	    //console.log($host);
	    alert($host);
	    alert($select_file);
    });
    $('body').on('click', 'button[id*=v_test]', function() {
	    var $this = $(this);
	    var $host = $($this.parent().parent().find('strong')).text();
	    //console.log($host);
	    alert($host);
    });
    $('body').on('click', 'button[id*=v_reload]', function() {
	    var $this = $(this);
	    var $host = $($this.parent().parent().find('strong')).text();
	    //console.log($host);
	    alert($host);
    });
});
