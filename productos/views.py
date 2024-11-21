from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Producto
from .forms import UserRegistrationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required


# Vista principal
def index(request):
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado
        return render(request, 'index.html')
    else:
        return redirect('login')

# Vista para listar productos
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listado.html', {'productos': productos})

@login_required
def registrar_producto(request):
    return render(request, 'form_registrar.html')

@login_required
def insertar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        precio = request.POST['precio']
        Producto.objects.create(nombre=nombre, marca=marca, precio=precio)
        return redirect('listar_productos')

@login_required
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.marca = request.POST['marca']
        producto.precio = request.POST['precio']
        producto.save()
        return redirect('listar_productos')
    return render(request, 'form_actualizar.html', {'producto': producto})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')


# Vista para registrar un nuevo usuario
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Inicia sesión del usuario
                return redirect('index')  # Redirige al índice
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista para cerrar sesión
def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige al login
