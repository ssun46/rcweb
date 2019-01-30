from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# wallet 정보 획득
@login_required
def read_wallet(request):
    return render(request, 'wallet/read_wallet.html', {})