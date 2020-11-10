# bartender-backend

Backend for some website, integrated with 
Cloudinary for media storage. 

Please provide .env files with format below
```
API_KEY=<your-api-key>
API_SECRET=<your-api-secret>
CLOUD_NAME=<your-cloud_name>
SECRET_KEY='changeme'
CLEARDB_DATABASE_URL='mysql://user:password@hosts:3306/db-name'
DEPLOY=DEV
```

# Docs
## Indices

* [Gallery](#gallery)
  * [List](#1-list)

--------


## Gallery



### 1. List


Get all gallery images


***Endpoint:***

```bash
Method: GET
Type: 
URL: {{server-address}}/api/gallery
```



***More example Requests/Responses:***


##### I. Example Request: gallery list



##### I. Example Response: gallery list
```js
[
    {
        "id": 1,
        "created_at": "2020-11-10T05:56:18Z",
        "file_name": "Doge",
        "image": "https://res.cloudinary.com/hfmoruzbm/image/upload/v1/media/images/gallery/bz9t3q58wrf51_qiqnhx"
    },
    {
        "id": 2,
        "created_at": "2020-11-10T05:57:14Z",
        "file_name": "Doge2",
        "image": "https://res.cloudinary.com/hfmoruzbm/image/upload/v1/media/images/gallery/1_IU3_gLp3V1gFq2deAod9BQ_enn1gv"
    }
]
```


***Status Code:*** 200

<br>



---
[Back to top](#bartender-api)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2020-11-10 13:42:06 by [docgen](https://github.com/thedevsaddam/docgen)
