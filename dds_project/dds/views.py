from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction, Status, Type, Category, Subcategory
from .forms import TransactionForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse

def transaction_list(request):
    transactions = Transaction.objects.all()

    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    status_id = request.GET.get('status')
    type_id = request.GET.get('type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')

    if date_from:
        transactions = transactions.filter(date__gte=date_from)
    if date_to:
        transactions = transactions.filter(date__lte=date_to)
    if status_id:
        transactions = transactions.filter(status_id=status_id)
    if type_id:
        transactions = transactions.filter(type_id=type_id)
    if category_id:
        transactions = transactions.filter(category_id=category_id)
    if subcategory_id:
        transactions = transactions.filter(subcategory_id=subcategory_id)

    context = {
        'transactions': transactions,
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
        'request': request
    }
    return render(request, 'dds/transaction_list.html', context)


def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
        form.fields['date'].initial = timezone.localdate()

    return render(request, 'dds/transaction_form.html', {'form': form})


def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'dds/transaction_form.html', {'form': form})



def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'dds/transaction_confirm_delete.html', {'transaction': transaction})



def load_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).all()
    return JsonResponse(list(categories.values('id', 'name')), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).all()
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)




# для справочников

def status_list(request):
    statuses = Status.objects.all()
    return render(request, 'dds/dictionary_management.html', {'statuses': statuses})

def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dictionary_management')
    else:
        form = StatusForm()
    return render(request, 'dds/status_form.html', {'form': form})

def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('dictionary_management')
    else:
        form = StatusForm(instance=status)
    return render(request, 'dds/status_form.html', {'form': form})

def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('dictionary_management')
    return render(request, 'dds/status_confirm_delete.html', {'status': status})



def type_list(request):
    types = Type.objects.all()
    return render(request, 'dds/dictionary_management.html', {'types': types})

def type_create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type_list')
    else:
        form = TypeForm()
    return render(request, 'dds/type_form.html', {'form': form})

def type_edit(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()
            return redirect('dictionary_management')
    else:
        form = TypeForm(instance=type_obj)
    return render(request, 'dds/type_form.html', {'form': form})

def type_delete(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        type_obj.delete()
        return redirect('dictionary_management')
    return render(request, 'dds/type_confirm_delete.html', {'type': type_obj})



def category_list(request):
    categories = Category.objects.select_related('type').all()
    return render(request, 'dds/dictionary_management.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dictionary_management')
    else:
        form = CategoryForm()
    return render(request, 'dds/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dictionary_management')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dds/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('dictionary_management')
    return render(request, 'dds/category_confirm_delete.html', {'category': category})



def subcategory_list(request):
    subcategories = Subcategory.objects.select_related('category').all()
    return render(request, 'dds/dictionary_management.html', {'subcategories': subcategories})

def subcategory_create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dictionary_management')
    else:
        form = SubcategoryForm()
    return render(request, 'dds/subcategory_form.html', {'form': form})

def subcategory_edit(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('dictionary_management')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'dds/subcategory_form.html', {'form': form})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('dictionary_management')
    return render(request, 'dds/subcategory_confirm_delete.html', {'subcategory': subcategory})


def dictionary_management(request):
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    context = {
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'dds/dictionary_management.html', context)
