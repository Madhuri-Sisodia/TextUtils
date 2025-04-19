from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyser(request):
    text = request.POST.get('text', 'default') 
    punctuation= request.POST.get('punctuation', 'off')   
    uppercase = request.POST.get('uppercase', 'off')  
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off') 
    
    if (punctuation != "on" and uppercase != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error: Please select at least one option.")
    
    if punctuation == "on":
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed_data = ""
        for char in text:
            if char not in Punctuations:
                analysed_data += char
        text = analysed_data

        
    if uppercase == "on":
        analysed_data=""
        for char in text:
            analysed_data += char.upper()
        text = analysed_data
            
            
      
    if newlineremover == "on":
        analysed_data=""
        for char in text:
               if char != '\n' and char != '\r':
                 analysed_data += char
        text = analysed_data
            
            
    if extraspaceremover == "on": 
       analysed_data = " ".join(text.split())
    text = analysed_data
      
   
    return render(request, 'analyser.html', {
                'purpose': 'Coverted into Upper Case',
                'analyse': analysed_data
                        })
