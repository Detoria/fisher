from flask import jsonify, Blueprint
from app.helper import is_isbn_or_key
from app.yushu_book import YuShuBook

web = Blueprint('web', __name__)

@web.route('/book/search/<q>/<page>')
def search(q, page):

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)