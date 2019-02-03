from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def done(request, op=None):
    msg = {}
    if op == 'logout':
        msg['title'] = '로그아웃'
        msg['subtitle'] = '로그아웃'
        msg['msg'] = '로그아웃 되었습니다.'
        msg['url'] = 'index'
    elif op == 'signup1':
        msg['title'] = '회원가입'
        msg['subtitle'] = '회원가입 완료'
        msg['msg'] = '회원가입 되었습니다.'
        msg['submsg'] = '자전거를 타고 RC코인을 받아보세요.'
        msg['url'] = 'index'
    elif op == 'signup2':
        msg['title'] = '회원가입'
        msg['subtitle'] = '회원가입 완료'
        msg['msg'] = '첫 방문 기념 3,000RC 지급'
        msg['submsg'] = '자전거를 타고 RC코인을 받아보세요.'
        msg['url'] = 'index'
    elif op == 'signup3':
        msg['title'] = '회원가입'
        msg['subtitle'] = '회원가입 실패'
        msg['msg'] = '회원가입에 실패했습니다.'
        msg['submsg'] = '관리자에게 문의하세요.'
        msg['url'] = 'index'
    elif op == 'remittance1':
        msg['title'] = '계좌관리'
        msg['subtitle'] = '송금'
        msg['msg'] = '송금완료.'
        msg['url'] = 'wallet:info'
    elif op == 'remittance2':
        msg['title'] = '계좌관리'
        msg['subtitle'] = '송금'
        msg['msg'] = '송금실패!!'
        msg['submsg'] = '송금을 실패했습니다. 다시 시도하세요.'
        msg['url'] = 'wallet:info'
    elif op == 'payment1':
        msg['title'] = '계좌관리'
        msg['subtitle'] = '결제'
        msg['msg'] = '결제완료.'
        msg['url'] = 'wallet:info'
    elif op == 'payment2':
        msg['title'] = '계좌관리'
        msg['subtitle'] = '결제'
        msg['msg'] = '결제실패!!'
        msg['submsg'] = '결제를 실패했습니다. 다시 시도하세요.'
        msg['url'] = 'wallet:info'
    elif op == 'cancel1':
        msg['title'] = '가맹점 관리'
        msg['subtitle'] = '결제취소'
        msg['msg'] = '결제가 취소되었습니다.'
        msg['url'] = 'store:info'
    elif op == 'cancel2':
        msg['title'] = '가맹점 관리'
        msg['subtitle'] = '결제취소'
        msg['msg'] = '결제취소에 실패했습니다.'
        msg['submsg'] = '결제취소에 실패했습니다. 다시 시도하세요.'
        msg['url'] = 'store:info'
    elif op == 'store1':
        msg['title'] = '가맹점 관리'
        msg['subtitle'] = '가맹점 삭제'
        msg['msg'] = '가맹점이 삭제되었습니다.'
        msg['url'] = 'index'
    elif op == 'store2':
        msg['title'] = '가맹점 관리'
        msg['subtitle'] = '가맹점 삭제'
        msg['msg'] = '가맹점이 삭제에 실패했습니다.'
        msg['url'] = 'store:info'
    return render(request, 'done.html', dict(msg=msg))