from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def done(request, op=None):
    msg = {}
    if op == 'logout':
        msg['title'] = '로그아웃'
        msg['msg'] = '로그아웃 되었습니다.'
        msg['url'] = 'index'
    elif op == 'signup1':
        msg['title'] = '회원가입'
        msg['msg'] = '회원가입 되었습니다.'
        msg['submsg'] = '자전거를 타고 RC코인을 받아보세요.'
        msg['url'] = 'index'
    elif op == 'signup2':
        msg['title'] = '회원가입'
        msg['msg'] = '회원가입 되었습니다.'
        msg['submsg'] = ['첫 방문 기념 3,000RC이 지급 되었습니다.', '자전거를 타고 RC코인을 더 받아보세요.']
        msg['url'] = 'index'
    elif op == 'signup3':
        msg['title'] = '회원가입'
        msg['msg'] = '회원가입에 실패했습니다.'
        msg['submsg'] = '관리자에게 문의하세요.'
        msg['url'] = 'index'
    elif op == 'remittance1':
        msg['title'] = '계좌관리'
        msg['msg'] = '송금완료.'
        msg['url'] = 'wallet:info'
    elif op == 'remittance2':
        msg['title'] = '계좌관리'
        msg['msg'] = '송금실패!!'
        msg['submsg'] = '송금을 실패했습니다. 다시 시도하세요.'
        msg['url'] = 'wallet:info'
    elif op == 'payment1':
        msg['title'] = '계좌관리'
        msg['msg'] = '결제완료.'
        msg['url'] = 'wallet:info'
    elif op == 'payment2':
        msg['title'] = '계좌관리'
        msg['msg'] = '결제실패!!'
        msg['submsg'] = '결제를 실패했습니다. 다시 시도하세요.'
        msg['url'] = 'wallet:info'
    elif op == 'cancel1':
        msg['title'] = '가맹점 관리'
        msg['msg'] = '결제가 취소되었습니다.'
        msg['url'] = 'store:info'
    elif op == 'cancel2':
        msg['title'] = '가맹점 관리'
        msg['subtitle'] = '결제취소'
        msg['submsg'] = '결제취소를 실패했습니다. 다시 시도하세요.'
        msg['url'] = 'store:info'
    elif op == 'store1':
        msg['title'] = '가맹점 관리'
        msg['msg'] = '가맹점이 삭제되었습니다.'
        msg['url'] = 'index'
    elif op == 'store2':
        msg['title'] = '가맹점 관리'
        msg['msg'] = '가맹점 삭제를 실패했습니다.'
        msg['url'] = 'store:info'
    return render(request, 'done.html', dict(msg=msg))

# 소개 페이지
def intro(request):
    template = loader.get_template('intro.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

# 이용안내 페이지
def guide(request):
    template = loader.get_template('guide.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

# 오시는길 페이지
def map(request):
    template = loader.get_template('map.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

# check logged user
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
