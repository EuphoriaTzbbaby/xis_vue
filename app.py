from flask import Flask, request, jsonify
from comment import Comment_Spider
from xhs_utils.common_utils import init

app = Flask(__name__)
cookies_str, base_path = init()
comment_spider = Comment_Spider()

@app.route('/api/fetch_comments', methods=['POST'])
def fetch_comments_api():
    """
    接收 JSON 格式的 note_url 参数，返回对应小红书笔记的评论（JSON 格式）
    请求示例：
    {
        "note_url": "https://www.xiaohongshu.com/explore/xxxxx"
    }
    """
    data = request.get_json()
    if not data or 'note_url' not in data:
        return jsonify({"success": False, "message": "缺少 note_url 参数", "comments": []}), 400

    note_url = data['note_url']
    success, msg, comments = comment_spider.spider_note_comment(note_url, cookies_str)

    return jsonify({
        "success": success,
        "message": msg,
        "comments": comments if success else []
    })

if __name__ == '__main__':
    app.run(debug=True)
