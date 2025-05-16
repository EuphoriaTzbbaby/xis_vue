## 📘 Comment 接口说明文档

基础路径：`47.101.42.177:7788/tzb`

---

### 📌 1. 添加评论

- **类**：`CommentCreateController`
    
- **方法**：`POST /comment/add`
    
- **描述**：添加一条新的视频评论。
    
- **请求体（JSON）**：
    

```json
{
  "videoId": 1001,
  "userId": 42,
  "content": "这个视频太棒了！"
}
```

- **返回值**：
    
    - `"添加成功"`
        
    - `"添加失败"`
        

---

### 📌 2. 删除评论

- **类**：`CommentDeleteController`
    
- **方法**：`DELETE /comment/{id}`
    
- **描述**：根据评论 ID 删除评论。
    
- **路径参数**：
    
    - `id`：评论 ID（long）
        
- **返回值**：
    
    - `"删除成功"`
        
    - `"删除失败"`
        

---

### 📌 3. 查询评论

- **类**：`CommentQueryController`
    

#### ▶ 根据评论 ID 查询

- **方法**：`GET /comment/{id}`
    
- **描述**：根据评论 ID 获取评论内容。
    
- **返回值（JSON）**：
    

```json
{
  "id": 1,
  "videoId": 1001,
  "userId": 42,
  "content": "精彩的视频！",
  "createTime": "2025-05-01 10:20:00"
}
```

#### ▶ 获取指定视频下所有评论

- **方法**：`GET /comment/video/{videoId}`
    
- **描述**：获取指定视频下的所有评论。
    
- **返回值（List）**：
    

```json
[
  {
    "id": 1,
    "videoId": 1001,
    "userId": 42,
    "content": "精彩！",
    "createTime": "2025-05-01 10:20:00"
  },
  {
    "id": 2,
    "videoId": 1001,
    "userId": 21,
    "content": "值得再看一遍",
    "createTime": "2025-05-01 10:22:10"
  }
]
```

---

### 📌 4. 更新评论

- **类**：`CommentUpdateController`
    
- **方法**：`PUT /comment/update`
    
- **描述**：更新评论内容。
    
- **请求体（JSON）**：
    

```json
{
  "id": 1,
  "videoId": 1001,
  "userId": 42,
  "content": "更新后的内容",
  "createTime": "2025-05-01 10:20:00"
}
```

- **返回值**：
    
    - `"更新成功"`
        
    - `"更新失败"`
        

---

## ✅ 字段说明

| 字段名          | 类型        | 说明                           |
| ------------ | --------- | ---------------------------- |
| `id`         | long      | 评论主键 ID                      |
| `videoId`    | long      | 所属视频的 ID                     |
| `userId`     | long      | 发表评论的用户 ID                   |
| `content`    | String    | 评论文本内容                       |
| `createTime` | Timestamp | 创建时间（格式 yyyy-MM-dd HH:mm:ss） |