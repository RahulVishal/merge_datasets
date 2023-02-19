from django.shortcuts import render,HttpResponse
import pandas as pd

# Create your views here.
def index(request):
    context={
        'variable':"this is not sent"
    }    
    return render(request,'index.html',context)
def new(request):
    return render(request,'new.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contacts(request):
    return render(request,'contact.html')
def checkbox(request):
    return render(request,'checkbox.html')
def import_file(request):
    return render(request,'import_file.html')
#def one_to_one_inner(request):
    #if request.method == 'POST':
        #csv_file1 = request.FILES['csv_file1']
        #csv_file2 = request.FILES['csv_file2']
        #df1 = pd.read_csv(csv_file1)
        #df2 = pd.read_csv(csv_file2)

        # perform the merge operation
        #df_merged = pd.merge(df1, df2, on='column_name', how='inner')
    #return render(request, 'import_file.html')

def merge_datasets(request):
    if request.method == 'POST':
        csv_file1 = request.FILES.get('csv_file1')
        csv_file2 = request.FILES.get('csv_file2')
        merge_type = request.POST.get('merge_type')
        
        df1 = pd.read_csv(csv_file1)
        df2 = pd.read_csv(csv_file2)

        if merge_type == 'inner':
            df_merged = pd.merge(df1, df2, how='inner')
        elif merge_type == 'left':
            df_merged = pd.merge(df1, df2, how='left')
        elif merge_type == 'right':
            df_merged = pd.merge(df1, df2, how='right')
        elif merge_type == 'outer':
            df_merged = pd.merge(df1, df2, how='outer')
        else:
            return render(request, 'final.html')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="merged_dataset.csv"'
        df_merged.to_csv(response, index=False)
        return response
        
    return render(request, 'final.html')

def download_merged_dataset(request):
    response = request.session.get('response')
    return response

def display_dataset(request):
    
    df = pd.read_csv('/merged_dataset.csv')
    context = {'data': df.to_html()}
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="merged_dataset.csv"'
    df.to_csv(path_or_buffer=response, index=False)
    return render(request, 'display_dataset.html', context), response

            