# # user/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
#
# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('goods:product_list')
#             else:
#                 messages.error(request, '用户名或密码错误')
#     else:
#         form = UserLoginForm()
#     return render(request, 'user/login.html', {'form': form})
#
# def user_logout(request):
#     logout(request)
#     return redirect('goods:product_list')
#
# def user_register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             messages.success(request, '注册成功，请登录')
#             return redirect('user:login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'user/register.html', {'form': form})
#
# def user_profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '个人信息更新成功')
#         else:
#             messages.error(request, '更新失败，请检查输入')
#     else:
#         form = UserProfileForm(instance=request.user)
#     return render(request, 'user/profile.html', {'form': form})