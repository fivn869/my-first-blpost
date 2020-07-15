from django.shortcuts import render, redirect, reverse, get_object_or_404,Http404
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import FileForm,poost as form_post
from .models import Profile, Poost



class PostEdit(View):

    TEMPLATE = 'post_edit.html'

    def get(self, request, pk):
        data = {}
        print('get')
        post = get_object_or_404(Poost, pk=pk)
        popo = {'post':post.blog, 'title':post.title}
        data['form'] =form_post(initial=popo)
        data['pk'] = pk
        return render(request, self.TEMPLATE, data)

    def post(self, request,pk):
        print('post')
        data = {}
        form = form_post(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            poo = form.cleaned_data.get('post')

            bpl=Poost.objects.get(pk=pk)

            bpl.us = request.user
            bpl.title = title
            bpl.blog = poo
            bpl.save()
            print("saved")

            return redirect('home')
        return render(request, self.TEMPLATE)


class Post02(View):

    TEMPLATE = 'post_02.html'

    def get(self, request):
        data = {}
        form = form_post()
        data['form'] = form
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        data = {}
        form = form_post(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            poo = form.cleaned_data.get('post')

            bpl=Poost()
            bpl.us = request.user
            bpl.title = title
            bpl.blog = poo
            bpl.save()
            print("saved")

            return redirect('home')




class ProfileForm(View):
    TEMPLATE='profile.html'

    def get(self, request):

        data = {}
        form = FileForm()
        user = Profile.objects.filter(us=request.user)
        if user.exists():
            form = FileForm(instance=user[0])

        data['form'] = form
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        data ={}
        print("post")

        form = FileForm(request.POST)

        if form.is_valid():
            pofi = Profile.objects.filter(us=request.user)
            if pofi.exists():
                pro =pofi[0]
                pro.delete()
                blog = form.save(commit=False)
                blog.us = request.user
                blog.save()

            else:
                blog = form.save(commit=False)
                blog.us = request.user
                blog.save()
            return redirect('home')

        else:
            data['form'] = FileForm()
            print('false')
            return redirect('profile')


class Register(View):
    TEMPLATE = "register_01.html"

    def get(self, request):
        data = {}
        data['error'] = request.GET.get('error')
        return render(request, self.TEMPLATE, data)

    def post(self, request):

        us = request.POST.get('username')
        ps = request.POST.get('password')
        ps2 = request.POST.get('check_password')


        exist = User.objects.filter(username=us).exists()
        if exist:
            return redirect('/register?error= the username has been used')
        if ps !=ps2:
            return redirect('/register?error=the twice password input is not same')
        User.objects.create_user(username=us, password=ps)

        return render(request, "login_1.html",{'message':'Congration! Now you can login'})

class Login(View):
    TEMPLATE = 'login_1.html'

    def get(self, request):
        data = {}
        data['error'] = request.GET.get('error')
        return render(request, self.TEMPLATE, data)


    def post(self, request):
        us = request.POST.get('username')
        ps = request.POST.get('password')
        print(us,ps)
        user = authenticate(username=us, password=ps)

        if user:
            print("success login!")
            login(request, user)
        else:
            print("wrong")
            return redirect("/login?error= Either username or password is wrong")

        return redirect('home')

class HomePage(View):
    TEMPLATE='home_01.html'

    def get(self, request):
        data = {}
        user =request.user

        if user.is_authenticated:
            des = Profile.objects.filter(us=user)
            if des.exists():
                des = des[0]
                data['description'] = des.description
                data['occupy'] = des.occupy
            else:
                data['error'] = 'please fill your own profile'
        user_posts = Poost.objects.filter(us=request.user)
        user_infos = Profile.objects.filter()
        data['infos'] = user_infos
        data['posts'] = user_posts

        return render(request, self.TEMPLATE,data)
    def post(self, request):

        blog = request.POST.get("comment")
        title = request.POST.get("title")
        post = Poost()

        post.title=title
        post.blog = blog
        post.us=request.user
        post.publish()
        print("success post!")

        return redirect('home')


class LogoutPage(View):

    def get(self, request):
        logout(request)
        return redirect('login')
# Create your views here.