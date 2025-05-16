
---

## 📘 Reply 接口说明文档

基础路径：`47.101.42.177:7788/tzb`

---

### 📌 1. 添加回复

- **URL**：`POST /reply/add`
    
- **描述**：添加一条新的评论回复。
    
- **请求参数（JSON）**：
    

```json
{
  "commentId": 1,
  "userId": 2,
  "replyToUserId": 3,
  "content": "感谢你的分享！",
  "createTime": "2025-05-01 10:15:00"
}
```

- **返回值**：
    
    - `"success"`：添加成功
        
    - `"fail"`：添加失败
        

---

### 📌 2. 根据 ID 获取单条回复

- **URL**：`GET /reply/byId/{id}`
    
- **描述**：根据回复 ID 获取单条回复信息。
    
- **路径参数**：
    
    - `id`：回复的唯一标识符（long）
        
- **返回值（JSON 示例）**：
    

```json
{
  "id": 1,
  "commentId": 1,
  "userId": 2,
  "replyToUserId": 3,
  "content": "谢谢！",
  "createTime": "2025-05-01 10:15:00"
}
```

---

### 📌 3. 获取指定评论下的所有回复

- **URL**：`GET /reply/byCommentId/{commentId}`
    
- **描述**：获取指定评论下的所有回复（按时间升序）。
    
- **路径参数**：
    
    - `commentId`：评论 ID（long）
        
- **返回值（List）**：
    

```json
[
  {
    "id": 1,
    "commentId": 10,
    "userId": 2,
    "replyToUserId": 3,
    "content": "我也觉得这段很精彩",
    "createTime": "2025-05-01 10:15:00"
  },
  {
    "id": 2,
    "commentId": 10,
    "userId": 4,
    "replyToUserId": 2,
    "content": "同意",
    "createTime": "2025-05-01 10:16:30"
  }
]
```

---

### 📌 4. 删除回复

- **URL**：`DELETE /reply/delete/{id}`
    
- **描述**：根据回复 ID 删除一条回复。
    
- **路径参数**：
    
    - `id`：回复的唯一标识符（long）
        
- **返回值**：
    
    - `"success"`：删除成功
        
    - `"fail"`：删除失败
        

---

### 📌 5. 更新回复内容

- **URL**：`PUT /reply/update/{id}`
    
- **描述**：更新指定回复的内容。
    
- **路径参数**：
    
    - `id`：回复 ID（long）
        
- **请求体**（纯文本）：
    
    - 新内容，例如 `"修改后的回复内容"`
        
- **返回值**：
    
    - `"success"`：更新成功
        
    - `"fail"`：更新失败
        

---

## ✅ 补充说明

|字段名|类型|说明|
|---|---|---|
|`id`|long|回复主键 ID|
|`commentId`|long|所属评论的 ID|
|`userId`|long|发起回复的用户 ID|
|`replyToUserId`|long|被回复的用户 ID|
|`content`|String|回复的文本内容|
|`createTime`|Timestamp|创建时间（格式统一）|
