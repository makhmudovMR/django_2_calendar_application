function deleteCalendarEntery(entery)
{
	$(entery).parent().remove()
	var id = $(entery).data('id')
	console.log(id)
	console.log(csrf_token)

	$.ajax({
		url: 'entery/delete/' + id,
		method: 'DELETE',
		beforeSend: function(xhr){
			xhr.setRequestHeader('X-CSRFToken', csrf_token)
		}
	})
}