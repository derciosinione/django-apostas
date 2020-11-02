$(document).ready(function() { 
    
    $("[rel=popover]").popover();
    
    $("[rel=tooltip]").tooltip();
    
    $('.check-all').click(
            function(){
                $(this).parent().parent().parent().parent().find("input[type='checkbox']").attr('checked', $(this).is(':checked'));   
            }
        );
        
    $('#select-all').click(function(event) {   
    if(this.checked) {
        // Iterate each checkbox
        $(':checkbox').each(function() {
            this.checked = true;                        
        });
    }
    });
    
});