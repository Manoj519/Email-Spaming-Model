# Import render from django shortcuts
from django.shortcuts import render

#Import check_email function, cv, model from Email_Spaming_Model.py
from Email_Spaming_Model import check_email,cv,model

# Making prediction function. 
def predict_email(msg):
    # Here msg is going through check_email function.
    email_pre = check_email(msg)
    
    # Then passes through CountVectorizer.
    email_arr = cv.transform(email_pre)
    
    if (email_arr.shape == (0,7274)):
        email_post = ['ham']
    else:
        # Then Predict the email (spam or ham)
        email_post = model.predict(email_arr)
    
    # return the output.
    return email_post[0]


# Making email spaming function. 
def emailhit(request):
    if request.method == 'POST':
        
        # receive input by post function.
        check_msg = request.POST['T1']
        
        #checking output is spam or not.
        if predict_email(check_msg) == 'spam':
            data = 'spam'
            
#           return spam to html file.
            return render(request, 'home.html', {'data': data})
        else:
            data = 'ham'
#           return ham to html file.
            return render(request, 'home.html', {'data': data})
    else:
#       return error if page is not load.
        return render(request, 'home.html', {'data': "Page Loading Fail"})

