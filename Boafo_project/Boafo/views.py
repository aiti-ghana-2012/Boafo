### Create your views here.
from django.forms import ModelForm,forms
from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from models import Location, Service, ServiceProvider, Category, Subscription

##
###                                       COMMENTFORM MODELFORM
##class CommentForm(ModelForm):
##    class Meta:
##        model = Comment
##        exclude=['post','author']
##
####class SForm(forms.Form):
####    param = forms.CharField()
##
###                                   POST LIST VIEW
##def post_list(request):
####    se = SForm()
##    posts = Post.objects.all().order_by('-pk')
##    t = loader.get_template('blog/post_list.html')
##    c = Context({ 'posts' :posts, 'user': request.user })
##    return HttpResponse(t.render(c))
##
###                                       POST DETAIL VIEW
##@csrf_exempt
##def post_detail(request, id, showComments=False):
##    post = Post.objects.get(pk=id)
##    if (request.method == 'POST'):
##        comment = Comment(post = post)
##        comment.author = request.user
##        form = CommentForm(request.POST, instance=comment)
##        if request.user.is_active:
##            if form.is_valid():
##                form.save()
##                return HttpResponseRedirect(request.path)
##        else:
##            return HttpResponseRedirect('reg/login.html')
##    else:
##        form = CommentForm()
##    comments = Comment.objects.filter(post = id).order_by('-pk')
##    t = loader.get_template('blog/post_detail.html')
##    c = Context ({ 'post' : post, 'comments' : comments, 'form' : form, 'user' : request.user })
##    return HttpResponse(t.render(c))
##
###                               EDIT COMMENT VIEW
##@csrf_exempt
##def edit_comment(request,id):
##    comment = Comment.objects.get(pk = id)
##    post = comment.post
##    if (request.method == 'POST'):
##        form = CommentForm(request.POST,instance =comment)
##        if form.is_valid():
##            if comment.author == request.user.username:
##                form.save()
##                return HttpResponseRedirect(post.get_absolute_url()  )
##            else:
##                return HttpResponseForbidden("You do not have permission to edit this comment. Login <a href=\"/reg/login\">here</a>")
##    else:
##        form = CommentForm(instance = comment)
##    return render_to_response('blog/edit_comment.html', {'form' : form, 'user' : request.user } )
##
##        #                   POST SEARCH VIEW
##def post_search(request, text):
##    posts = Post.objects.filter(body__icontains=text)
##    return render_to_response('blog/post_search.html', {'posts' : posts , 'text' : text, 'user':request.user } ) 
##    
###                           HOME VIEW
##def home(request):
##    return render_to_response('blog/base.html', {} ) 
