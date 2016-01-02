$(document).ready(function() {
    $('body').on('click', 'button[id*=v_edit]', function() {
	    var $this = $(this);
	    var $host = $($this.parent().parent().find('strong')).text();
	    //console.log($host);
	    alert($host);
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
