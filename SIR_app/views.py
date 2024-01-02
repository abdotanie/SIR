from django.shortcuts import render
from .BooleanModel import show
from .ExtentedBooleanModel import show_a
from .VectorsModel import show_b
from .read_word import read_doc_file
import os


def home(request):
    search_results = []
    content = ''

    if request.method == 'POST':
        search_input = request.POST.get('search-input', '')
        search_option = request.POST.get('select-option')

        if search_input:
            if search_option == 'Boolean Model':
                search_results_str = show(search_input)
            elif search_option == 'Extended Boolean':
                search_results_str = show_a(search_input)
            elif search_option == 'Vector Model':
                search_results_str = show_b(search_input)
            else:
                pass
                

            # Split the string into a list using ',' as the separator
            search_results = search_results_str.split(',')
          
            content=read_doc_file(search_results[0])
           
            
    return render(request, 'index.html', {'search_results': search_results, 'CONT': content})
