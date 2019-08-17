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

    $('.delete-resume').on('click', function (e) {
        console.log('delete resume');

        var me = $(this), data = me.data('resume-no');

        console.log(data);

        $.ajax({
            url: '/accounts/resume/delete/' + data,
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
            window.location.href = '/accounts/resume/';
        }).fail(function (jqXHR, textStatus, errorThrown) {
            $('#warning').show();
            $('#warning-message').html('You can write 3 resumes.');
        });
    });
});