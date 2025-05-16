```markdown

# 用户管理 API 文档


## 基础信息

- **基础路径**: `47.101.42.177:7788/tzb/users`

- **数据格式**: JSON


## 用户实体结构

```json

{

  "id": "整数类型，用户唯一标识",

  "username": "字符串类型，用户名",

  "password": "字符串类型，密码",

  "role": "枚举类型[student/admin/teacher]",

  "name": "字符串类型，用户姓名",

  "email": "字符串类型，电子邮箱",

  "createdAt": "时间戳(java.sql.Timestamp)，创建时间",

  "avatar": "字符串类型，头像URL（默认avatar.jpg, 先写死这个）"

}

```


## API 接口说明


### 1. 新增用户

- **端点**: `/insert`

- **HTTP方法**: POST

- **请求参数**:

  ```json

  {

    "username": "必填",

    "password": "必填",

    "role": "必填，需校验枚举值",

    "name": "必填",

    "email": "必填",

	"ceeateAt" : "问ai"

	"avatar" : 'avatar.jpg'

  }

  ```

- **成功响应**:

  ```json

  {

    "code": 200,

    "message": "用户创建成功"

  }

  ```


### 2. 删除用户

- **端点**: `/delete/{id}`

- **HTTP方法**: DELETE

- **路径参数**:

  - `id`: 要删除的用户ID

- **成功响应**:

  ```json

  {

    "code": 200,

    "message": "用户删除成功"

  }

  ```


### 3. 更新用户

- **端点**: `/updateById`

- **HTTP方法**: PUT

- **请求参数**:

- **注**：其实这个做各个读入框时， 每个输入框的值由原来传来的数据代替

  ```json

  {

    "username": "必填",

    "password": "必填",

    "role": "必填（需校验）",

    "name": "必填",

    "email": "必填"，

	"ceeateAt" : "必填"

	"avatar" : "必填"

  }

  ```

- **成功响应**:

  ```json

  {

    "code": 200,

    "message": "用户更新成功",

  }

  ```


### 4. 查询所有用户

- **端点**: `/selectAll`

- **HTTP方法**: GET

- **成功响应**:

  ```json

  {

    "code": 200,

    "data": [

      "用户对象数组"

    ]

  }

  ```


### 5. 条件查询

- **端点**: `/select/{searchValue}`

- **HTTP方法**: GET

- **路径参数**:

  - `searchValue`: 搜索关键词（支持模糊查询）

- **成功响应**:

  ```json

  {

    "code": 200,

    "data": [

      "匹配的用户对象数组"

    ]

  }

  ```



