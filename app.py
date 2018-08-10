from sanic import Sanic
from sanic import response

from jinja2 import Template

app = Sanic()

txt_template = open("template.html").read()
tasks = []

@app.route('/', methods=["GET"])
async def save_task(request):
	task = request.args.get('task')
	if task:
		tasks.append([task,False])

	template = Template(txt_template)
	html_template = template.render(tasks=tasks)
	return response.html(html_template)

@app.route('/task/<_id>', methods=["GET"])
async def delete_task(request,_id):
	template = Template(txt_template)
	respuesta={}
	if int(_id) >= len(tasks) or int(_id) < 0:
		respuesta={"status":"not found"}
	try:
		del tasks[int(_id)]
	except ValueError:
		respuesta={"status": "id is not valid"}

	if len(respuesta) == 0:
		respuesta={"status": "deleted", "id": _id}

	html_template = template.render(tasks=tasks,message=respuesta)
	return response.html(html_template)

@app.route('/realized/<_id>', methods=["GET"])
async def mark_as_done(request,_id):
	template = Template(txt_template)
	respuesta={}
	if int(_id) >= len(tasks) or int(_id) < 0:
		respuesta={"status":"not found"}
	try:
		if tasks[int(_id)][1]:
			tasks[int(_id)][1]=False
		else:
			tasks[int(_id)][1]=True

	except ValueError:
		respuesta={"status": "id is not valid"}

	if len(respuesta) == 0:
		respuesta={"status": "realized", "id": _id}

	html_template = template.render(tasks=tasks,message=respuesta)
	return response.html(html_template)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
