$(document).ready(function(){
    var form = $('[name="form_choosing_book"]');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var submit_btn = $('[class="btn btn-sm btn-outline-secondary"]');
        var book_id = submit_btn.data('book_id');
        var book_name = submit_btn.data("book_name");
        consolе.log(book_id);
        console.log(book_name);

    })
})
