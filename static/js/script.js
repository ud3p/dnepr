$('#show_username').click(function(){
  $(this).text('admin')
});

$('#show_password').click(function(){
  $(this).text('admin')
});

$('.index').each(function(){
   $(this).html( $(this).html().replace(/((http|https|ftp):\/\/[\w?=&.\/-;#~%-]+(?![\w\s?&.\/;#~%"=-]*>))/g, '<a target="_blank" href="$1">$1</a> ') );
});

