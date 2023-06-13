function keyprosearch(){
    var xhttp=new XMLHttpRequest();
    xhttp.open('GET','contain/'+document.getElementById('keyword').value,true)
    xhttp.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var data=JSON.parse(this.responseText);
            str='<table>'
            for(x of data.newval){
                str=str+'<tr>';
                    str += '<td>' + x.name + '</td>';
                    str=str+'<td>₹'+ x.price + '</td>';
            }
            str=str+'</table>';
            document.getElementById('data').innerHTML = str
        }
    }
    xhttp.send();}