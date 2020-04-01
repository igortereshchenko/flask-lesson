

function add_job(job_title, job_salary, job_skils){

    var new_job = {"title": job_title, "salary": job_salary, "skill": job_skils};

    $.ajax({
    type: "POST",
    url: '/addjob',
    data: new_job,
    dataType : "json",
    success: function (data) {

        if (data.status=='ok'){
            window.location.replace(data.redirect);
        }

    }
    });
}

