$('.date-picker').datepicker();
$(function(){
    $(".manager_user_show").click(function(){
        var id = $(this).parent().parent('tr').children('td').first().text();
        console.log($(this).parent().parent('tr'));
        console.log(id);
        $("#manager_user_show_modal .modal-body").load('show?id=' + id ); 
    });

    $("#select_add").click(function() {
        var $options = $('#select_1 option:selected');
        var $remove = $options.remove()
        $remove.appendTo("#select_2");
    });

    $("#select_remove").click(function() {
        var $options = $('#select_2 option:selected');
        var $remove = $options.remove()
        $remove.appendTo("#select_1");
    });
});
