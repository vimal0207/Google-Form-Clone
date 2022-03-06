
# Google Form Clone for Pillarplus

This Codebase contains code for task assigned by Pillarplus company, In this project multiple users can create their own form and further share it to other users who can fill the form.




## Authors

- [@vimal0207](https://www.github.com/vimal0207)


## API Reference

#### Authentication

```http
  POST /user/singup
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Your Email For singup |
| `password` | `string` | **Required**. Password to protect your account |

```http
  GET /user/singin
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Your Email For singin |
| `password` | `string` | **Required**. Registaer password to signin |

```http
  GET /user/api/rtoken
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `rtoken` | `string` | **Required**. Refresg token to get the new access token |

#### User Form

```http
  POST /form/api/create_form/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**. Token for authentication |
| `form_name`      | `string` | **Required**. A unique name for the form |
| `file`      | `string` | **Required**. CSV file to which define the form fields |

```http
  GET /form/api/form_list/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**. Token for authentication |

```http
  GET /form/form_field/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `form_id`      | `integer` | **Required**. Form id to get get all fields of form with rules |

```http
  GET /form/form_data/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `form_id`      | `integer` | **Required**. Form id to get the form |
| `id`      | `integer` | **Required**. Data id to get detail of data |

```http
  DELETE /form/form_data/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `form_id`      | `integer` | **Required**. Form id to get the form |
| `id`      | `integer` | **Required**. Data id to delete data |

```http
  POST /form/form_data/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `form_id`      | `integer` | **Required**. Form id to get the form |
| `*`      | `*` | **Required**. All field according to form |

```http
  PATCH /form/form_data/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `form_id`      | `integer` | **Required**. Form id to get the form |
| `data_id`      | `integer` | **Required**. Data id to get the data for update |
| `*`      | `*` | **Required**. All field according to form |


## Tech Stack

**Client:** Html, Css, Bootstrap

**Server:** Django, Django Rest Famework, 

**Database** Mongodb (Djongo)


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd pillarplus
```

Start virtualenv

```bash
  virtualenv env
```
Install libraries 

```bash
pip install -r requirements.txt
```

```file
Change DATABASE_NAME in the seeting.py file
```

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```


## Acknowledgements

 - [Django Documentation](https://code.djangoproject.com/wiki/DynamicModels)
 - [Mongodb](https://www.djongomapper.com/)

## 🚀 About Me
I'm a full stack developer...

