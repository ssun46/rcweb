from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from time import sleep
import requests, json, datetime
from store.models import Store

# Create your views here.

host = 'http://210.107.78.166:3000/'

# wallet 정보 획득
@login_required
def read_wallet(request):
    user = get_object_or_404(User, pk=request.user.pk)
    url = host + 'get_account'
    params = {'user_id' : user.username}
    response = requests.get(url, params=params)
    res = response.json()
    data = {
        'balance' : '{:,}'.format(int(res['value']))
    }
    return render(request, 'wallet/read_wallet.html', data)

# RC코인 발행
@csrf_exempt
@login_required
def publish(request):
    if request.method == 'POST':
        toId = request.POST.get('userid') 
        amount = request.POST.get('amount')
        today = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        url = host + 'publish'
        data = {
            'user_id'   : toId, 
            'from_id'   : 'admin',
            'amount'    : amount,
            'date'      : today
        }
        data_json = json.dumps(data)
        param_data = { 'param_data' : data_json }
        response = requests.post(url, params=param_data, headers=headers)
        data = {
            'res' : response.status_code
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json;charset=UTF-8')
    return render(request,'wallet/publish.html')

# 송금
@csrf_exempt
@login_required
def remittance(request):
    if request.method == 'POST':
        # 송금로직
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        fromId = request.user.username
        toId = request.POST.get("target") 
        amount = (request.POST.get("point")).replace(',', '')
        today = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        url = host + 'transfer'
        data = {
            'from_id'   : fromId, 
            'to_id'     : toId,
            'amount'    : amount,
            'type'      : '5',
            'date'      : today
        }
        param_data = { 'param_data' : json.dumps(data) }
        response = requests.post(url, params=param_data, headers=headers)
        res = response.json()
        # 송금 성공 처리
        sleep(2)
        return redirect('wallet:info')
    
    # 송금위한 잔액 전송
    user = get_object_or_404(User, pk=request.user.pk)
    url = host + 'get_account'
    params = {'user_id' : user.username}
    response = requests.get(url, params=params)
    res = response.json()
    data = {
        'balance' : '{:,}'.format(int(res['value']))
    }
    return render(request, 'wallet/remittance.html', data)

# 결제
@csrf_exempt
@login_required
def payment(request):
    if request.method == 'POST':
        # 결제로직
        pass
    return render(request, 'wallet/payment.html', {})

# 결제 히스토리
@login_required
def get_history(request):
    fro = request.GET.get('fro',None)
    this_page_num = request.GET.get('this_page',None)
    query_type = request.GET.get('type', 1)
    url = host + "get_txList"
    params = {'user_id' : fro}
    response = requests.get(url, params=params)
    res = response.json()
    res.reverse()

    filtered_list = []
    # 송금 (txType:5,6,7,8)
    if query_type == '2' :
        for x in res :
            if x["txType"] == '5' or x["txType"] == '6' or x["txType"] == '7' or x["txType"] == '8':
                filtered_list.append(x)
    # 결제 (txType:1,2,3,4)
    elif query_type == '3':
        for x in res :
            if x["txType"] =='1' or x["txType"] =='2' or x["txType"] =='3' or x["txType"] =='4':
                filtered_list.append(x)
    # 발행 (txType:0)
    elif query_type == '1':
        for x in res :
            if x["txType"] =='0':
                filtered_list.append(x)
    elif query_type == '0':
        filtered_list = res

    history_list = []
    page_size = 10
    p = Paginator(filtered_list, page_size)

    for history in p.page(this_page_num):
        s_name = history['trader']
        if history['txType'] == '1':
            user = get_object_or_404(User, username=history['trader'])
            store = Store.objects.filter(Q(representative=user.id) & ~Q(status='d'))
            s_name = store[0].name
        temp = {
            'balance':history["balance"],
            'trader':s_name,
            'amount':history["amount"],
            'txType':history["txType"],
            'date':history["date"]
        }
        history_list.append(temp)

    start_seq = p.count - (page_size * (int(this_page_num) - 1))
    data = {
        'start_seq' : start_seq,
        'history_list' : history_list,
        'current_page_num' : this_page_num,
        'max_page_num' : p.num_pages,
        'fullLength' : start_seq
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json;charset=UTF-8")
