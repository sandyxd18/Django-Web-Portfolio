# Portfolio Website base on Django

This is my final individual project in Net Development 2024.
![image](https://github.com/sandyxd18/Django-Web-Portfolio/assets/137029388/8f1494b3-2ba7-42e0-bf06-09b57e6813fc)

## Overview

This project is build base on Django, so you can directly change some content inside of website using Django Administration.
![image](https://github.com/sandyxd18/Django-Web-Portfolio/assets/137029388/67bd7034-90ed-4bce-845b-005262f8e4e4)
You can access to this url to change content.
```
YOUR_IP_ADDRESS:8000/admin
```

## Getting Started
1. Clone the repository
```bash
git clone https://github.com/sandyxd18/Django-Web-Portfolio.git
cd Django-Web-Portfolio/
```

2. Build docker image
```bash
docker build -t image-name .
```

3. Run docker container with the image
```bash
docker run -d -p 8080:7000 --restart always --name web-porto image-name
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
