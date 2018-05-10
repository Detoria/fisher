from flask import jsonify, Blueprint, request
from app.helper import is_isbn_or_key
from app.yushu_book import YuShuBook
from app.web import web
from app.forms.book import SearchForm


@web.route('/book/search')
def search():

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

    # a = request.args.to_dict() ## 将不可变字典转换为普通字典
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)

        return jsonify(result)
    else:
        return jsonify(form.errors)