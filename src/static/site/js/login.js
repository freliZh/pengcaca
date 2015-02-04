$(document).ready(function() {
    $('.ui.form')
      .form(
      {
          firstName: {
              identifier: 'first-name',
              rules: [
                  {
                      type: 'empty',
                      prompt: '请填写姓'
                  }
              ]
          },
          lastName: {
              identifier: 'last-name',
              rules: [
                  {
                      type: 'empty',
                      prompt: '请填写名'
                  }
              ]
          },
          username: {
              identifier: 'username',
              rules: [
                  {
                      type: 'empty',
                      prompt: '请填写用户名（昵称）'
                  }
              ]
          },
          phone_number: {
              identifier: 'phone_number',
              rules: [
                  {
                      type: 'empty',
                      prompt: '请填写电话号码'
                  },
                  {
                      type: 'length[11]',
                      prompt: '电话号码至少为11个字符'
                  }
              ]
          },
          address: {
              identifier: 'address',
              rules: [
                  {
                      type: 'empty',
                      prompt: '请填写常用地址'
                  }
              ]
          },
          password: {
              identifier: 'password',
              rules: [
                  {
                      type: 'empty',
                      prompt: '请填写密码'
                  },
                  {
                      type: 'length[6]',
                      prompt: '密码至少为6个字符'
                  }
              ]
          },
          password_confirm: {
              identifier: 'password_confirm',
              rules: [
                  {
                      type: 'empty',
                      prompt: '请填写确认密码'
                  },
                  {
                      type: 'match[password]',
                      prompt: '两次输入密码不一致'
                  }
              ]
          },
          terms: {
              identifier: 'terms',
              rules: [
                  {
                      type: 'checked',
                      prompt: '您必须同意彭擦擦网站的协议'
                  }
              ]
          }
      },
       {
          inline : true,
          onSuccess: submit_form
       });
      $('.ui.checkbox')
      .checkbox()
      ;
    function submit_form()
    {
        var formData = $('.ui.form.segment input').serializeArray();
        $.ajax({
            type:"post",
            url: "/account/login",
            data: formData,
            success: function(text){
               if(text == "F")
               {
                   $("#z_warning").show();
               }else{
                    $("#z_warning").hide();
               }
            }
        });

    }
});