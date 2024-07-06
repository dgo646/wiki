from django.shortcuts import render
from . import util
from .import form
import secrets
import markdown

def ret_dic():
    dic={
        "list":'',"page":'',"form_s":'',"form_n":'',"Title_principal":'',"subtitle":'',
        "edit":''
    }
    return dic

def index(request):
    ret_dicc = ret_dic()
    list_source = util.list_entries()

    if request.method == "POST":
        form_vacio = form.forms_se(request.POST)
        form_search = request.POST['form_search']

        form_search_list = util.get_entry(form_search)
        if form_search_list == None:
            coincidence_list_print = []                
            for i in range(len(list_source)):
                coincidence_list = list_source[i].find(form_search)
                if coincidence_list != -1:
                    coincidence_list_print.append(list_source[i])

            if len(coincidence_list_print) == 0:
                ret_dicc["Title_principal"]='Not_Found'
                ret_dicc["form_s"] = form_vacio

                return render(request, "encyclopedia/index.html", ret_dicc) 
            else:
                ret_dicc["Title_principal"]='Titles related to search'
                ret_dicc["form_s"] = form_vacio
                ret_dicc["list"] = coincidence_list_print

                return render(request, "encyclopedia/index.html", ret_dicc)
        else:
            ret_dicc["Title_principal"]='Search Result'
            ret_dicc["form_s"] = form_vacio
            ret_dicc["list"] = list_source
            ret_dicc["page"] = markdown.markdown(util.get_entry(form_search))


            return render(request, "encyclopedia/index.html",ret_dicc)
    else:
        form_vacio = form.forms_se()
        form_search = ""                    #Necesario limpiar si es GET
        ret_dicc["Title_principal"]='All Pages'
        ret_dicc["form_s"] = form_vacio
        ret_dicc["list"] = list_source   

        return render(request, "encyclopedia/index.html",ret_dicc)


def new_page(request):
    flag = 0
    ret_dicc = ret_dic()
    if request.method == "POST":
        form_vacio = form.forms_np(request.POST)
        form_title = request.POST['form_title']
        form_descr = request.POST['form_description']
        
        
        for i in range(len(util.list_entries())):
            if util.list_entries()[i] == form_title:
                flag = flag + 1

        if flag==0:
            util.save_entry(form_title, form_descr)
            form_vacio = ''
            ret_dicc["page"] = markdown.markdown(util.get_entry(form_title))
        else:
            
            ret_dicc["Subtitle"]='Page existent in the source'
            form_vacio = ''  
    else:
        form_vacio = form.forms_np()
        form_title = "" 
        form_descr = ""
    
    ret_dicc["Title_principal"]='New Page'
    ret_dicc["form_n"] = form_vacio       
    return render(request, "encyclopedia/new_page.html",ret_dicc)
     

def random_page(request):
    ret_dicc = ret_dic()
    ret_dicc["page"] = markdown.markdown(util.get_entry(secrets.choice(util.list_entries())))
    ret_dicc["Title_principal"] = 'Random Page'
    return render(request, "encyclopedia/index.html",ret_dicc)


def detail(request, question_id):
    search_get = util.get_entry(question_id)
    if search_get==None:
        search_get = ''

    ret_dicc = ret_dic()
    ret_dicc["form_s"] = form.forms_se()
    ret_dicc["list_n"] = util.list_entries() 
    ret_dicc["page"] = markdown.markdown(search_get)
    ret_dicc["edit"]='edit_page'
    return render(request, "encyclopedia/index.html",ret_dicc)


def edit_page(request,question_id):
    ret_dicc = ret_dic()
    search_get = util.get_entry(question_id)
    if request.method == "POST":
        form_vacio = form.forms_np(request.POST)
        form_title = request.POST['form_title']
        form_descr = request.POST['form_description']

        util.save_entry(form_title, form_descr)
        form_vacio = ''
        ret_dicc["page"] = markdown.markdown(util.get_entry(form_title))
        ret_dicc["edit"]='edit_page'

    else:
        form_vacio = form.forms_np(initial={"form_title":question_id,"form_description":search_get})
        form_title = "" 
        form_descr = ""    
    print(question_id)
    ret_dicc["Title_principal"]='Edit_Page'      
    ret_dicc["form_n"] = form_vacio
    return render(request, "encyclopedia/new_page.html",ret_dicc)     