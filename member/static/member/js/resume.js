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
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        }).done(function (data, textStatus, jqXHR) {
            window.location.href = '/accounts/resume/' + data.resume_uuid;
        }).fail(function (jqXHR, textStatus, errorThrown) {
            var error_message = $('.error-message');

            error_message.addClass('is-block').removeClass('is-hidden');
            error_message.html('You cannot have more than 3 resumes.');
        });
    });

    $('.delete-resume').on('click', function (e) {
        $.ajax({
            url: '/accounts/resume/delete/' + $(this).data('resume-no'),
            type: 'post',
            dataType: 'json',
            data: {
                'title': 'Resume title',
                'description': 'Resume summary'
            },
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        }).done(function (data, textStatus, jqXHR) {
            window.location.href = '/accounts/resume/';
        }).fail(function (jqXHR, textStatus, errorThrown) {
        });
    });

    $('.make-primary-resume').on('click', function (e) {
        $('.modal').toggleClass('is-active');
        $('html').toggleClass('is-clipped');
    });

    $('.modal-card-head .delete, .modal-card-foot .cancel').on('click', function (e) {
        $('.modal').toggleClass('is-active');
        $('html').toggleClass('is-clipped');
    });
});