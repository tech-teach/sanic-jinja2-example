from sanic import Sanic
from sanic import response

from jinja2 import Template

app = Sanic()

txt_template = open("template.html").read()

tasks = []

#generador de id
def numId():
	i=0
	while True:
		yield i
		i+=1

nums=numId()

@app.route('/', methods=["GET"])
async def test(request):
    task = request.args.get('task')
    if task:
        tasks.append({str(next(nums)):task})

    template = Template(txt_template)
    html_template = template.render(tasks=tasks)
    return response.html(html_template)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
