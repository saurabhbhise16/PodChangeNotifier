from flask import Flask, redirect, url_for, render_template
from kubernetes import client, config

app = Flask(__name__)

def main():
	# Configs can be set in Configuration class directly or using helper utility
	config.load_kube_config()

	'''v1 = client.CoreV1Api()
	print("Listing pods with their IPs:")
	ret = v1.list_pod_for_all_namespaces(watch=False)
	for i in ret.items:
		for x in range(5):	 
		 	pods = {'statusPod' : i.status.pod_ip, 'metadata' : i.metadata.namespace, 'name' : i.metadata.name
		 	}	
		 #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))'''


@app.route("/")
def home():
	config.load_kube_config()

	v1 = client.CoreV1Api()
	print("Listing pods with their IPs:")
	ret = v1.list_pod_for_all_namespaces(watch=False)
	podName= []
	
	for i in ret.items:
		podName.extend([[i.status.pod_ip, i.metadata.namespace, i.metadata.name]])
	
			 #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
	return render_template("index.html" ,content = podName)


if __name__ == "__main__":
	app.run(debug = True)

