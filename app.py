from flask import Flask, render_template, flash, request, session

import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '789546321452145a'

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/adminlogin")

@app.route("/adminlogin")
def adminlogin():
    return render_template('Adminlogin.html')

@app.route("/ADMINLOGIN", methods=['GET', 'POST'])
def ADMINLOGIN():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('AdminHome.html',data=data)
        else:
            flash("Username or Password is wrong")
            return render_template('Adminlogin.html')

@app.route("/userlogin")
def userlogin():
    return render_template('Userlogin.html')

@app.route("/USERLOGIN", methods=['GET', 'POST'])
def USERLOGIN():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['uname'] = request.form['username']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash("Username or Password is wrong...!")
            return render_template('UserLogin.html')
        else:
            session['mobile'] = data[2]
            session['email'] = data[3]
            session['address'] = data[4]
            session['profile'] = data[7]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where UserName='" + username + "' and Password='" + password + "'")

            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('UserHome.html',data=data)



@app.route("/newuser")
def newuser():
    return render_template('NewUser.html')

@app.route("/NEWUSER", methods=['GET', 'POST'])
def NEWUSER():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['Password']
        file = request.files['file']
        file.save("static/assets/profile/" + file.filename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='1falldetectionreportdb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + name + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','"+ file.filename +"')")
            conn.commit()
            conn.close()
            flash('New User register successfully')
            return render_template('Userlogin.html')
        else:
            flash('Already registered')
            return render_template('NewUser.html')



@app.route("/UserHome")
def UserHome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where UserName='"+ uname +"'")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)



@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/predict")
def predict():
    from pygrabber.dshow_graph import FilterGraph

    graph = FilterGraph()
    devices = graph.get_input_devices()

    # Print without [] and ''
    for device in devices:
        print(device)
    import cv2
    from ultralytics import YOLO
    uname = session['uname']
    profile = session['profile']

    # Load the YOLOv8 model
    model = YOLO('runs/detect/fall/weights/best.pt')
    # Open the video file
    # video_path = "path/to/your/video/file.mp4"
    cap = cv2.VideoCapture(0)
    dd1 = 0

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame, conf=0.4)
            for result in results:
                if result.boxes:
                    box = result.boxes[0]
                    class_id = int(box.cls)
                    object_name = model.names[class_id]
                    print(object_name)

                    if object_name == 'Fall-Detected':
                        dd1 += 1

                    if dd1 == 20:
                        dd1 = 0
                        import winsound

                        filename = 'alert.wav'
                        winsound.PlaySound(filename, winsound.SND_FILENAME)

                        annotated_frame = results[0].plot()

                        import random
                        loginkey = random.randint(1111, 9999)
                        imgg = "static/assets/upload/" + str(loginkey) + ".jpg"

                        cv2.imwrite("alert.jpg", annotated_frame)
                        cv2.imwrite(imgg, annotated_frame)

                        import datetime
                        date = datetime.datetime.now().strftime('%Y-%m-%d')

                        time = datetime.datetime.now().strftime('%H:%M:%S')

                        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                       database='1falldetectionreportdb')
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO reporttb VALUES ('','" + date + "','" + time + "','" + object_name + "','" + str(
                                imgg) + "','"+ uname +"','"+ profile +"','"+ str(device) +"')")
                        conn.commit()
                        conn.close()


                        cv2.imwrite("alert.jpg", annotated_frame)
                        sendmail()
                        sendmsg("8870928999", "Prediction Name:" + object_name)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()


    return UReports()



@app.route("/UReports")
def UReports():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM reporttb where uname='"+ uname +"'")
    data = cur.fetchall()
    return render_template('UReports.html', data=data)


@app.route("/AReports")
def AReports():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1falldetectionreportdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM reporttb")
    data = cur.fetchall()
    return render_template('AReports.html', data=data)



def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")


def sendmail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr =  "sameeahamed1@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = "Fall Detected"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "alert.jpg"
    attachment = open("alert.jpg", "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "kkvz xxke jmeb pcyb")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()





if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
