from django.http import HttpResponse
import threading
from django.shortcuts import render
import json
from django.core import serializers
from .models import *
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.db.models import Count
from django.views.decorators.cache import never_cache
from django.core.files.storage import FileSystemStorage
import os
import pickle
from blockchain import *
from django.db.models import Q
import base64
import ipfshttpclient
import shutil
from pathlib import Path

# For machine learning
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

global idd, tk_idd
s_a = open("C:/Users/benba/Anaconda/Blockchain/Blockchain/s_id.txt", "r+")
s_aa = s_a.readline()
s_a.close()
t_a = open("C:/Users/benba/Anaconda/Blockchain/Blockchain/tk_id.txt", "r+")
t_aa = t_a.readline()
t_a.close()
idd = int(s_aa)
tk_idd = int(t_aa)
print("####")
print("idd", idd)
print("####")
print("####")
print("tk_idd", tk_idd)
print("####")
#####################################################################################################################################################################


@never_cache
def show_index(request):
    return render(request, "login.html", {})


@never_cache
def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
    return render(request, 'login.html')


@never_cache
def show_register(request):
    return render(request, "register.html", {})


@never_cache
def register(request):
    name = request.POST.get("name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    gender = request.POST.get("gender")
    address = request.POST.get("address")
    mobile = request.POST.get("mobile")
    p_address = request.POST.get("p_address")

    obj12 = Users.objects.filter(p_address=p_address)
    co = obj12.count()
    if co == 1:
        return HttpResponse("<script>alert('Public Address Already Exists');window.location.href='/show_register/'</script>")

    obj178 = Requests.objects.filter(p_address=p_address)
    co = obj178.count()
    if co == 1:
        return HttpResponse("<script>alert('Public Address Already Exists');window.location.href='/show_register/'</script>")

    obj121 = Users.objects.filter(username=username)
    co = obj121.count()
    if co == 1:
        return HttpResponse("<script>alert('Username Already Exists');window.location.href='/show_register/'</script>")

    obj10 = Requests.objects.filter(mobile=mobile, username=username, password=password,
                                    p_address=p_address, name=name, address=address, gender=gender)
    co = obj10.count()
    if co == 1:
        return HttpResponse("<script>alert('Request is in Pending list');window.location.href='/show_index/'</script>")

    else:
        obj1 = Requests(mobile=mobile, username=username, password=password,
                        p_address=p_address, name=name, address=address, gender=gender)
        obj1.save()
        return HttpResponse("<script>alert('Request sent, Wait For Approval');window.location.href='/show_index/'</script>")


@never_cache
def check_login(request):

    username = request.POST.get("username")
    password = request.POST.get("password")

    print(username)
    print(password)

    if username == 'admin' and password == 'admin':
        request.session["uid"] = "admin"
        return HttpResponse("<script>alert('Admin Login Successful');window.location.href='/show_home_admin/'</script>")

    else:
        obj2 = Users.objects.filter(username=username, password=password)
        c2 = obj2.count()
        print(c2)
        if c2 == 1:
            ob9 = Users.objects.get(username=username, password=password)
            request.session["uid"] = ob9.r_id
            request.session["username"] = ob9.username
            request.session["name"] = ob9.name
            return HttpResponse("<script>alert('User Login Successful');window.location.href='/show_home_user/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid');window.location.href='/show_index/'</script>")


@never_cache
# ADMIN START
def show_home_admin(request):
    if 'uid' in request.session:
        print(request.session['uid'])
        return render(request, 'home_admin.html')
    else:
        return render(request, 'login.html')


@never_cache
def show_request_admin(request):
    if 'uid' in request.session:
        print(request.session['uid'])
        req_list = Requests.objects.all()

        return render(request, 'view_request_admin.html', {'req': req_list})
    else:
        return render(request, 'login.html')


@never_cache
def show_user_admin(request):
    if 'uid' in request.session:
        print(request.session['uid'])
        obj = get_users()
        print("###############################")
        print("###############################")
        print("###############################")
        print(obj)
        print("###############################")
        print("###############################")
        print("###############################")
        return render(request, 'view_user.html', {'obj': obj})
    else:
        return render(request, 'login.html')


@never_cache
def approve(request):
    r_id = request.POST.get('r_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    mobile = request.POST.get('mobile')
    p_address = request.POST.get('p_address')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    if not verify_adr(p_address):
        obj32 = Requests.objects.get(r_id=int(r_id))
        obj32.delete()
        return HttpResponse("<script>alert('Public Key does not belong to blockchain');window.location.href='/show_request_admin/';</script>")
    else:

        obj1 = Users(username=username, password=password, name=name,
                     address=address, gender=gender, mobile=mobile, p_address=p_address)
        obj1.save()
        obj2 = Users.objects.get(username=username, password=password, name=name,
                                 address=address, gender=gender, mobile=mobile, p_address=p_address)
        user_id = obj2.r_id
        print("User id : ", user_id)
        add_user1(user_id, username, password, name,
                  mobile, p_address, address, gender)

        obj3 = Requests.objects.get(r_id=int(r_id))
        obj3.delete()
        return HttpResponse("<script>alert('Approved Successfully');window.location.href='/show_request_admin/'</script>")


@never_cache
def reject(request):
    r_id = request.POST.get('r_id')
    obj1 = Requests.objects.get(r_id=int(r_id))
    obj1.delete()
    return HttpResponse("<script>alert('Rejected');window.location.href='/show_request_admin/'</script>")


@never_cache
def show_home_user(request):
    if 'uid' in request.session:
        name = request.session["name"]
        return render(request, 'home_user.html', {'value': name})
    else:
        return render(request, 'login.html')


def show_price_predictor(request):
    if 'uid' in request.session:
        name = request.session["name"]
        return render(request, 'predict.html')
    else:
        return HttpResponse("<script>alert('Some unknown error occurred....Try again');window.location.href='/show_home_user/'</script>")


def predict(request):
    return render(request, "predict.html")


def predict_result(request):
    data = pd.read_csv(
        r"C:/Users/benba/Anaconda/Blockchain/Blockchain/DataSet/USA_Housing.csv")
    data = data.drop(['Address'], axis=1)
    X = data.drop('Price', axis=1)
    Y = data['Price']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.30)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    try:
        var1 = float(request.GET['n1'])
    except (KeyError, ValueError):
        var1 = 68583.1089839702

    try:
        var2 = float(request.GET['n2'])
    except (KeyError, ValueError):
        var2 = 5.977222035287

    try:
        var3 = float(request.GET['n3'])
    except (KeyError, ValueError):
        var3 = 6.9877918509092

    try:
        var4 = float(request.GET['n4'])
    except (KeyError, ValueError):
        var4 = 3.98133

    try:
        var5 = float(request.GET['n5'])
    except (KeyError, ValueError):
        var5 = 36163.5160385404

    pred = model.predict(
        np.array([var1, var2, var3, var4, var5]).reshape(1, -1))
    pred = round(pred[0])

    price = "The predicted price is $" + str(pred)

    return render(request, "predict.html", {"result2": price})


#######################################################################################################################
##################################################################################################################
# ------------------------------------------------Normal----------------------------------------------------------------#
#######################################################################################################################
#######################################################################################################################
@never_cache
def sell_intro(request):
    if 'uid' in request.session:
        name = request.session["name"]
        return render(request, 'sell_intro.html')
    else:
        return render(request, 'login.html')


@never_cache
def Sell(request):
    if 'uid' in request.session:
        name = request.session["name"]
        s_type = request.POST.get("Select")
        if (s_type == "Normal"):
            return render(request, 'Sell.html')  # Normal sell page
        else:
            return render(request, 'Sell_token.html')  # Token sell page
    else:
        return render(request, 'login.html')


@never_cache
def Sell_1(request):
    global dd
    if 'uid' in request.session:
        if (dd == 0):
            return render(request, 'Sell.html')  # Normal sell page
        else:
            return render(request, 'Sell_token.html')  # Token sell page
    else:
        return render(request, 'login.html')


def sell(request):  # sell page
    global dd, idd
    idd = idd+1
    dd = 0
    name = request.session["name"]
    username = request.session["username"]
    ptype = request.POST.get("Selecttt")  # prp type
    p_id = request.POST.get("P_ID")  # prp id
    private = request.POST.get("pvt")  # private key
    details = request.POST.get("details")
    amount = request.POST.get("amount")
    image = request.FILES["image"]
    ####################################
    status = "Pending"
    file_name1 = image.name
    file_name = p_id+".jpg"
    print("image:", file_name)
    print("###################################")
    api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    new_file = api.add("SHCS_app/Images/"+str(file_name1))
    print(new_file)
    hash1 = new_file.get('Hash')
    print("###########hash1:", hash1)
    ###########################################################################################
    hashh = []
    check = []
    username = request.session["username"]
    ab = get_prps()
    print("####val:", ab)
    print("######################")
    val = ab.values()
    print("####val:", val)
    print("######################")
    for i in val:
        d1 = i
        et = str(d1['hash1'])
        if (et == hash1):
            check = []
    ###########################################################################################
    if check != []:
        return HttpResponse("<script>alert('Try another property');window.location.href='/Sell_1/';</script>")
    else:
        obb = Users.objects.get(username=username)
        pb = obb.p_address
        phn = obb.mobile
        print(pb)
        a = verify_key(pb, private)
        print(a)
        if (a == "Yes"):
            obj22 = Selling.objects.filter(Prop_id=p_id)
            c22 = obj22.count()
            print(c22)
            #########################################
            obj23 = Token.objects.filter(Prop_id=p_id)
            c23 = obj23.count()
            print(c23)
            ##########################################
            obj24 = Buyed.objects.filter(p_id=p_id)
            c24 = obj24.count()
            print(c24)
            #########################################
            if (c22 == 0 and c23 == 0 and c24 == 0):
                status = "Pending"
                obj11 = Selling(r_id1=idd, Name=name, Ptype=ptype, Prop_id=p_id, details=details,
                                image=file_name, mobile=phn, amount=amount, username=username, status=status, hash1=hash1)
                obj11.save()
                obj32 = Selling.objects.get(Prop_id=p_id)
                h = obj32.Prop_id
                us = obj32.r_id1
                us = int(us)
                print("#########:", us)
                print("Type :", type(h))
                add_prop(us, h, username, ptype, details,
                         file_name, amount, status, phn, hash1)
                ###################################################################################
                se_id = str(idd)
                print("##############", se_id)
                f1 = open(
                    'C:/Users/benba/Anaconda/Blockchain/Blockchain/s_id.txt', 'w')
                f1.write(se_id)
                f1.close()
                ###################################################################################
                return HttpResponse("<script>alert('Successfully Added');window.location.href='/show_home_user/';</script>")
            else:
                return HttpResponse("<script>alert('Property ID is already existed');window.location.href='/Sell_1/';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/Sell_1/';</script>")


@never_cache
def View_s(request):  # to view the selled properties
    if 'uid' in request.session:
        return render(request, 'View_s.html')
    else:
        return render(request, 'login.html')


@never_cache
def View_selled(request):
    s_type = request.POST.get("Select")
    if (s_type == "Normal"):
        se = []
        hashh = []
        fname = []
        username = request.session["username"]
        ab = get_prps()
        print("######################")
        print(ab)
        print("######################")

        print("######################")
        val = ab.values()
        print("####val:", val)
        print("######################")
        for i in val:
            d1 = i
            et = str(d1['Prop_id'])
            try:
                blk12 = Selling.objects.get(Prop_id=et, username=username)
                st = blk12.status
                if (d1['username'] == username and d1['status'] == "Pending" and st != "Buyed"):
                    se.append(d1)
            except:
                continue
        print("######selled:", se)
        if se == []:
            return HttpResponse("<script>alert('No datas to show');window.location.href='/View_s/';</script>")
        else:
            if os.path.isdir("SHCS_app/static/"+"Ipfs"):
                shutil.rmtree("SHCS_app/static/"+"Ipfs")
                os.makedirs("SHCS_app/static/"+"Ipfs")
            else:
                os.makedirs("SHCS_app/static/"+"Ipfs")
            for j in se:
                d2 = j
                ss1 = d2['hash1']
                ss2 = d2['file_name']
                hashh.append(ss1)
                fname.append(ss2)
            for k in range(0, len(hashh)):
                ab = str(hashh[k])
                ab = ab.strip()
                api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
                api.get(ab)
                fn = str(fname[k])
                new_file = fn
                with open(ab, 'rb') as f1:
                    with open("SHCS_app/static/"+"Ipfs/"+new_file, 'wb') as f2:
                        f2.write(f1.read())
                os.remove("C:/Users/benba/Anaconda/Blockchain/Blockchain/"+ab)
            return render(request, 'view_sell.html', {'selled': se})
    else:
        img = []
        hsh = []

        username = request.session["username"]
        bkkl = Token.objects.filter(username=username)
        c3 = bkkl.count()
        if (c3 > 0):
            bkkl1 = Token.objects.filter(
                username=username).values('image', 'hashh')

            bkkl1 = list(bkkl1)
            print("bkkl1########:", bkkl1)
            ##########################################################################
            if os.path.isdir("SHCS_app/static/"+"Ipfs"):
                shutil.rmtree("SHCS_app/static/"+"Ipfs")
                os.makedirs("SHCS_app/static/"+"Ipfs")
            else:
                os.makedirs("SHCS_app/static/"+"Ipfs")
            for i in bkkl1:
                dc = i
                image = str(dc['image'])
                hashh = str(dc['hashh'])
                hashh = hashh.strip()
                #############################################################
                api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
                api.get(hashh)
                with open(hashh, 'rb') as f1:
                    with open("SHCS_app/static/"+"Ipfs/"+image, 'wb') as f2:
                        f2.write(f1.read())
                os.remove(
                    "C:/Users/benba/Anaconda/Blockchain/Blockchain/" + hashh)
            ################################################################
            ##########################################################################
            return render(request, 'view_sell_tk.html', {'users': bkkl})
        else:
            return HttpResponse("<script>alert('No datas to show');window.location.href='/View_s/';</script>")


@never_cache
def Buy(request):
    if 'uid' in request.session:
        return render(request, 'Buy.html')
    else:
        return render(request, 'login.html')


@never_cache
def Buy_p(request):
    s_type = request.POST.get("Select")
    if (s_type == "Normal"):
        se = []
        hashh = []
        fname = []
        username = request.session["username"]
        ab = get_prps()
        print("######################")
        print(ab)
        print("######################")

        print("######################")
        val = ab.values()
        print("####val:", val)
        print("######################")
        sta = "Pending"
        for i in val:
            d1 = i
            print("##############")
            print("########d1:", d1)
            print("##############")
            et = str(d1['Prop_id'])
            print("et#########:", et)
            try:
                blk12 = Selling.objects.get(Prop_id=et, status=sta)
                st = blk12.status
                if (d1['username'] != username and d1['status'] == "Pending" and st != "Buyed"):
                    se.append(d1)
            except:
                continue
        print("######selled:", se)
        if se == []:
            return HttpResponse("<script>alert('No Available Properties');window.location.href='/View_s/';</script>")
        else:
            if os.path.isdir("SHCS_app/static/"+"Ipfs"):
                shutil.rmtree("SHCS_app/static/"+"Ipfs")
                os.makedirs("SHCS_app/static/"+"Ipfs")
            else:
                os.makedirs("SHCS_app/static/"+"Ipfs")
            for j in se:
                d2 = j
                ss1 = d2['hash1']
                ss2 = d2['file_name']
                hashh.append(ss1)
                fname.append(ss2)
            for k in range(0, len(hashh)):
                ab = str(hashh[k])
                ab = ab.strip()
                api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
                api.get(ab)
                fn = str(fname[k])
                new_file = fn
                with open(ab, 'rb') as f1:
                    with open("SHCS_app/static/"+"Ipfs/"+new_file, 'wb') as f2:
                        f2.write(f1.read())
                os.remove("C:/Users/benba/Anaconda/Blockchain/Blockchain/"+ab)
            return render(request, 'Buy_p.html', {'Buy': se})
    else:
        ##########################################################################################
        img = []
        hsh = []

        username = request.session["username"]
        bkkl = Token.objects.filter(
            status="Pending").exclude(username=username)
        c3 = bkkl.count()
        if (c3 > 0):
            bkkl1 = Token.objects.filter(status="Pending").exclude(
                username=username).values('image', 'hashh')

            bkkl1 = list(bkkl1)
            print("bkkl1########:", bkkl1)
            ##########################################################################
            if os.path.isdir("SHCS_app/static/"+"Ipfs"):
                shutil.rmtree("SHCS_app/static/"+"Ipfs")
                os.makedirs("SHCS_app/static/"+"Ipfs")
            else:
                os.makedirs("SHCS_app/static/"+"Ipfs")
            for i in bkkl1:
                dc = i
                image = str(dc['image'])
                hashh = str(dc['hashh'])
                hashh = hashh.strip()
                #############################################################
                api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
                api.get(hashh)
                with open(hashh, 'rb') as f1:
                    with open("SHCS_app/static/"+"Ipfs/"+image, 'wb') as f2:
                        f2.write(f1.read())
                os.remove("C:/Users/benba/Anaconda/Blockchain/Blockchain/"+hashh)
            ################################################################
            ##########################################################################
            return render(request, 'Buy_p_tk.html', {'users': bkkl})
        else:
            return HttpResponse("<script>alert('No datas to show');window.location.href='/Buy/';</script>")
            ##########################################################################################


@never_cache
def Payment(request):
    if 'uid' in request.session:
        uname = request.POST.get('uname')
        ptype = request.POST.get('ptype')
        pid = request.POST.get('pid')
        details = request.POST.get('details')
        amount = request.POST.get('amount')
        mobile = request.POST.get('mobile')
        print('####:', uname, ptype, pid, details, amount, mobile)
        return render(request, 'payment.html', {'uname': uname, 'ptype': ptype, 'pid': pid, 'details': details, 'amount': amount, 'mobile': mobile})
    else:
        return render(request, 'login.html')


@never_cache
def Pay(request):
    if 'uid' in request.session:
        name = request.POST.get('name1')
        print(name)
        ptype = request.POST.get('ptype1')
        pid = request.POST.get('pid1')
        details = request.POST.get('details1')
        amount = request.POST.get('amount1')
        mobile = request.POST.get('mobile1')
        pvt = request.POST.get('pvt')
        uname = request.session["username"]
        blk2 = Users.objects.get(username=uname)
        paddr1 = blk2.p_address
        mb = blk2.mobile
        blk3 = Users.objects.get(username=name)
        paddr2 = blk3.p_address
        a = verify_key(paddr1, pvt)
        print(a)
        print(amount)
        status = "Buyed"
        if (a == "Yes"):
            t_hash = transfer(paddr1, paddr2, pvt, amount)
            print("#######", t_hash)
            obj21 = Transaction(SName=name, Saddr=paddr2, RName=uname,
                                Raddr=paddr1, P_id=pid, Amount=amount, T_hash=t_hash)
            obj21.save()
            obj22 = Selling.objects.get(Prop_id=pid)
            obj22.status = status
            im = obj22.image
            i_hash = obj22.hash1
            obj22.save()
            i_hash = str(obj22.hash1)
            obj55 = Buyed(name=uname, p_id=pid, hash1=i_hash,
                          p_type=ptype, im=im, details=details, phone=mb)
            obj55.save()
            ####################################
            obb1 = Selling.objects.get(Prop_id=pid)
            obb1.delete()
            ####################################
            ob = Transaction.objects.get(
                SName=name, Saddr=paddr2, RName=uname, Raddr=paddr1, P_id=pid, Amount=amount, T_hash=t_hash)
            get_id = ob.r_id1
            add_transaction_to_table(
                get_id, name, paddr2, uname, paddr1, pid, amount, t_hash)
            return HttpResponse("<script>alert('Payment Successful');window.location.href='/Transactin_tab/';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/Buy/';</script>")
    else:
        return render(request, 'login.html')


@never_cache
def Transactin_tab(request):
    if 'uid' in request.session:
        print(request.session['uid'])
        obj = get_transactions()
        print("##obj##:", obj)
        return render(request, 'view_tr_table.html', {'obj': obj})
    else:
        return render(request, 'login.html')


def buyprp_intro(request):
    if 'uid' in request.session:
        return render(request, 'buyprp_intro.html')
    else:
        return render(request, 'login.html')


def buyprp(request):
    if 'uid' in request.session:
        s_type = request.POST.get("Select")
        if (s_type == "Normal"):
            print(request.session['uid'])
            ima = []
            has = []
            namee = request.session["username"]
            req_list = Buyed.objects.filter(name=namee)
            c22 = req_list.count()
            print(c22)
            if (c22 == 0):
                return HttpResponse("<script>alert('No Bought Properties');window.location.href='/show_home_user/';</script>")
            else:
                for i in req_list:
                    im1 = i.im
                    h1 = i.hash1
                    ima.append(im1)
                    has.append(h1)
                print("ima#######:", ima)
                print("has#######:", has)
                if os.path.isdir("SHCS_app/static/"+"Ipfs"):
                    shutil.rmtree("SHCS_app/static/"+"Ipfs")
                    os.makedirs("SHCS_app/static/"+"Ipfs")
                else:
                    os.makedirs("SHCS_app/static/"+"Ipfs")
                for k in range(0, len(has)):
                    ab = str(has[k])
                    ab = ab.strip()
                    api = ipfshttpclient.connect(
                        '/ip4/127.0.0.1/tcp/5001/http')
                    api.get(ab)
                    fn = str(ima[k])
                    new_file = fn
                    with open(ab, 'rb') as f1:
                        with open("SHCS_app/static/"+"Ipfs/"+new_file, 'wb') as f2:
                            f2.write(f1.read())
                    os.remove(
                        "C:/Users/benba/Anaconda/Blockchain/Blockchain/"+ab)

                return render(request, 'buyprp.html', {'req': req_list})
        else:
            img = []
            hsh = []

            name = request.session["name"]
            bkkl = Buyed_tk.objects.filter(name=name)
            c3 = bkkl.count()
            if (c3 > 0):
                bkkl1 = Buyed_tk.objects.filter(
                    name=name).values('im', 'hash1')
                bkkl1 = list(bkkl1)
                print("bkkl1########:", bkkl1)
                ##########################################################################
                if os.path.isdir("SHCS_app/static/"+"Ipfs"):
                    shutil.rmtree("SHCS_app/static/"+"Ipfs")
                    os.makedirs("SHCS_app/static/"+"Ipfs")
                else:
                    os.makedirs("SHCS_app/static/"+"Ipfs")
                for i in bkkl1:
                    dc = i
                    image = str(dc['im'])
                    hashh = str(dc['hash1'])
                    hashh = hashh.strip()
                    #############################################################
                    api = ipfshttpclient.connect(
                        '/ip4/127.0.0.1/tcp/5001/http')
                    api.get(hashh)
                    with open(hashh, 'rb') as f1:
                        with open("SHCS_app/static/"+"Ipfs/"+image, 'wb') as f2:
                            f2.write(f1.read())
                    os.remove(
                        "C:/Users/benba/Anaconda/Blockchain/Blockchain/"+hashh)
                ################################################################
                ##########################################################################
                return render(request, 'buyprp_tk.html', {'req': bkkl})
            else:
                return HttpResponse("<script>alert('No Bought Properties');window.location.href='/show_home_user/';</script>")
    else:
        return render(request, 'login.html')


def sell_buyed(request):
    if 'uid' in request.session:
        namee = request.session["name"]
        uname = request.POST.get("name")
        pr_id = request.POST.get("pid")
        p_type = request.POST.get("ptype")
        hashhh = request.POST.get("hashh")
        details = request.POST.get("details")
        mbb = request.POST.get("mobile")
        imgg = request.POST.get("img")
        return render(request, 'Buyed_sell.html', {'name': namee, 'username': uname, 'pro_id': pr_id, 'pro_ty': p_type, 'hsh': hashhh, 'det': details, 'mobile': mbb, 'imgg': imgg})
    else:
        return render(request, 'login.html')

########################################################################################################
########################################################################################################


def sell_b_tk(request):
    if 'uid' in request.session:
        namee = request.session["name"]
        uname = request.POST.get("name")
        pr_id = request.POST.get("pid")
        p_type = request.POST.get("ptype")
        hashhh = request.POST.get("hashh")
        details = request.POST.get("details")
        mbb = request.POST.get("mobile")
        imgg = request.POST.get("img")
        return render(request, 'bs_token.html', {'name': namee, 'username': uname, 'pro_id': pr_id, 'pro_ty': p_type, 'hsh': hashhh, 'det': details, 'mobile': mbb, 'imgg': imgg})
    else:
        return render(request, 'login.html')
########################################################################################################
########################################################################################################


def b_selltk(request):
    global tk_idd
    tk_idd = tk_idd
    name = request.session["name"]
    username = request.session["username"]
    ptype = request.POST.get("ptype")
    p_id = request.POST.get("p_id")
    private = request.POST.get("pvt")
    details = request.POST.get("details")
    img = request.POST.get("image")
    amount = request.POST.get("amount")
    amount = int(amount)
    hashh = request.POST.get("hsh")
    mob = request.POST.get("mob")
    status = "Pending"
    obb = Users.objects.get(username=username)
    pb = obb.p_address
    phn = obb.mobile
    token = request.POST.get("token")
    token = int(token)
    button = "Buy"
    Cuholder = name
    pre = "-"
    amnt = float(amount/token)
    print(pb)
    a = verify_key(pb, private)
    print(a)
    obb = Users.objects.get(username=username)
    pb = obb.p_address
    phn = obb.mobile
    print(pb)
    a = verify_key(pb, private)
    print(a)
    if (a == "Yes"):
        ##########################################
        obj22 = Selling.objects.filter(Prop_id=p_id)
        c22 = obj22.count()
        print(c22)
        #########################################
        obj23 = Token.objects.filter(Prop_id=p_id)
        c23 = obj23.count()
        print(c23)
        ##########################################

        if (c22 == 0 and c23 == 0):
            for i in range(1, token+1):
                tk_idd = tk_idd+1
                tok_name = p_id+"__"+"token"+str(i)
                file_name11 = p_id+"__"+"token"+str(i)+".jpg"
                blk1 = Token(r_id1=tk_idd, Name=name, Ptype=ptype, Prop_id=p_id, details=details, tkname=tok_name, image=file_name11,
                             mobile=phn, amount=amnt, status=status, username=username, token_count=token, Cuholder=Cuholder, hashh=hashh, Button=button)
                blk1.save()
                ##################################################################################################################################################################################################################
                obj323 = Token.objects.get(tkname=tok_name)
                amn = str(obj323.amount)
                idd1 = int(obj323.r_id1)
                idd1 = int(idd1)
                print(type(idd1))
                print(idd1)
                ##################################################################################################################################################################################################################
                tkadd(idd1, ptype, p_id, tok_name, file_name11, amn,
                      Cuholder, hashh, username)  # to store tokens to blockchain
            ################################################################################################
            tk_id = str(tk_idd)
            f1 = open(
                'C:/Users/benba/Anaconda/Blockchain/Blockchain/tk_id.txt', 'w')
            f1.write(tk_id)
            f1.close()
            obb = Buyed.objects.get(p_id=p_id)
            obb.delete()
            ################################################################################################
            return HttpResponse("<script>alert('Successfully Added');window.location.href='/show_home_user/';</script>")
        else:
            return HttpResponse("<script>alert('Property ID is already existed');window.location.href='/buyprp/';</script>")
    else:
        return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/buyprp/';</script>")
########################################################################################################


def b_sell(request):
    global idd
    idd = idd+1
    name = request.session["name"]
    username = request.session["username"]
    ptype = request.POST.get("ptype")
    p_id = request.POST.get("p_id")
    private = request.POST.get("pvt")
    details = request.POST.get("details")
    img = request.POST.get("image")
    amount = request.POST.get("amount")
    hashh = request.POST.get("hsh")
    mob = request.POST.get("mob")
    status = "Pending"
    obb = Users.objects.get(username=username)
    pb = obb.p_address
    phn = obb.mobile
    print(pb)
    a = verify_key(pb, private)
    print(a)
    if (a == "Yes"):
        obj22 = Selling.objects.filter(Prop_id=p_id, status="Pending")
        c22 = obj22.count()
        print(c22)
        if (c22 == 0):
            ####################################
            try:
                obb1 = Selling.objects.get(Prop_id=p_id)
                obb1.delete()
            except:
                print("**")
            ####################################
            status = "Pending"
            obj11 = Selling(r_id1=idd, Name=name, Ptype=ptype, Prop_id=p_id, details=details,
                            image=img, mobile=mob, amount=amount, username=username, status=status, hash1=hashh)
            obj11.save()
            obj32 = Selling.objects.get(Prop_id=p_id, status="Pending")
            h = obj32.Prop_id
            us = obj32.r_id1
            us = int(us)
            print("#########:", us)
            print("Type :", type(h))
            add_prop(us, h, username, ptype, details,
                     img, amount, status, mob, hashh)
            obb = Buyed.objects.get(p_id=p_id)
            obb.delete()
            ###################################################################################
            se_id = str(idd)
            f1 = open(
                'C:/Users/benba/Anaconda/Blockchain/Blockchain/s_id.txt', 'w')
            f1.write(se_id)
            f1.close()
            ###################################################################################
            return HttpResponse("<script>alert('Successfully Added');window.location.href='/show_home_user/';</script>")
        else:
            return HttpResponse("<script>alert('Property ID is already existed');window.location.href='/buyprp/';</script>")
    else:
        return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/buyprp/';</script>")
#######################################################################################################################
##################################################################################################################
# ------------------------------------------------Token------------------------------------------------------------------#
#######################################################################################################################
#######################################################################################################################


@never_cache
def sell_token(request):
    global dd, tk_idd
    tk_idd = tk_idd
    dd = 1
    name = request.session["name"]
    username = request.session["username"]
    ptype = request.POST.get("Selecttt")
    p_id = request.POST.get("P_ID")
    private = request.POST.get("pvt")
    details = request.POST.get("details")
    amount = request.POST.get("amount")
    amount = int(amount)
    image = request.FILES["image"]
    token = request.POST.get("token")
    token = int(token)
    ####################################
    obb = Users.objects.get(username=username)
    phn = obb.mobile
    ####################################
    button = "Buy"
    Cuholder = name
    pre = "-"
    amnt = float(amount/token)
    ####################################
    status = "Pending"
    file_name1 = image.name
    file_name = p_id+".jpg"
    print("image:", file_name)
    print("###################################")
    api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    new_file = api.add("SHCS_app/Images/"+str(file_name1))
    print(new_file)
    hash1 = new_file.get('Hash')
    print("###########hash1:", hash1)
    ###########################################################################################

    hashh = []
    check = []
    username = request.session["username"]
    ab = get_prps()
    print("####val:", ab)
    print("######################")
    val = ab.values()
    print("####val:", val)
    print("######################")
    for i in val:
        d1 = i
        et = str(d1['hash1'])
        if (et == hash1):
            check = []
    ###########################################################################################

    if check != []:
        return HttpResponse("<script>alert('Try another property');window.location.href='/Sell_1/';</script>")
    else:
        obb = Users.objects.get(username=username)
        pb = obb.p_address
        phn = obb.mobile
        print(pb)
        a = verify_key(pb, private)
        print(a)
        if (a == "Yes"):
            ##########################################
            obj22 = Selling.objects.filter(Prop_id=p_id)
            c22 = obj22.count()
            print(c22)
            #########################################
            obj23 = Token.objects.filter(Prop_id=p_id)
            c23 = obj23.count()
            print(c23)
            ##########################################
            obj24 = Buyed.objects.filter(p_id=p_id)
            c24 = obj24.count()
            print(c24)
            #########################################
            if (c22 == 0 and c23 == 0 and c24 == 0):
                for i in range(1, token+1):
                    tk_idd = tk_idd+1
                    tok_name = p_id+"__"+"token"+str(i)
                    file_name11 = p_id+"__"+"token"+str(i)+".jpg"
                    blk1 = Token(r_id1=tk_idd, Name=name, Ptype=ptype, Prop_id=p_id, details=details, tkname=tok_name, image=file_name11,
                                 mobile=phn, amount=amnt, status=status, username=username, token_count=token, Cuholder=Cuholder, hashh=hash1, Button=button)
                    blk1.save()
                    ##################################################################################################################################################################################################################
                    obj323 = Token.objects.get(tkname=tok_name)
                    amn = str(obj323.amount)
                    idd1 = int(obj323.r_id1)
                    idd1 = int(idd1)
                    print(type(idd1))
                    print(idd1)
                    ##################################################################################################################################################################################################################
                    # to store tokens to blockchain
                    tkadd(idd1, ptype, p_id, tok_name, file_name11,
                          amn, Cuholder, hashh, username)
                ################################################################################################
                tk_id = str(tk_idd)
                f1 = open(
                    'C:/Users/benba/Anaconda/Blockchain/Blockchain/tk_id.txt', 'w')
                f1.write(tk_id)
                f1.close()
                ################################################################################################
                return HttpResponse("<script>alert('Successfully Added');window.location.href='/show_home_user/';</script>")
            else:
                return HttpResponse("<script>alert('Property ID is already existed');window.location.href='/Sell_1/';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/Sell_1/';</script>")


@never_cache
def Payment_tk(request):
    if 'uid' in request.session:
        cuname = request.POST.get('cuname')
        ptype = request.POST.get('ptype')
        pid = request.POST.get('pid')
        details = request.POST.get('details')
        amount = request.POST.get('amount')
        token = request.POST.get('token')
        mobile = request.POST.get('mobile')
        tkname = request.POST.get('tkname')
        hashh = request.POST.get('hsh')
        img = request.POST.get('img')
        return render(request, 'payment_token.html', {'cuname': cuname, 'ptype': ptype, 'pid': pid, 'details': details, 'amount': amount, 'mobile': mobile, 'tkname': tkname, 'hashh': hashh, 'img': img, 'tco': token})
    else:
        return render(request, 'login.html')


@never_cache
def pay_tk(request):
    if 'uid' in request.session:
        cuname = request.POST.get('cuname1')
        ptype = request.POST.get('ptype1')
        pid = request.POST.get('pid1')
        details = request.POST.get('details1')
        amount = request.POST.get('amount1')
        mobile = request.POST.get('mobile1')
        tkna = request.POST.get('tkname1')
        pvt = request.POST.get('pvt')
        hashh = request.POST.get('hash1')
        img = request.POST.get('img1')
        tco = request.POST.get('token_co')
        ######################################
        uname = request.session["username"]
        blk2 = Users.objects.get(username=uname)
        paddr1 = blk2.p_address
        nmr = blk2.name
        mb = blk2.mobile
        blk3 = Users.objects.get(name=cuname)
        paddr2 = blk3.p_address
        a = verify_key(paddr1, pvt)
        print(a)
        print(amount)
        if (a == "Yes"):
            t_hash = transfer(paddr1, paddr2, pvt, amount)
            print("#######", t_hash)
            obj21 = Transaction(SName=cuname, Saddr=paddr2, RName=nmr,
                                Raddr=paddr1, P_id=tkna, Amount=amount, T_hash=t_hash)
            obj21.save()
            obj22 = Token.objects.get(tkname=tkna)
            obj22.delete()
            ob = Transaction.objects.get(
                SName=cuname, Saddr=paddr2, RName=nmr, Raddr=paddr1, P_id=tkna, Amount=amount, T_hash=t_hash)
            get_id = ob.r_id1
            add_transaction_to_table(
                get_id, cuname, paddr2, nmr, paddr1, tkna, amount, t_hash)
            obj55 = Buyed_tk(name=nmr, p_id=pid, tk_name=tkna, hash1=hashh, p_type=ptype,
                             im=img, details=details, amnt=amount, phone=mb, tok_co=tco)
            obj55.save()
            return HttpResponse("<script>alert('Payment Successful');window.location.href='/Transactin_tab/';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/Buy/';</script>")
    else:
        return render(request, 'login.html')


@never_cache
def sell_buyed_tk(request):
    if 'uid' in request.session:
        namee = request.session["name"]
        uname = request.POST.get("name")
        pr_id = request.POST.get("pid")
        p_type = request.POST.get("ptype")
        hashhh = request.POST.get("hashh")
        details = request.POST.get("details")
        mbb = request.POST.get("mobile")
        img = request.POST.get("img")
        amount = request.POST.get("amount")
        tok_co = request.POST.get("tco")
        tk_nm = request.POST.get("tkname")
        return render(request, 'Buyed_sell_tk.html', {'name': namee, 'username': uname, 'pro_id': pr_id, 'pro_ty': p_type, 'hsh': hashhh, 'det': details, 'mobile': mbb, 'imgg': img, 'amount': amount, 'tok_co': tok_co, 'tk_nm': tk_nm})
    else:
        return render(request, 'login.html')


@never_cache
def b_sell_tk(request):
    global tk_idd
    if 'uid' in request.session:
        tk_idd = tk_idd+1
        status = "Pending"
        button = "Buy"
        namee = request.session["name"]
        uname = request.session["username"]
        pr_id = request.POST.get("p_id")
        p_type = request.POST.get("ptype")
        hashhh = request.POST.get("hsh")
        details = request.POST.get("details")
        mbb = request.POST.get("mob")
        img = request.POST.get("image")
        amount = request.POST.get("amnt")
        tok_co = request.POST.get("tokco")
        tk_nm = request.POST.get("tkname")
        pvt = request.POST.get("pvt")
        obb1 = Users.objects.get(username=uname)
        pb = obb1.p_address
        print(pb)
        a = verify_key(pb, pvt)
        print(a)
        if (a == "Yes"):
            blk1 = Token(r_id1=tk_idd, Name=namee, Ptype=p_type, Prop_id=pr_id, details=details, tkname=tk_nm, image=img, mobile=mbb,
                         amount=amount, status=status, username=uname, token_count=tok_co, Cuholder=namee, hashh=hashhh, Button=button)
            blk1.save()
            ##################################################################################################################################################################################################################
            obj323 = Token.objects.get(tkname=tk_nm)
            amn = str(obj323.amount)
            idd1 = int(obj323.r_id1)
            idd1 = int(idd1)
            print(type(idd1))
            print(idd1)
            ##################################################################################################################################################################################################################
            tkadd(idd1, p_type, pr_id, tk_nm, img, amount, namee,
                  hashhh, uname)  # to store tokens to blockchain
            obb22 = Buyed_tk.objects.get(tk_name=tk_nm)
            obb22.delete()
            ################################################################################################
            tk_id = str(tk_idd)
            f1 = open(
                'C:/Users/benba/Anaconda/Blockchain/Blockchain/tk_id.txt', 'w')
            f1.write(tk_id)
            f1.close()
            ################################################################################################
            return HttpResponse("<script>alert('Successfully Added');window.location.href='/show_home_user/';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/Sell_1/';</script>")
    else:
        return render(request, 'login.html')


def sell_buyed_asset_tk(request):
    if 'uid' in request.session:
        uname = request.session["username"]
        name = request.session["name"]
        tok_co = request.POST.get("tco")
        p_id = request.POST.get("pid")
        ptype = request.POST.get("ptype")
        details = request.POST.get("details")
        mobile = request.POST.get("mobile")
        hashh = request.POST.get("hashh")
        print("###tok_co###:", tok_co)
        img = p_id+".jpg"
        obj22 = Buyed_tk.objects.filter(p_id=p_id)
        c22 = obj22.count()
        print(c22)
        c22 = int(c22)
        tok_co = int(tok_co)
        if (tok_co == c22):
            return render(request, 'Buyed_sell_asset_tk.html', {'name': name, 'username': uname, 'pro_id': p_id, 'pro_ty': ptype, 'hsh': hashh, 'det': details, 'mobile': mobile, 'imgg': img})
        else:
            return HttpResponse("<script>alert('User does not contain full tokens');window.location.href='/buyprp_intro/';</script>")

    else:
        return render(request, 'login.html')


@never_cache
def b_sell_tk_asset(request):
    global idd
    idd = idd+1
    print("###idd###:", idd)
    uname = request.session["username"]
    name = request.session["name"]
    p_id = request.POST.get("p_id")
    ptype = request.POST.get("ptype")
    details = request.POST.get("details")
    mobile = request.POST.get("mob")
    hashh = request.POST.get("hsh")
    img = request.POST.get("image")
    private = request.POST.get("pvt")
    amount = request.POST.get("amount")
    ######################################
    try:
        Buyed_tk.objects.filter(p_id=p_id).delete()
    except:
        print("**")
    status = "Pending"
    obb = Users.objects.get(username=uname)
    pb = obb.p_address
    phn = obb.mobile
    print(pb)
    a = verify_key(pb, private)
    print(a)
    if (a == "Yes"):
        obj22 = Selling.objects.filter(Prop_id=p_id, status="Pending")
        c22 = obj22.count()
        print(c22)
        if (c22 == 0):
            ####################################
            try:
                obb1 = Selling.objects.get(Prop_id=p_id)
                obb1.delete()
            except:
                print("**")
            ####################################
            obj11 = Selling(r_id1=idd, Name=name, Ptype=ptype, Prop_id=p_id, details=details,
                            image=img, mobile=mobile, amount=amount, username=uname, status=status, hash1=hashh)
            obj11.save()
            obj32 = Selling.objects.get(Prop_id=p_id, status="Pending")
            h = obj32.Prop_id
            us = obj32.r_id1
            us = int(us)
            print("#########:", us)
            print("Type :", type(h))
            add_prop(us, h, uname, ptype, details, img,
                     amount, status, mobile, hashh)
            ###################################################################################
            se_id = str(idd)
            f1 = open(
                'C:/Users/benba/Anaconda/Blockchain/Blockchain/s_id.txt', 'w')
            f1.write(se_id)
            f1.close()
            ###################################################################################
            return HttpResponse("<script>alert('Successfully Added');window.location.href='/show_home_user/';</script>")
        else:
            return HttpResponse("<script>alert('Property ID is already existed');window.location.href='/buyprp_intro/';</script>")
    else:
        return HttpResponse("<script>alert('Invalid Private Key');window.location.href='/buyprp_intro/';</script>")
