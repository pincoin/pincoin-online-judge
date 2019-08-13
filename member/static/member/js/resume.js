$(document).ready(function () {
    $('#new-resume').on('click', function (e) {
        $('#warning').hide();

        $.ajax({
            url: '/accounts/resume/add/',
            type: 'post',
            dataType: 'json',
            data: {
                'title': 'Resume title',
                'description': 'Resume summary'
            },
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }).done(function (data, textStatus, jqXHR) {
            window.location.href = '/accounts/resume/' + data.uuid;
        }).fail(function (jqXHR, textStatus, errorThrown) {
            $('#warning').show();
            $('#warning-message').html('You can write 3 resumes.');
        });
    });
});