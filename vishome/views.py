from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from .models import item
from .models import contactdet
from django.template import loader

def landing(req):
    page=loader.get_template('landingpage.html')
    db=item.objects.all()
    response=page.render({'pro':db},req)
    return HttpResponse(response)

def addcart(req):
    id=req.GET['proid']
    qty=req.GET['proqty']
    cartitems={}
    if req.session.__contains__('cartdata'):
        cartitems=req.session['cartdata']
    cartitems[id]=qty
    req.session['cartdata']=cartitems
    print(cartitems)
    print(req.session['cartdata'])
    return render(req,'itemadd.html')

def viewcart(req):
    page=loader.get_template('mycart.html')
    if req.session.__contains__('cartdata'):
        if req.session['cartdata']:
            for i in req.session.keys():
                if i=='cartdata':
                    amt=0
                    a=list(req.session[i].items())
                    b=[]
                    for j in a:
                        proid=j[0]
                        proqty=0
                        if j[1]=='':
                            proqty=0
                        else:
                            proqty=int(j[1])
                        db=item.objects.get(id=proid)
                        b.append({'Id':j[0],'Qty':proqty,'Name':db.proname})
                        amt+=proqty*db.proprice
            response=page.render({'pro':b,'amount':amt},req)
            return HttpResponse(response)
        else:
            return render(req,'noitems.html')
    return render(req,'noitems.html')
    
def searchitem(req):
    return render(req,'prodsearch.html')

def getdata(req,keyword):
    newitem=[]
    for i in item.objects.filter(proname__contains=keyword):
        newitem.append({
            'id':i.id,
            'name':i.proname,
            'price':i.proprice,
            'specification':i.prospec
        })
    data={'newval':newitem}
    return JsonResponse(data)

def delete_item(req):
    if req.method == 'POST':
        item_id = req.POST.get('item_id')
        if item_id:
            del req.session['cartdata'][item_id]
            req.session.modified = True
            return render(req,'itemdel.html')

def contactus(req):
    return render(req,'contactus.html')

def addet(req):
    cnt=contactdet(
        name=req.POST['cname'],
        emailid=req.POST['cemail'],
        phone=req.POST['cphno']
    )
    cnt.save() #to save the data in databsase
    return render(req,'usrcreated.html')


