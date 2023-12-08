from flask import Flask,request,jsonify,render_template
import cv2
import numpy as np 
import json

app=Flask(__name__)

#----------------------------------DEMO ----------------------------------------------------------------------------------

@app.route('/api_checking/')
def api_checking():
	return 'it will work fine'





#----------------------------------GET METHOD ----------------------------------------------------------------------------------

@app.route('/string_checking',methods=['GET'])
def string_checking():
    input_text=request.args.get("page_number")
    return(input_text)   



@app.route('/video_processing/')
def video_processing():
	cap = cv2.VideoCapture(0) 
	if (cap.isOpened()): 
		while True:
			ret, img = cap.read() 
			cv2.imshow('output', img) 
			if cv2.waitKey(30) & 0xff == ord('q'): 
				break
		cap.release() 
		cv2.destroyAllWindows() 
		pass
	else:
		pass
		return "Alert ! Camera disconnected"

	
#--------------------------------------------------------------------------------------------------------------------------
#----------------------------------POST METHOD ----------------------------------------------------------------------------------

@app.route('/list_operation/',methods=['POST']) ## User give the input string through the API 
def list_operation():

	request_data = json.loads(request.data.decode(), strict=False)
	recordedfile = dict(request_data['recordedfile'])#.strip()
	print(type(recordedfile))
	return recordedfile


@app.route('/string_processing/',methods=['POST']) ## User give the input string through the API 
def string_processing():
    input_string = request.data
    input_string=input_string.decode("utf-8") 
    length=len(input_string)
    return 'Total Number of String:-'+str(length)

@app.route('/other_json_processing/',methods=['POST']) 
def other_json_processing():
    input_json_data=request.json['language']
    return input_json_data


@app.route('/json_processing/',methods=['POST'])
def json_processing():
    request_data = json.loads(request.data.decode(), strict=False)
    language = str(request_data['language']).strip()
    return language+'welcome arunachalam'

@app.route('/text_file_processing/',methods=['POST'])
def text_file_processing():
	
	input_file=request.files['input_file']
	file_name=input_file.filename

	file_open=open(file_name,'r')
	file_read=file_open.read().split('.')
	output={}
	for index,data in enumerate(file_read):
		data=data.strip('\n')
		data=data.strip("")
		output[index]=data
	return jsonify(output)

@app.route('/image_processing/',methods=['POST'])
def image_processing():
	image_file=request.files['image_file']
	file_name=image_file.filename
	read_image=cv2.imread(file_name)
	cv2.imwrite('output.jpg',read_image)
	return "True"
#-------------------------------------------------------------------------------------------------------------------------



if __name__=='__main__':
	app.run(host='0.0.0.0',port=7007,threaded=True,debug=True)
	
