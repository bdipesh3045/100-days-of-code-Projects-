from flask import Flask,redirect,url_for,flash,render_template,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from pypdf import PdfWriter

merger = PdfWriter()



app = Flask(__name__,template_folder="templates")
app.config['MAX_CONTENT_LENGTH']=50*1024*1024
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///users.db"
# db=SQLAlchemy(app )

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
ALLOWED_EXTENSIONS = { 'pdf','epub'}


def check(file):   
    if '.' in file and file.rsplit(".",1)[1] in ALLOWED_EXTENSIONS :
        return True
    else:
        return False

@app.route('/uploads/<path:filename>')
def download_file(filename):
    a=(send_from_directory('Store',
                               filename, as_attachment=True))

    return(a)



@app.route("/combinepdf",methods=['GET','POST'])
def combinepdf():
    error=None
    if request.method=='POST':
        files = request.files.getlist('files')
        if escape(files[0].filename) =='':
            flash("NO files selected")
            return render_template("work.html")
        if len(files)==1:
            flash("Select more than one file")    
            return render_template("work.html")
        for file in files:
            if file and check(escape(file.filename)):
                pass
            else:
                flash('Invalid filetype')
                return render_template("work.html")
                
            
        for pdf in files:
            merger.append(pdf)

        merger.write("Store/merged-pdf.pdf")
        merger.close()  
        filename="merged-pdf.pdf"
        return redirect(url_for('download_file',filename=filename))
        
    else:
        return render_template('work.html')




    

if __name__ == "__main__":
    app.run(debug=True) 