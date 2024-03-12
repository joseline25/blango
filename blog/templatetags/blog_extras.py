from django.contrib.auth import get_user_model
<<<<<<< HEAD
from django import template
from blog.models import Post
=======
user_model = get_user_model()

>>>>>>> a81208007da7b52442be7ef013deea0f5358282e
from django.utils.html import escape
from django.utils.safestring import mark_safe
from blog.models import Post
from django import template
from django.utils.html import format_html

register = template.Library()

<<<<<<< HEAD

@register.simple_tag(takes_context=True)
def author_details_tag(context):
  request = context["request"]
  current_user = request.user
  post = context["post"]
  author = post.author
  if author == current_user:
    return format_html("<strong>me</strong>")
  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"
  if author.email:
    prefix = format_html('<a href="mailto:{}">',
    author.email)
    suffix = format_html("</a>")
  else:
    prefix = ""
    suffix = ""
  return format_html("{}{}{}", prefix, name, suffix)

@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return "</div>"


@register.simple_tag
def col(extra_classes=""):
  return format_html('<div class="col {}">', extra_classes)
=======
@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)


@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return format_html("</div>")

@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)
>>>>>>> a81208007da7b52442be7ef013deea0f5358282e


@register.simple_tag
def endcol():
<<<<<<< HEAD
  return format_html("</div>")  
=======
    return format_html("</div>")
>>>>>>> a81208007da7b52442be7ef013deea0f5358282e


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
<<<<<<< HEAD
  posts = Post.objects.exclude(pk=post.pk)[:5]
  return {"title": "Recent Posts", "posts": posts}
=======
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}
>>>>>>> a81208007da7b52442be7ef013deea0f5358282e
