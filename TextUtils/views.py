#This file was created by me - Sweekrit Dash

# This file was created by Sweekrit Dash

from django.shortcuts import HttpResponse, render

def index(request):
    return render(request, 'inde.html')

def analyze(request):
    # Get The Text
    # print(request.GET.get('text','default')) # to print the text in the terminal
    
    removepunc = request.POST.get('removepunc', 'off')
    removeline = request.POST.get('removeline', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')
    count=0
    djtext = request.POST.get('text', 'default')
    analyze = ""

    if removepunc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyze += char
        params = {'purpose': 'Remove Punctuation', 'analyze': analyze,'type':'str'}
        # Analyze The Text
        return render(request, 'result.html', params)
    #To Remove new line
    elif removeline == 'on':
        for char in djtext:
            if char != '\n':
                analyze += char
        params = {'purpose': 'Remove Line', 'analyze': analyze,'type':'str'}
        # Analyze The Text
        return render(request, 'result.html', params)
    #To Remove extra space
    elif extraspace == 'on':
        for i,char in enumerate(djtext):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                analyze += char
        params = {'purpose': 'Remove space','analyze': analyze,'type':'str'}
        # Analyze The Text
        return render(request, 'result.html', params)
    #To count the characters.
    elif charcount == 'on':
        for i,char in enumerate(djtext):
            if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122):
                count+=1
        params = {'purpose': 'Character count','analyze': count,'type':'int'}
        # Analyze The Text
        return render(request, 'result.html', params)
    else:
        params = {'purpose': 'Checkbox not selected', 'analyze': 'No data found'}
        return render(request, 'result.html', params)




