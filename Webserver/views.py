import os
from django.http import HttpResponse
import json

fishname='hhh'
def handlepicture(request):
    if request.method == "POST":
        picture = request.FILES.get("picture", None)
        destination = open(os.path.join("/home/zouyi/wechat/pictures/", picture.name), 'wb+')
        for chunk in picture.chunks():
            destination.write(chunk)
        destination.close()
        # pysh(picture)
	python /home/zouyi/wechat/script/predict.py
    if request.method == "GET":
        data = {"fishname": fishname}
        return HttpResponse(json.dumps(data), content_type="application/json")
        # render(request, {"data": data})

# def pysh(picture):


if __name__ == '__main__':
    handlepicture()

