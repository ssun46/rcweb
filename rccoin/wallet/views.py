from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests, json, datetime

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
        'balance' : res['value']
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
@login_required
def remittance(request):
    if request.method == 'POST':
        # 송금로직
        pass
    # 송금위한 잔액 전송
    return render(request, 'wallet/remittance.html', {})

# 결제
@login_required
def payment(request):
    if request.method == 'POST':
        # 결제로직
        pass
    return render(request, 'wallet/payment.html', {})