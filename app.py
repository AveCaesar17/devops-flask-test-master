from flask import Flask, request
from flask import Flask, Response
#from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
#metrics = PrometheusMetrics(app)

counter = 0
# by_path_counter = metrics.counter(
#     'by_path_counter', 'Request count by request paths',
#     labels={'path': lambda: request.path}
# )
@app.route('/')
#@by_path_counter
def visit():
    global counter
    counter = counter + 1
    result = "Visit number %d\n" % counter
    return Response(result, mimetype='text/plain')
#metrics.info('app_info', 'Application info', version=counter)

@app.route('/metrics')
def metrics():
    global counter
    result = "# TYPE hello_world_counter counter\nhello_world_counter %d\n" % counter
    return Response(result, mimetype='text/plain')

app.run(host='0.0.0.0',port=5000)