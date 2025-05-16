## 基础信息

- **基础路径**: `47.101.42.177:7788/tzb`
- **数据格式**: JSON
- **认证方式**: 无需认证（若有认证需求，请另行说明）

---

## 📁 模块概览

- `VideoAlbumController*`: 管理视频合集（如名称、封面图、描述等）
    
- `VideoController*`: 管理具体视频条目（如所属合集、视频 OSS 地址、标题等）
    

---

## 📚 VideoAlbumController 接口文档

### ✅ 查询合集列表

- **接口**：`GET /videoAlbum/select/all`
    
- **描述**：获取所有视频合集信息。
    
- **响应**：
    

```json
[
  {
    "id": 1,
    "title": "合集标题",
    "description": "合集描述",
    "coverUrl": "https://oss.../cover.jpg",
    "createTime": "2025-04-29T08:00:00"
  }
]
```

---

### ✅ 插入新合集

- **接口**：`POST /videoAlbum/insert`
    
- **描述**：添加一个新的视频合集。
    
- **请求体**：
    

```json
{
  "title": "新合集标题",
  "description": "合集描述",
  "coverUrl": "https://oss.../封面地址"
}
```

- **响应**：成功状态码或插入条数。
    

---

### ✅ 删除合集

- **接口**：`DELETE /videoAlbum/delete/{id}`
    
- **描述**：根据主键 ID 删除视频合集。
    
- **路径参数**：
    
    - `id`：合集 ID
        

---

### ✅ 更新合集

- **接口**：`PUT /videoAlbum/update`
    
- **描述**：根据 ID 修改合集信息。
    
- **请求体**：
    

```json
{
  "id": 1,
  "title": "修改后的标题",
  "description": "修改描述",
  "coverUrl": "https://oss.../修改后的封面"
}
```

---

## 🎥 VideoController 接口文档

### ✅ 查询视频列表

- **接口**：`GET /video/select/all`
    
- **描述**：获取所有视频记录。
    

---

### ✅ 插入新视频

- **接口**：`POST /video/insert`
    
- **描述**：添加一条视频记录。
    
- **请求体**：
    

```json
{
  "albumId": 1,
  "title": "视频标题",
  "ossKey": "e_learning/xxx/视频.mp4",
  "videoUrl": "https://oss.../视频.mp4",
  "duration": 120,
  "sortOrder": 1
}
```

---

### ✅ 删除视频

- **接口**：`DELETE /video/delete/{id}`
    
- **描述**：根据主键 ID 删除视频。
    
- **路径参数**：
    
    - `id`：视频 ID
        

---

### ✅ 更新视频

- **接口**：`PUT /video/update`
    
- **描述**：修改视频条目。
    
- **请求体**：
    

```json
{
  "id": 1,
  "title": "修改后标题",
  "ossKey": "e_learning/xxx/修改后视频.mp4",
  "videoUrl": "https://oss.../修改后视频.mp4",
  "duration": 130,
  "sortOrder": 2
}
```

---
