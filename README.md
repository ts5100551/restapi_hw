# Django REST Framework Homework
## 目標：完成一組 API 做到 User 的新增/讀取/刪除

1. Build image. <br />
`docker build --tag restapi_hw_image .`

2. Create the container and set the port and volume between local and container by using the image created above. <br />
`docker run --name restapi_hw_container -d -p 8000:8000 -v $(pwd):/restapi_hw/ restapi_hw_image` 

3. The following command can be used to entering the container. <br />
`docker exec -it restapi_hw_container /bin/bash`