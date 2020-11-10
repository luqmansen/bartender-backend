
# Bartender API

The API is mostly a readonly, since currently we don't need to update stuff, but might change in the future.

## Indices

* [Article](#article)

  * [Detail](#1-detail)
  * [List](#2-list)

* [Gallery](#gallery)

  * [List](#1-list)


--------


## Article
Show article related API



### 1. Detail


Retrieve particular article from the slug


***Endpoint:***

```bash
Method: GET
Type: 
URL: {{server-address}}/api/article/{{slug-example}}/
```



***More example Requests/Responses:***


##### I. Example Request: Detail



##### I. Example Response: Detail
```js
{
    "id": 3,
    "title": "Article Example",
    "header_image": "https://res.cloudinary.com/hfmoruzbm/image/upload/v1/media/images/article/Rectangle_1_ffb3yi",
    "content": "<p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\">Lorem ipsum dolor sit amet</span></p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\"><br></span>Consectetur adipiscing elit. Morbi tempor vestibulum elit, at aliquam magna fermentum nec. Phasellus maximus risus ac scelerisque auctor. Donec porta finibus consequat. Ut suscipit vitae mauris tincidunt consectetur. Vivamus gravida placerat felis, eu pretium metus ultricies in.</p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\">Vestibulum dolor lacus</span></p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\">Tristique ut erat eget, hendrerit mattis libero. Sed pellentesque tortor ac sem pellentesque, sed blandit tellus auctor. Suspendisse potenti. Mauris in est non turpis consequat blandit. Nam turpis nunc, feugiat eu mi ac, dictum tempor diam. Integer eu quam ut nisl blandit porta.&nbsp;</p>",
    "slug": "article-example-kpvs3wu9qc"
}
```


***Status Code:*** 200

<br>



### 2. List


Get all article list


***Endpoint:***

```bash
Method: GET
Type: 
URL: {{server-address}}/api/article
```



***More example Requests/Responses:***


##### I. Example Request: List



##### I. Example Response: List
```js
[
    {
        "id": 3,
        "title": "Article Example",
        "header_image": "https://res.cloudinary.com/hfmoruzbm/image/upload/v1/media/images/article/Rectangle_1_ffb3yi",
        "content": "<p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\">Lorem ipsum dolor sit amet</span></p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\"><br></span>Consectetur adipiscing elit. Morbi tempor vestibulum elit, at aliquam magna fermentum nec. Phasellus maximus risus ac scelerisque auctor. Donec porta finibus consequat. Ut suscipit vitae mauris tincidunt consectetur. Vivamus gravida placerat felis, eu pretium metus ultricies in.</p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\">Vestibulum dolor lacus</span></p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\">Tristique ut erat eget, hendrerit mattis libero. Sed pellentesque tortor ac sem pellentesque, sed blandit tellus auctor. Suspendisse potenti. Mauris in est non turpis consequat blandit. Nam turpis nunc, feugiat eu mi ac, dictum tempor diam. Integer eu quam ut nisl blandit porta.&nbsp;</p>",
        "slug": "article-example-kpvs3wu9qc"
    },
    {
        "id": 4,
        "title": "Article 2 Example",
        "header_image": "https://res.cloudinary.com/hfmoruzbm/image/upload/v1/media/images/article/black_icad3t",
        "content": "<p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\">Lorem ipsum dolor sit amet</span></p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\"><br></span>Consectetur adipiscing elit. Morbi tempor vestibulum elit, at aliquam magna fermentum nec. Phasellus maximus risus ac scelerisque auctor. Donec porta finibus consequat. Ut suscipit vitae mauris tincidunt consectetur. Vivamus gravida placerat felis, eu pretium metus ultricies in.</p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\"><span style=\"font-weight: 700;\">Vestibulum dolor lacus</span></p><p style=\"margin-bottom: 15px; padding: 0px; text-align: justify; font-family: &quot;Open Sans&quot;, Arial, sans-serif;\">Tristique ut erat eget, hendrerit mattis libero. Sed pellentesque tortor ac sem pellentesque, sed blandit tellus auctor. Suspendisse potenti. Mauris in est non turpis consequat blandit. Nam turpis nunc, feugiat eu mi ac, dictum tempor diam. Integer eu quam ut nisl blandit porta.&nbsp;</p>",
        "slug": "article-2-example-q9ciw4lwq1"
    }
]
```


***Status Code:*** 200

<br>



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


##### I. Example Request: List



##### I. Example Response: List
```js
[
    {
        "id": 1,
        "file_name": "Doge",
        "image": "https://res.cloudinary.com/hfmoruzbm/image/upload/v1/media/images/gallery/bz9t3q58wrf51_qiqnhx"
    },
    {
        "id": 2,
        "file_name": "Doge2",
        "image": "https://res.cloudinary.com/hfmoruzbm/image/upload/v1/media/images/gallery/1_IU3_gLp3V1gFq2deAod9BQ_enn1gv"
    }
]
```


***Status Code:*** 200

<br>



---
[Back to top](#bartender-api)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2020-11-10 19:56:24 by [docgen](https://github.com/thedevsaddam/docgen)
