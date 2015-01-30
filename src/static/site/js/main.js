$("#sub").click(function(){
    if($("#q_title").val() == "")
    {
        alert("请填写标题");
        return false;
    }
    if($("#q_content").val() == "")
    {
        alert("请填写描述");
        return false;
    }
});

