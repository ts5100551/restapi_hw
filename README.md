1. Build image.
`docker build --tag restapi_hw_image .`

2. Create the container and set the port and volume between local and container by using the image created above.
`docker run --name restapi_hw_container -d -p 8000:8000 -v $(pwd):/restapi_hw/ restapi_hw_image` 

3. The following command can be used to entering the container.
`docker exec -it restapi_hw_container /bin/bash`