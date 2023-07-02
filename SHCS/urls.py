"""SHCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from SHCS_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # login & registration start
    path('',show_index),
    path('show_register/', show_register, name="show_register"), 
    path('register/', register, name="register"), 
    path('show_index/', show_index, name="show_index"), 
    path('check_login/', check_login, name="check_login"), 
    path('logout/', logout, name="logout"), 
    # login & registration end

    #For Price Predictor
    path('predict/', predict, name="predict"),
    path('predict/result/', predict_result,name="predict_result"),
    path('show_price_predictor/',show_price_predictor,name="show_price_predictor"), #to show the user home page

    path('show_home_admin/',show_home_admin,name="show_home_admin"), 
    path('show_request_admin/',show_request_admin,name="show_request_admin"), 
    path('show_user_admin/',show_user_admin,name="show_user_admin"), 
    path('show_home_user/',show_home_user,name="show_home_user"), 
    path('sell_intro/',sell_intro,name="sell_intro"), #intro page of sell property where we can select type(normal or token)
    path('Sell/',Sell,name="Sell"), #shows the properties sell page (normal/token) 
    path('approve/',approve,name="approve"), 
    path('reject/',reject,name="reject"), 
    path('sell/',sell,name="sell"),  #sell normal
    path('View_s/',View_s,name="View_s"),  #view sold properties
    path('View_selled/',View_selled,name="View_selled"), #read properties from blockchain
    path('Buy/',Buy,name="Buy"), 
    path('Buy_p/',Buy_p,name="Buy_p"), 
    path('Payment/',Payment,name="Payment"), #payment page(Normal)
    path('Pay/',Pay,name="Pay"), #Payment part
    path('Transactin_tab/',Transactin_tab,name="Transactin_tab"), 
    path('buyprp_intro/',buyprp_intro,name="buyprp_intro"), 
    path('buyprp/',buyprp,name="buyprp"),  
    path('sell_buyed/',sell_buyed,name="sell_buyed"), # page to sell bought prp
    path('b_sell/',b_sell,name="b_sell"), #sell property and add to blockchain
    ##################################################################################################################
    #Token
    ##################################################################################################################
    path('sell_token/',sell_token,name="sell_token"), #sell token properties
    path('Sell_1/',Sell_1,name="Sell_1"), #sell page (normal/token)
    path('Payment_tk/',Payment_tk,name="Payment_tk"), 
    path('pay_tk/',pay_tk,name="pay_tk"), 
    path('sell_buyed_tk/',sell_buyed_tk,name="sell_buyed_tk"), #sell bought token property
    path('b_sell_tk/',b_sell_tk,name="b_sell_tk"), 
    path('sell_buyed_asset_tk/',sell_buyed_asset_tk,name="sell_buyed_asset_tk"), #sell as normal asset
    path('b_sell_tk_asset/',b_sell_tk_asset,name="b_sell_tk_asset"), 
    path('sell_b_tk/',sell_b_tk,name="sell_b_tk"), #Sell normal bought as token
    path('b_selltk/',b_selltk,name="b_selltk"), 
]
