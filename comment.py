import json
import pandas as pd
from datetime import datetime
from loguru import logger
from apis.pc_apis import XHS_Apis
from xhs_utils.common_utils import init

class Comment_Spider:
    def __init__(self):
        self.xhs_apis = XHS_Apis()

    def _format_timestamp(self, timestamp: int) -> str:
        try:
            return datetime.fromtimestamp(timestamp / 1000).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return "未知时间"

    def _get_user_info(self, user_id: str, cookies_str: str) -> tuple:
        try:
            success, msg, user_info = self.xhs_apis.get_user_info(user_id, cookies_str)
            if success:
                gender = user_info.get("data", {}).get("basic_info", {}).get("gender", 2)
                ip_location = user_info.get("data", {}).get("basic_info", {}).get("ip_location", "未知地址")
                return gender, ip_location
            else:
                logger.warning(f"获取用户信息失败: {msg}")
                return 2, "未知地址"
        except Exception as e:
            logger.error(f"获取用户信息异常: {str(e)}")
            return 2, "未知地址"

    def _get_gender_str(self, gender: int) -> str:
        return {0: "男性", 1: "女性"}.get(gender, "未知")

    def _format_comment_data(self, comment: dict, cookies_str: str, level: str = "一级") -> dict:
        user_info = comment.get("user_info", {})
        user_id = user_info.get("user_id", "")
        nickname = user_info.get("nickname", "未知用户")
        gender, ip_location = self._get_user_info(user_id, cookies_str)
        gender_str = self._get_gender_str(gender)

        return {
            "note_id": comment.get("note_id", ""),
            "comment_id": comment.get("id", ""),
            "user_id": user_id,
            "nickname": nickname,
            "content": comment.get("content", "无内容"),
            "time": self._format_timestamp(comment.get("time", 0)),
            "like_count": comment.get("like_count", 0),
            "gender": gender_str,
            "ip_location": ip_location,
            "level": level
        }

    def _print_comment(self, comment_data: dict):
        logger.info(f"[{comment_data['nickname']}] (性别: {comment_data['gender']}, 地址: {comment_data['ip_location']}) 发表了评论: {comment_data['content']}")

    def _save_comments_to_csv(self, comments: list, note_id: str, output_dir: str):
        try:
            filename = f"{output_dir}/note_{note_id}_comments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            pd.DataFrame(comments).to_csv(filename, index=False, encoding="utf-8-sig")
            logger.info(f"评论已保存到 {filename}")
        except Exception as e:
            logger.error(f"保存 CSV 失败: {str(e)}")

    def spider_note_comment(
        self,
        note_url: str,
        cookies_str: str,
        proxies=None,
        save_to_csv: bool = True,
        output_dir: str = "D:/vscode/JuRuoVueDeWay/Spider_XHS/datas"
    ):
        try:
            success, msg, comment_data = self.xhs_apis.get_note_all_comment(note_url, cookies_str, proxies)
            if not success:
                logger.warning(f"获取评论失败: {msg}")
                return success, msg, []

            logger.info(f"成功获取笔记评论，共 {len(comment_data)} 条一级评论")
            all_comments = []

            for comment in comment_data:
                primary = self._format_comment_data(comment, cookies_str, "一级")
                self._print_comment(primary)
                all_comments.append(primary)

                for sub in comment.get("sub_comments", []):
                    secondary = self._format_comment_data(sub, cookies_str, "二级")
                    self._print_comment(secondary)
                    all_comments.append(secondary)

            if save_to_csv:
                note_id = note_url.split("/")[-1].split("?")[0]
                self._save_comments_to_csv(all_comments, note_id, output_dir)

            return True, "评论获取成功", all_comments

        except Exception as e:
            msg = str(e)
            logger.error(f"发生异常: {msg}")
            return False, msg, []

# if __name__ == "__main__":
#     """
#     单独运行：打印笔记评论内容到控制台并保存到 CSV
#     """
#     cookies_str, base_path = init()
#     comment_spider = Comment_Spider()

#     note_url = r"https://www.xiaohongshu.com/explore/6803758b000000001c0064b1?xsec_token=ABmyQP4kXFmSdN5dfpxDYaINKO5574nx64hYR26OlUitY=&xsec_source=pc_feed"

#     success, msg = comment_spider.spider_note_comment(
#         note_url, cookies_str, save_to_csv=True, output_dir="comments"
#     )
#     logger.info(f"爬取结果: {success}, 消息: {msg}")

#     # 创建 XHS_Apis 实例
#     # xhs_apis = XHS_Apis()

#     # user_id = "61ab7f8d000000001000a2ad"
#     # # 测试 get_user_info
#     # success, msg, user_info = xhs_apis.get_user_info(user_id, cookies_str)
#     # if success:
#     #     print("获取用户信息成功:", user_info)
#     # else:
#     #     print("获取用户信息失败:", msg)

#     # # 测试 get_user_self_info
#     # success, msg, self_info = xhs_apis.get_user_self_info(cookies_str)
#     # if success:
#     #     print("获取用户自己信息1成功:", self_info)
#     # else:
#     #     print("获取用户自己信息1失败:", msg)

#     # # 测试 get_user_self_info2
#     # success, msg, self_info2 = xhs_apis.get_user_self_info2(cookies_str)
#     # if success:
#     #     print("获取用户自己信息2成功:", self_info2)
#     # else:
#     #     print("获取用户自己信息2失败:", msg)

