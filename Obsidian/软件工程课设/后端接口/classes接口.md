# 用户管理 API 文档

## 基础信息

- **基础路径**: `47.101.42.177:7788/tzb`
- **数据格式**: JSON
- **认证方式**: 无需认证（若有认证需求，请另行说明）

## 班级实体结构

```json
{
  "id": "整数类型，班级唯一标识",
  "name": "字符串，班级名称",
  "createdAt": "时间戳 (java.sql.Timestamp)，创建时间"
}
```

## 页面功能要求

### 页面 A（班级管理页面）

- **功能概述**：
    - 作为应用的根页面，所有后续页面均为 A 的子页面。
    - 显示所有班级信息（通过 `/classes/selectAll` 接口），使用表格展示。
    - 每行包含三个操作按钮：删除、编辑、查看。
    - 提供“新增班级”按钮（调用 `/classes/insert` 接口），位置由开发者设计。
    - 支持搜索框功能，根据输入内容查询班级（调用 `/classes/select/{searchValue}` 接口）。
- **表格字段**：
    - `id`：班级 ID
    - `name`：班级名称
    - `createdAt`：创建时间
- **操作按钮**：
    - **按钮 1 - 删除**：调用 `/classes/delete/{id}` 删除指定班级。
    - **按钮 2 - 编辑**：调用 `/classes/updateById`，弹出编辑框，输入框默认显示原始数据。
    - **按钮 3 - 查看**：调用 `/users/selectStudentsAndTeachers/{id}`，跳转到页面 B，展示该班级的学生和教师信息。

### 页面 B（班级成员页面）

- **功能概述**：
    - 显示指定班级（由页面 A 传入的 `id`）的学生和教师信息。
    - 支持搜索框功能，根据输入内容查询成员（调用 `/users/select/{searchValue}/{id}` 接口）。

---

## API 接口说明

### 1. 查询所有班级

- **端点**: `/classes/selectAll`
- **方法**: `GET`
- **请求参数**: 无
- **成功响应**:
    
    ```json
    {
      "code": 200,
      "data": [
        // 班级对象数组
        {
          "id": 1,
          "name": "Class A",
          "createdAt": "2023-10-01T12:00:00"
        }
      ]
    }
    ```
    
- **错误响应**:
    
    ```json
    {
      "code": 500,
      "message": "服务器错误"
    }
    ```
    

### 2. 新增班级

- **端点**: `/classes/insert`
- **方法**: `POST`
- **请求参数**:
    
    ```json
    {
      "name": "字符串，班级名称，必填",
      "createdAt": "时间戳，创建时间，建议由服务器生成"
    }
    ```
    
- **成功响应**:
    
    ```json
    {
      "code": 200,
      "message": "班级创建成功"
    }
    ```
    
- **错误响应**:
    
    ```json
    {
      "code": 400,
      "message": "班级名称不能为空"
    }
    ```
    

### 3. 删除班级

- **端点**: `/classes/delete/{id}`
- **方法**: `DELETE`
- **路径参数**:
    - `id`: 整数，班级 ID，必填
- **成功响应**:
    
    ```json
    {
      "code": 200,
      "message": "班级删除成功"
    }
    ```
    
- **错误响应**:
    
    ```json
    {
      "code": 404,
      "message": "班级不存在"
    }
    ```
    

### 4. 更新班级

- **端点**: `/classes/updateById`
- **方法**: `PUT`
- **请求参数**:
    
    ```json
    {
      "id": "整数，班级 ID，必填",
      "name": "字符串，班级名称，必填",
      "createdAt": "时间戳，创建时间，必填"
    }
    ```
    
- **说明**：编辑时，输入框应预填原始数据（由 `/classes/selectAll` 或其他接口获取）。
- **成功响应**:
    
    ```json
    {
      "code": 200,
      "message": "班级更新成功"
    }
    ```
    
- **错误响应**:
    
    ```json
    {
      "code": 400,
      "message": "无效的班级 ID"
    }
    ```
    

### 5. 查询班级成员（学生和教师）

- **端点**: `/users/selectStudentsAndTeachers/{id}`
- **方法**: `GET`
- **路径参数**:
    - `id`: 整数，班级 ID，必填
- **成功响应**:
    
    ```json
    {
      "code": 200,
      "data": [
        // 用户对象数组
        {
          "id": 1,
          "name": "John Doe",
          "role": "student"
        },
        {
          "id": 2,
          "name": "Jane Smith",
          "role": "teacher"
        }
      ]
    }
    ```
    
- **错误响应**:
    
    ```json
    {
      "code": 404,
      "message": "班级不存在"
    }
    ```
    

### 6. 按条件查询班级

- **端点**: `/classes/select/{searchValue}`
- **方法**: `GET`
- **路径参数**:
    - `searchValue`: 字符串，搜索关键词，支持模糊查询
- **成功响应**:
    
    ```json
    {
      "code": 200,
      "data": [
        // 匹配的班级对象数组
        {
          "id": 1,
          "name": "Class A",
          "createdAt": "2023-10-01T12:00:00"
        }
      ]
    }
    ```
    
- **错误响应**:
    
    ```json
    {
      "code": 400,
      "message": "搜索关键词不能为空"
    }
    ```
    

### 7. 按条件查询班级成员

- **端点**: `/users/select/{searchValue}/{id}`
- **方法**: `GET`
- **路径参数**:
    - `searchValue`: 字符串，搜索关键词，支持模糊查询
    - `id`: 整数，班级 ID，限制查询范围
- **成功响应**:
    
    ```json
    {
      "code": 200,
      "data": [
        // 匹配的用户对象数组
        {
          "id": 1,
          "name": "John Doe",
          "role": "student"
        }
      ]
    }
    ```
    
- **错误响应**:
    
    ```json
    {
      "code": 404,
      "message": "班级或用户不存在"
    }
    ```
    

---

## 备注

- 所有时间戳字段（`createdAt`）应使用 `java.sql.Timestamp` 格式，建议由后端自动生成。
- 搜索功能支持模糊查询，开发者需确保输入框内容在调用接口前进行必要的校验（如非空检查）。
- 页面 A 和 B 的搜索框实现应支持实时或按需查询（例如，输入后按回车或点击搜索按钮触发）。
- 建议在前端使用框架（如 React、Vue）实现动态表格和路由跳转，提升用户体验。