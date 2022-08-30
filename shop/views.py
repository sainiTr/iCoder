import json
from operator import truediv
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from shop.models import Product, User as userdata, orders, orderupdate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):

    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)

        allprods.append(prod)

    captions = {
        'products': allprods
    }

    if not request.user.is_anonymous:
        if str(request.user).replace(" ", "") != 'tenali':
            print("The user is : ", request.user)
            d = userdata.objects.filter(user=request.user)
            print("The user is : ", d[0].image)
            print("The user is : ", d[0].fname+" " + d[0].lname)
            captions['image'] = d[0].image
            captions['user'] = d[0].fname.capitalize() + " " + \
                d[0].lname.capitalize()

    return render(request, 'shop/index.html', captions)

def searchMatch(query, item):
    querys = str(query).split(" ")
    for query in querys:
        if query in str(item.desc).lower() or query in str(item.name).lower() or query in str(item.category).lower() or query in str(item.subcategory).lower() or query in str(item.price).lower(): 
            return True
        else:
            return False
    print(query,item)
    # return False

def search(request):
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        proditem = Product.objects.filter(category=cat)
        prod = [item for item in proditem if searchMatch(query,item)]

        allprods.append(prod)

    captions = {
        'products': allprods
    }
    return render(request,'shop/index.html',captions)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid')
        email = request.POST.get('email')
        f = f"Order is  {orderid} \n{email}"
        try:
            data = orders.objects.filter(
                addr_id=orderid, email=f'{email}').exists()
            if data:
                newupdates = orderupdate.objects.filter(up_id=orderid)
                updates = []
                for update in newupdates:
                    updates.append(
                        {'text': update.up_id, 'desc': update.desc, 'time': update.time})

                    response = json.dumps([updates, orders.objects.filter(
                        addr_id=orderid)[0].cartjson], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse({"error": 1})
        except Exception as e:
            print(e)
            return HttpResponse({'error': 1})
    else:
        return render(request, 'shop/tracker.html')


def productview(request):
    return HttpResponse('we are at productview')


def checkcart(request):
    data = Product.objects.all()
    ids = [1, 2, 4, 56, 61, 65, 70]
    fdata = []
    for i in ids:
        for item in data.filter(id=i):
            fdata.append(item)
    parems = {
        'data': fdata
    }
    return render(request, 'shop/productCart.html', parems)


def UploadProd(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        subcat = request.POST.get('subcat')
        date = request.POST.get('date')
        available = request.POST.get('available')
        image = request.POST.get('image')
        desc = request.POST.get('desc')

        s = Product(name=name, price=price, category=category, subcategory=subcat,
                    desc=desc, pubdate=date, image=f"shop/images/{image}", available=available)

        s.save()

    return render(request, 'shop/chackout.html')


def productview(request, id):
    product = Product.objects.filter(id=id)

    return render(request, 'shop/productView.html', {'product': product[0]})


def SignUp(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        user = request.POST.get('user')
        profile = request.POST.get('profile')
        password = request.POST.get('pass')

    # Save the user data at adjango server
        if not User.objects.exclude().filter(username=user).exists():
            userdetails = userdata(fname=firstName, lname=lastName, birthday=birthday, gender=gender,
                                   email=email, user=user, image='shop/profiles/'+profile, passw=password)
            userdetails.save()

            # # # Creating a New User ########################``
            user = User.objects.create_user(user, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()

        else:
            print("The user is Alrady exist : ")

    return render(request, 'shop/Ragistration.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('The user and password is : '+username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect(f'/shoppingmall')

        else:
            return redirect('/shoppingmall/login')

            # No backend authenticated the credentials
    return render(request, 'shop/login.html')


def Profile(request):
    if not request.user.is_anonymous:
        if str(request.user).replace(" ", "") == 'tenali':
            data = {
                'data': request.user
            }
            return render(request, 'shop/profile.html', data)
        return redirect('/shoppingmall/login')
    else:
        return redirect('/shoppingmall/login')


def logoutuser(request):
    logout(request)
    return redirect('/shoppingmall/login')


def checkoutproduct(request, cart):
    from django.template import RequestContext

    print(request.COOKIES['csrftoken'])
    f = HttpResponse("j")
    f.set_cookie('value', 'I am Monu Saini')
    if request.method == 'POST':

        cartjson = request.POST.get('cartjson')
        name = request.POST.get('fname')+" " + request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('addr1')+" " + request.POST.get('addr2')
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")
        amount = request.POST.get('amount')

        addrs = orders(cartjson=cartjson, name=name, email=email, phone=phone,
                       address=address, city=city, state=state, zip_code=zip_code, amount=amount)
        addrs.save()
        update = orderupdate(up_id=addrs.addr_id,
                             desc='Your Order is place   ')
        update.save()
        return redirect('/shoppingmall/tracker')
    return render(request, 'shop/checkoutprod.html')
    # return HttpResponse("hello i am Monu Saini")


def pushorderupdate(request):
    if not request.user.is_anonymous:
        if str(request.user).replace(" ", "") == 'tenali':
            if request.method == "POST":
                print("The newupdate is pushed")
                update_id = request.POST.get('update_id')
                newupdate = request.POST.get("newudate")
                orderupdate(up_id=update_id, desc=newupdate).save()
                return redirect('/shoppingmall/ordernewupdate')
            else:
                data = orderupdate.objects.all()
                ordersupdate = []
                for item in data:
                    order = data.filter(up_id=item.up_id)

                    ord = [item.up_id, order[len(order)-1].desc, item.time]
                    if ord not in ordersupdate:
                        ordersupdate.append(ord)

                newupdates = {
                    'updates': ordersupdate
                }

                return render(request, 'shop/pushorderupdate.html', newupdates)
        else:
            return redirect('/shoppingmall/login')
    else:
        return redirect('/shoppingmall/login')


def handlepayment(request):
    pass

