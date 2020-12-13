from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages

def ffem(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def ffec(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def ffemh(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def ffcp(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fsem(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fsep(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fseg(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fscs(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def stem(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def stdm(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def stds(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def stca(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def sfda(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def sfps(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def sfos(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def sfpd(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tfds(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tftc(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tfml(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tfcl(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tscd(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tscn(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tsai(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def tsiot(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fsvse(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fsvds(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fsvcc(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fsvbt(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fegdp(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def fegcn(request):
    if request.method == "POST":
        que = request.POST['q1']
        op1 = request.POST['o11']
        op2 = request.POST['o12']
        op3 = request.POST['o13']
        op4 = request.POST['o14']
        ans = request.POST['a1']
        category = request.POST['c1']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q2']
        op1 = request.POST['o21']
        op2 = request.POST['o22']
        op3 = request.POST['o23']
        op4 = request.POST['o24']
        ans = request.POST['a2']
        category = request.POST['c2']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q3']
        op1 = request.POST['o31']
        op2 = request.POST['o32']
        op3 = request.POST['o33']
        op4 = request.POST['o34']
        ans = request.POST['a3']
        category = request.POST['c3']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q4']
        op1 = request.POST['o41']
        op2 = request.POST['o42']
        op3 = request.POST['o43']
        op4 = request.POST['o44']
        ans = request.POST['a4']
        category = request.POST['c4']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q5']
        op1 = request.POST['o51']
        op2 = request.POST['o52']
        op3 = request.POST['o53']
        op4 = request.POST['o54']
        ans = request.POST['a5']
        category = request.POST['c5']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q6']
        op1 = request.POST['o61']
        op2 = request.POST['o62']
        op3 = request.POST['o63']
        op4 = request.POST['o64']
        ans = request.POST['a6']
        category = request.POST['c6']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q7']
        op1 = request.POST['o71']
        op2 = request.POST['o72']
        op3 = request.POST['o73']
        op4 = request.POST['o74']
        ans = request.POST['a7']
        category = request.POST['c7']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q8']
        op1 = request.POST['o81']
        op2 = request.POST['o82']
        op3 = request.POST['o83']
        op4 = request.POST['o84']
        ans = request.POST['a8']
        category = request.POST['c8']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q9']
        op1 = request.POST['o91']
        op2 = request.POST['o92']
        op3 = request.POST['o93']
        op4 = request.POST['o94']
        ans = request.POST['a9']
        category = request.POST['c9']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q10']
        op1 = request.POST['o101']
        op2 = request.POST['o102']
        op3 = request.POST['o103']
        op4 = request.POST['o104']
        ans = request.POST['a10']
        category = request.POST['c10']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q11']
        op1 = request.POST['o111']
        op2 = request.POST['o112']
        op3 = request.POST['o113']
        op4 = request.POST['o114']
        ans = request.POST['a11']
        category = request.POST['c11']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q12']
        op1 = request.POST['o121']
        op2 = request.POST['o122']
        op3 = request.POST['o123']
        op4 = request.POST['o124']
        ans = request.POST['a12']
        category = request.POST['c12']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q13']
        op1 = request.POST['o131']
        op2 = request.POST['o132']
        op3 = request.POST['o133']
        op4 = request.POST['o134']
        ans = request.POST['a13']
        category = request.POST['c13']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q14']
        op1 = request.POST['o141']
        op2 = request.POST['o142']
        op3 = request.POST['o143']
        op4 = request.POST['o144']
        ans = request.POST['a14']
        category = request.POST['c14']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
        que = request.POST['q15']
        op1 = request.POST['o151']
        op2 = request.POST['o152']
        op3 = request.POST['o153']
        op4 = request.POST['o154']
        ans = request.POST['a15']
        category = request.POST['c15']
        f = dffem(que=que,op1=op1,op2=op2,op3=op3,op4=op4,category=category,ans=ans)
        f.save()
    return render(request,'sub/ffem.html')

def exam(request):
    a = dffem.objects.all()
    return render(request,'student/exam.html',{'a':a});