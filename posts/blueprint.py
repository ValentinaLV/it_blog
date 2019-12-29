from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from models.post import Post
from models.tag import Tag
from .forms import PostForm

posts_ = Blueprint('posts', __name__, template_folder='templates')


# http://localhost/blog/create
@posts_.route('/create', methods=['POST', 'GET'])
def create_post():
    # if post
    if request.method == 'POST':
        title = request.form.get('title', '')
        body = request.form.get('body', '')
        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Post wasn\'t added to db')
        return redirect(url_for('posts.index'))
    # if get
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts_.route('/<slug>/edit', methods=['POST', 'GET'])
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts_.route('/')
def index():
    q = request.args.get('q')

    # /blog/?page=2 (args after =)
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(
            Post.title.contains(q) | Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=3)

    return render_template('posts/index.html', posts=posts, pages=pages)


# http://localhost/blog/first-post
@posts_.route('/<string:slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


# http://localhost/blog/tag/python
@posts_.route('/tag/<string:slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
