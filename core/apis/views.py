from core import Blueprint, request, models, db,\
    jsonify
from time import time
from random import randint

api = Blueprint('api', __name__)


def exclude_from_token_check(func):
    func._exclude_from_token_check = True
    return func


# Test Home
@api.route('', methods=['GET'])
def home():
    return jsonify({"status": "success", "message": "API Working"}), 200


# Add Post
@api.route('add-post', methods=['POST'])
def add_post():
    print(request.json)
    try:
        by = request.json.get('by')
        descendants = request.json.get('descendants')
        title = request.json.get('title')
        url = request.json.get('url')
        text = request.json.get('text')
        while True:
            id = randint(10000001, 30000000)
            if models.PostId.query.filter_by(public_id=id).first() is None:
                break
        p_id = models.PostId(
            public_id=id
        )
        db.session.add(p_id)
        db.session.commit()
        get_type = models.Type.query.filter_by(name="story").first()
        if get_type is None:
            get_type = models.Type(name="story")
            db.session.add(get_type)
            db.session.commit()

        post = models.Post(
            by = by,
            descendants = descendants,
            public_id = p_id.public_id,
            time = time(),
            title = title,
            text = text,
            url = url,
            type = get_type.id,
        )
        db.session.add(post)
        db.session.commit()
        return jsonify({"status": "success", "data": "Post Entered"}), 201
    except:
        return jsonify({"status": "error", "data": "Unable To complete Post"}), 400

# Show Post
@api.route('get-posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', "", type=str)
    per_page = 10
    if search:
        try:
            post = models.Post.query.order_by(models.Post.id.desc())\
                .paginate(page=page, per_page=per_page)
        except:
            return jsonify({"status": "error", "message": "Page not found"}), 400
        
    else:
        try:
            post = models.Post.query.filter(models.Post.text.ilike(f"%{search}%") | models.Post.title.ilike(f"%{search}%")) \
                .order_by(models.Post.created_on.desc())\
                .paginate(page=page, per_page=per_page)  
        except:
            return jsonify({"status": "error", "message": "Page not found"}), 400

    posts = []
    for _ in post.items:
        trans = _.sheetSummary
        posts.append(trans)
    return jsonify({"status": "success", "data": posts, "page":page, "length":round(post.total/per_page)}), 200

# Show Post
@api.route('get-comments', methods=['GET'])
def get_comments():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    try:
        post = models.Comment.query.order_by(models.Comment.id.asc())\
            .paginate(page=page, per_page=per_page)
    except:
        return jsonify({"status": "error", "message": "Comment not found"}), 404

    posts = []
    for _ in post.items:
        trans = _.sheetSummary
        posts.append(trans)
    return jsonify({"status": "success", "data": posts, "page":page, "length":round(post.total/per_page)})


# Add Comment
@api.route('add-comment', methods=['POST'])
def add_comment():
    by = request.json.get('by')
    title = request.json.get('title')
    text = request.json.get('text')
    parent_id_ = request.json.get('parent_id')
    
    comment_reply = False
    parent_id = models.PostId.query.filter_by(
        public_id=parent_id_
    ).first()
    if parent_id is not None:
        post_id = parent_id.id
        comment_reply = False
    else:
        print(parent_id)
        parent_id = models.Comments.query.filter_by(
            public_id=parent_id_
        ).first()
        print(parent_id)
        if parent_id is not None:
            parent_id.replied = True
            post_id = parent_id.id
            comment_reply = True
        else:
            return jsonify({"status": "error", "message": "Post does not exist"}), 404

    while True:
        id = randint(10000001, 30000000)
        if models.PostId.query.filter_by(public_id=id).first() is None:
            print(id)
            break
    post = models.Comments(
        by = by,
        parent_id = post_id,
        public_id = id,
        time = time(),
        title = title,
        text = text,
        kid = comment_reply
    )
    db.session.add(post)
    db.session.commit()
    
    # find_type = models.Type.query.filter_by(name="comment").first()
    # if find_type is None:
    #     type_ = models.Type(
    #         name = "comment",
    #     )
    #     db.session.add(type_)
    #     post.type = type_.id
    # else:
    #     post.type = find_type.id
    # db.session.commit()

    return jsonify({"status": "success", "message": "Comment Entered"})



# Add Post
@api.route('delete-post', methods=['POST'])
def delete_post():
    id = request.args.get('id', None, type=int)
    return jsonify({"status": "success", "message": "Comment Entered"})
