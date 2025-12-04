import smtplib
from email.mime.text import MIMEText
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect
from .models import code_table, user_table  # Import the user_table model

# Create your views here.
from app.models import *


def login(request):
    return render(request, "login.html")



def logout(request):
    auth.logout(request)
    return render(request, "login.html")





def logincode(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        ob1=login_table.objects.get(username=username,password=password)
        if ob1.type=='admin':
            request.session['lid'] = ob1.id
            ob3=auth.authenticate(username='admin',password='admin')
            if ob3 is not None:
                auth.login(request,ob3)
            return HttpResponse('''<script> alert("login success ");window.location="/adminhome" </script>''')
        elif ob1.type=='user':
            ob3 = auth.authenticate(username='admin', password='admin')
            if ob3 is not None:
                auth.login(request, ob3)
            request.session['ccode']="na"
            request.session['lid'] = ob1.id
            obb=user_table.objects.filter(LOGIN=ob1.id)
            request.session['img']=obb[0].photo.url
            request.session['name']=obb[0].name
            return HttpResponse('''<script> alert("login success ");window.location="/userhome" </script>''')
        else:
            return HttpResponse('''<script> alert("No user");window.location="/" </script>''')
    except:
        return HttpResponse('''<script> alert("Invalid Username or Password ");window.location="/" </script>''')

    #elif ob1.type

def registration(request):
    return render(request,"registration.html")



def registration_post(request):
    name=request.POST["n1"]
    email=request.POST["emaill"]
    username=request.POST["usrname"]
    password=request.POST["pwd"]
    age=request.POST["age"]
    gender=request.POST["radio"]
    phone=request.POST["phone"]
    address=request.POST["address"]
    PHOTO=request.FILES["file"]
    fs=FileSystemStorage()
    fn=fs.save(PHOTO.name,PHOTO)

    xx=login_table.objects.filter(username=username)

    if len(xx)>0:
        return HttpResponse('''<script> alert('User name already Exists');window.location='/registration'</script>''')

    else:

        ob=login_table()
        ob.username=username
        ob.password=password
        ob.type="user"
        ob.save()

        ob1=user_table()
        ob1.LOGIN=ob
        ob1.name = name
        ob1.email = email
        ob1.age = age
        ob1.gender = gender
        ob1.phone = phone
        ob1.address = address
        ob1.photo = fn

        ob1.save()
        return HttpResponse('''<script> alert('Account created');window.location='/'</script>''')




def forgot_password_reset(request):
    print(request.POST)
    try:
        print("1")
        print(request.POST)
        email = request.POST['textfield']
        print(email)
        s=user_table.objects.get(email=email)

        print(s, "=============")
        if s is None:
            return HttpResponse('''<script>alert('invalid email');window.location='/forgotpassword'</script>''')

            # return jsonify({'task': 'invalid email'})
        else:
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('sinubaby044@gmail.com', 'yosh sdvy trze yjrk')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Your new password id : " + str(s.LOGIN.password))
            print(msg)
            msg['Subject'] = 'Your password'
            msg['To'] = email
            msg['From'] = 'sinubaby044@gmail.com'

            print("ok====")

            try:
                gmail.send_message(msg)
            except Exception as e:
                return HttpResponse('''<script>alert('invalid email');window.location='/forgotpassword'</script>''')
            return HttpResponse('''<script>alert('sended');window.location='/'</script>''')
    except Exception as e:
        try:
            print("1")
            print(request.POST)
            email = request.POST['textfield']
            print(email)
            s = user_table.objects.get(LOGIN__username=email)
            email=s.email
            # qry = "SELECT login.password FROM student  JOIN login ON login.L_id = student.L_id WHERE email=%s"
            # s = selectone(qry, email)
            print(s, "=============")
            if s is None:
                return HttpResponse('''<script>alert('invalid email');window.location='/forgotpassword'</script>''')

                # return jsonify({'task': 'invalid email'})
            else:
                try:
                    gmail = smtplib.SMTP('smtp.gmail.com', 587)
                    gmail.ehlo()
                    gmail.starttls()
                    gmail.login('sinubaby044@gmail.com', 'yosh sdvy trze yjrk')
                    print("login=======")
                except Exception as e:
                    print("Couldn't setup email!!" + str(e))
                msg = MIMEText("Your new password id : " + str(s.LOGIN.password))
                print(msg)
                msg['Subject'] = 'Your password'
                msg['To'] = email
                msg['From'] = 'sinubaby044@gmail.com'

                print("ok====")

                try:
                    gmail.send_message(msg)
                except Exception as e:
                    return HttpResponse('''<script>alert('invalid email');window.location='/forgotpassword'</script>''')
                return HttpResponse('''<script>alert('sended');window.location='/'</script>''')
        except Exception as e:
            print(e)
            return HttpResponse('''<script>alert('invalid username or email');window.location='/forgotpassword'</script>''')


def forgotpassword(request):
    return render(request,"forgot password.html")

@login_required(login_url='/')
def adminhome(request):
    return render(request,"admin/admin_home.html")


# @login_required(login_url='/')
def userhome(request,):
    # obb = user_table.objects.get(LOGIN=request.session['lid'])
    # print(obb.photo,"hhhhhhhhh")
    # img=request.session['img']
    # name=request.session['name']
    return render(request, "user/index.html")

@login_required(login_url='/')
def exampleprogram(request):
    ob=sample_programs.objects.all().order_by('-id')
    return render(request,"user/Example Program.html",{"val":ob})




@login_required(login_url='/')
def examplesearch1(request):
    exsearch = request.POST['select']
    top = request.POST['exsearch']
    # if exsearch=="":
    #     ob=sample_programs.objects.filter(Q(topic__icontains=top,Language__icontains=exsearch)|Q(Language__icontains=exsearch)).order_by('-id')
    #     return render(request,"user/Example Program.html",{"val":ob,"e":exsearch,"t":top})
    # else:
    ob=sample_programs.objects.filter(topic__icontains=top,Language__icontains=exsearch).order_by('-id')
    return render(request,"user/Example Program.html",{"val":ob,"e":exsearch,"t":top})

@login_required(login_url='/')
def exampleprogramview(request,id):
    ob=sample_programs.objects.get(id=id)
    return render(request,"user/individual example program.html",{"val":ob})


@login_required(login_url='/')
def individual_user(request,id):
    ob = user_table.objects.get(id=id)
    return render(request,"admin/individual_view_block_user.html",{"val":ob})


@login_required(login_url='/')
def viewcode(request):
    ob=code_table.objects.all().order_by('-id')
    return render(request,"admin/view code.html",{"val":ob})


@login_required(login_url='/')
def userviewcode(request):
    ob=code_table.objects.filter(USER__LOGIN__id=request.session['lid']).order_by('-date')
        # .order_by('-time')
    return render(request,"user/user view code.html",{"val":ob})



@login_required(login_url='/')
def viewcodesearch(request):
    name=request.POST['name']
    ob=code_table.objects.filter(USER__name__icontains=name)
    return render(request,"admin/view code.html",{"val":ob})





@login_required(login_url='/')
def sharetofriend(request):
    ob = share_table.objects.filter(FROMUSER__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, "user/share to friend view all.html", {"val": ob})

@login_required(login_url='/')
def sharetofriendsearch(request):
    name = request.POST['name']
    ob = share_table.objects.filter(TOUSER__name__icontains=name,FROMUSER__LOGIN__id=request.session['lid'])
    return render(request, "user/share to friend view all.html", {"val": ob})


@login_required(login_url='/')
def individualuserfriendcodeview(request, id):
    ob = share_table.objects.get(id=id)
    return render(request, "user/individualuserfriendcodeview.html", {"val": ob})



#
# def examplesearch(request):
#     name=request.POST['exsearch']
#     ob=sample_programs.objects.filter(topic__icontains=name)
#     return render(request,"admin/Example Program.html",{"val":ob})




@login_required(login_url='/')
def individualcodeview(request,id):
    ob = code_table.objects.get(id=id)
    return render(request,"admin/individual code view.html",{"val":ob})



@login_required(login_url='/')
def individualusercodeview(request,id):
    ob = code_table.objects.get(id=id)
    request.session['cid']=id
    return render(request,"user/user individual code view.html",{"val":ob})



@login_required(login_url='/')
def vieworblocksearch(request):
    name=request.POST['name']
    ob=user_table.objects.filter(name__startswith=name)
    return render(request,"admin/View or block.html",{"val":ob,"name1":name})








@login_required(login_url='/')
def feedback(request):
    ob = feedback_table.objects.all().order_by('-id')
    return render(request,"admin/view feedback.html",{"val":ob})




@login_required(login_url='/')
def individualfeedbackview(request,id):
    ob = feedback_table.objects.get(id=id)
    return render(request,"user/sendfeedback.html",{"val":ob})





@login_required(login_url='/')
def complaint(request):
    ob = complaint_table.objects.all().order_by('-id')
    return render(request,"admin/view complaint.html",{"val":ob})


@login_required(login_url='/')
def replycomplaint(request,cid):
    request.session["cid"]=cid
    return render(request,"admin/send reply.html")




@login_required(login_url='/')
def replycomplaintdb(request):
    complaint = request.POST['reply']
    ob=complaint_table.objects.get(id=request.session["cid"])
    ob.reply=complaint
    ob.save()
    return HttpResponse('''<script>alert('Replied successfully');window.location='/complaint'</script>''')



from .models import user_table





@login_required(login_url='/')
def vieworblock(request):
    ob = user_table.objects.all().order_by('-id')
    user_ob = []

    for user in ob:
        if user.LOGIN.type == 'user':
            user_ob.append(user)

    return render(request, "admin/View or block.html", {"val": user_ob})


# def vieworblocksearch(request):
#     name=request.POST['name']
#     ob=user_table.objects.filter(name__startswith=name)
#     return render(request,"admin/View or block.html",{"val":ob})




@login_required(login_url='/')
def block_user(request,lid):
    ob1 = login_table.objects.get(id=lid)
    ob1.type="blocked"
    ob1.save()
    return HttpResponse('''<script> alert('Account blocked');window.location='/vieworblock'</script>''')




@login_required(login_url='/')
def unblock_user(request,lid):
    ob1 = login_table.objects.get(id=lid)
    ob1.type="user"
    ob1.save()
    return HttpResponse('''<script> alert('Account unblocked');window.location='/vieworblock'</script>''')


#-------------------------------------user--------------------------



@login_required(login_url='/')
def history(request):
    return render(request, "user/history.html")



@login_required(login_url='/')
def historycode(request):
    return render(request,"user/history code.html")




@login_required(login_url='/')
def sampleprogram(request):
    ob = sample_programs.objects.all().order_by('-id')
    return render(request, "admin/sampleprogram.html", {"val": ob})




@login_required(login_url='/')
def examplesearch(request):
    exsearch = request.POST['exsearch']
    ob = sample_programs.objects.filter(topic__icontains=exsearch).order_by('-id')
    return render(request, "admin/sampleprogram.html", {"val": ob})




@login_required(login_url='/')
def sampleprogramview(request,id):
    ob=sample_programs.objects.get(id=id)
    return render(request,"admin/sampleprogramview.html",{"val":ob})




@login_required(login_url='/')
def addsampleprogram(request):
    return render(request, "admin/addsampleprogram.html")




@login_required(login_url='/')
def addsampleprogram_post(request):
    code = request.POST['examplecode']
    topic = request.POST['topic']
    lang = request.POST['language']
    ob = sample_programs()
    ob.code=code
    ob.Language=lang
    ob.date = datetime.datetime.now().date()
    ob.topic=topic
    ob.save()
    return HttpResponse('''<script>alert('sample program uploaded sucessfully');window.location='/sampleprogram'</script>''')






@login_required(login_url='/')
def usercode_post(request):
    code = request.POST['codee']

    ob = code_table()
    ob.code=code
    ob.USER = user_table.objects.get(LOGIN=request.session["lid"])
    ob.date = datetime.datetime.now().date()
    ob.save()
    return HttpResponse('''<script>alert('feedback sent sucessfully');window.location='/sendfeedback'</script>''')




@login_required(login_url='/')
def usercodesave(request):

    return render(request, "user/savecode.html")





@login_required(login_url='/')
def usercodesave_post(request):
    if request.method == 'POST':
        code = request.POST['examplecode']
        topic = request.POST['topic']
        lang = request.POST['language']

        ob = code_table()
        ob.code = code
        ob.language = lang
        ob.topic = topic
        ob.USER = user_table.objects.get(id=request.session["lid"])  # Fetch the user instance
        ob.date = datetime.datetime.now().date()
        ob.save()
        request.session['code']=""
        return HttpResponse('''<script>alert('Code successfully saved');window.location='/usercodesave'</script>''')
    else:
        return render(request, 'user/usercodesave.html')





@login_required(login_url='/')
def user_program_edit_save(request):
    ob = code_table.objects.get(id=request.session['cid'])
    return render(request, "user/edit user individual saved program.html",{"i":ob})





@login_required(login_url='/')
def user_program_edit_save_post(request):
    if request.method == 'POST':
        code = request.POST['examplecode']
        topic = request.POST['topic']
        lang = request.POST['language']
        # idd=request.session["id"]
        ob = code_table.objects.get(id=request.session['cid'])
        ob.code = code
        ob.language = lang
        ob.topic = topic
        ob.USER = user_table.objects.get(id=request.session["lid"])  # Fetch the user instance
        ob.date = datetime.datetime.now().date()
        ob.save()
        request.session['code']=""
        return HttpResponse('''<script>alert('Code successfully edited');window.location='/userviewcode'</script>''')
    else:
        return render(request, 'user/usercodesave.html')


from django.shortcuts import render, get_object_or_404, redirect

@login_required(login_url='/')
def group_code_edit(request,id):
    request.session['scid']=id
    ob = share_group_table.objects.get(id=id)
    return render(request, "user/group code edit.html", {"i": ob})


@login_required(login_url='/')
def group_code_edit_post(request):
    if request.method == 'POST':
        kk = request.session['gid']
        code = request.POST['examplecode']
        topic = request.POST['topic']
        lang = request.POST['language']

        ob = share_group_table.objects.get(id=request.session['scid'])
        # Update the object's fields
        ob.code = code
        ob.Language = lang
        ob.topic = topic
        ob.date = datetime.datetime.now().date()
        ob.save()

        request.session['code'] = ""
        return HttpResponse(
            f'''<script>alert('Code successfully edited');window.location='/individualgroupview/{kk}'</script>''')

    else:
        return render(request, 'user/usercodesave.html')


@login_required(login_url='/')
def sendfeedback(request):
    ob = feedback_table.objects.filter(USER__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, "user/sendfeedback.html",{"val":ob})



@login_required(login_url='/')
def sendfeedback_post(request):
    feedback = request.POST['feed']
    rating= request.POST['rating']


    ob = feedback_table()
    ob.feedback=feedback
    ob.rating=rating
    ob.USER=user_table.objects.get(LOGIN=request.session["lid"])
    ob.date=datetime.datetime.now().date()
    ob.save()
    return HttpResponse('''<script>alert('feedback sent sucessfully');window.location='/sendfeedback'</script>''')



@login_required(login_url='/')
def replycomplaintuser(request):
    a=complaint_table.objects.filter(USER__LOGIN_id=request.session['lid']).order_by('-id')
    return render(request,"user/send complaint.html",{'data':a})



@login_required(login_url='/')
def send_comp2(request):
    return render(request,"user/send com2.html")




@login_required(login_url='/')
def replycomplaintuser_post(request):
    complaint = request.POST['complaint']
    ob=complaint_table()
    ob.complaint=complaint
    ob.date=datetime.datetime.now().today().date()
    ob.USER = user_table.objects.get(LOGIN_id=request.session["lid"])
    ob.save()
    return HttpResponse('''<script>alert('complainted successfully');window.location='/replycomplaintuser'</script>''')





@login_required(login_url='/')
def group(request):
    user_id = request.session['lid']
    # Fetch the group memberships for the current user
    group_memberships = group_members_table.objects.filter(USER__LOGIN__id=user_id).order_by('-id')
    return render(request, "user/Group.html", {"val": group_memberships})

# def group(request):
#     # kk=group_table.objects.filter(USER__LOGIN__id=request.session['lid']).order_by('-id')
#     kk=group_members_table.objects.filter(USER__LOGIN__id=request.session['lid']).order_by('-id')
#     return render(request,"user/Group.html",{"val":kk})








@login_required(login_url='/')
def individual_share(request):
    kk = user_table.objects.all()
    return render(request, "user/individual share.html", {"val": kk})



@login_required(login_url='/')
def individual_share_post(request):
    if request.method == 'POST':
        language = request.POST['language']
        topic = request.POST['title']
        touser_id = request.POST['touser']  # Ensure this retrieves the correct ID as a string
        code = request.POST['code']

        ob = share_table()
        ob.code = code
        ob.Language = language
        ob.topic = topic
        ob.FROMUSER = user_table.objects.get(id=request.session["lid"])
        try:
            ob.TOUSER = user_table.objects.get(id=int(touser_id))  # Convert touser_id to an integer
        except ValueError:
            return HttpResponse('''<script>alert('Invalid user ID');window.location='/individual_share'</script>''')

        ob.date = datetime.datetime.now().date()
        ob.status = 'Active'
        ob.save()

        request.session['code'] = ""
        return HttpResponse('''<script>alert('Code successfully saved');window.location='/individual_share'</script>''')
    else:
        return render(request, 'user/usercodesave.html')





@login_required(login_url='/')
def usergroupsharelist(request):
    kk = group_members_table.objects.filter(USER__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, "user/group share list.html", {"val":kk})






@login_required(login_url='/')
def usergroupsharelist_post(request):
    if request.method == 'POST':
        language = request.POST['language']
        topic = request.POST['title']
        group_id = request.POST['group']
        status = request.POST['status']
        code = request.POST['code']  # fixed typo: request.post -> request.POST

        ob = share_group_table()
        ob.code = code
        ob.Language = language
        ob.topic = topic
        ob.type=status
        ob.USER = user_table.objects.get(id=request.session["lid"])  # Fetch the user instance
        ob.GROUP = group_table.objects.get(id=group_id)  # Fetch the group instance
        ob.date = datetime.datetime.now().date()  # Add current date
        ob.save()

        request.session['code'] = ""
        return HttpResponse('''<script>alert('Code successfully saved');window.location='/usergroupsharelist'</script>''')
    else:
        return render(request, 'user/usercodesave.html')




@login_required(login_url='/')
def groupview(request):
    ob = group_table.objects.all().order_by('-id')
    return render(request, "user/groupview.html",{"val":ob})



@login_required(login_url='/')
def individualgroupcodeview(request,id):
    ob = share_group_table.objects.get(id=id)
    return render(request,"user/individualgroupcodeview.html",{"val":ob})





@login_required(login_url='/')
def creategroup(request):
    return render(request, "user/create group.html")

@login_required(login_url='/')
def groupcreate(request):
    groupname = request.POST['groupname']
    description= request.POST['description']


    photo = request.FILES["file"]
    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
    fs.save(date,photo)
    path=fs.url(date)



    ob = group_table()
    ob.grpName=groupname
    ob.date=datetime.datetime.now().date()
    ob.Detail=description
    ob.photo=path
    ob.USER=user_table.objects.get(LOGIN__id=request.session["lid"])
    ob.save()

    ob1 = group_members_table()
    ob1.GROUP=ob
    ob1.date=datetime.datetime.now().date()
    ob1.USER=user_table.objects.get(LOGIN__id=request.session["lid"])
    ob1.type= "admingrp"
    ob1.save()
    return HttpResponse('''<script>alert('group created sucessfully');window.location='/group'</script>''')





@login_required(login_url='/')
def managegroupmembers(request,id):
    request.session['grpid'] = id
    kk=group_members_table.objects.filter(GROUP__id=id).order_by('-id')
    return render(request,"user/manage group members.html",{"val":kk,"id":id})




@login_required(login_url='/')
def addgroupmember(request):
    ob=user_table.objects.all()
    return render(request, "user/addmembers.html",{"val":ob})


from .models import group_members_table, user_table, group_table




@login_required(login_url='/')
def addgrpmembercode(request):
    kk = request.session['gid']
    name = request.POST['name']
    description = request.POST['type']

    # Ensure you're checking for the user within the same group
    if group_members_table.objects.filter(GROUP=request.session['grpid'], USER__id=name).exists():
        return HttpResponse(
            f'''<script>alert('Cannot add same member in the group');window.location='/managegroupmembers/{kk}'</script>''')

    ob = group_members_table()
    ob.USER = user_table.objects.get(id=name)
    ob.GROUP = group_table.objects.get(id=request.session['grpid'])
    ob.date = datetime.datetime.now().date()
    ob.type = description
    ob.save()
    return HttpResponse(f'''<script>alert('Member added');window.location='/managegroupmembers/{kk}'</script>''')




@login_required(login_url='/')
def individual_user_group(request,id):
    ob = user_table.objects.get(id=id)
    return render(request,"user/individual_user_group.html",{"val":ob})




@login_required(login_url='/')
def delete_user_group_member (request,id):
    ob = group_members_table.objects.get(id=id)
    ob.delete()
    kk = request.session['gid']
    return HttpResponse(f'''<script>alert('Group member Deleted');window.location='/managegroupmembers/{kk}'</script>''')




@login_required(login_url='/')
def deletesharegroupdata (request,id):
    ob = share_group_table.objects.get(id=id)
    ob.delete()
    kk=request.session['gid']
    return HttpResponse(f'''
               <script>
                   alert('Program Deleted');
                   window.location = '/individualgroupview/{kk}';  // Redirect with session ID (kk)
               </script>
           ''')



@login_required(login_url='/')
def delete_user_group(request, id):
    ob = group_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('group Deleted');window.location='/group'</script>''')

        # ob.GROUP = group_table.objects.get(id=request.session['grpid'])


@login_required(login_url='/')
def share_code_to_group(request):
    return render(request, "user/share code to group.html")





@login_required(login_url='/')
def individualgroupview(request,id):
    request.session['gid']=id

    kk=group_table.objects.get(id=id)
    ob=share_group_table.objects.filter(GROUP__id=id).order_by('-id')
    return render(request, "user/individual group view.html",{"val":kk,"ob":ob})



@login_required(login_url='/')
def share_code_to_group_post(request):
    gid = request.session['gid']
    code = request.POST['examplecode']
    topic = request.POST['topic']
    Language = request.POST['language']
    statu = request.POST['status']
    ob = share_group_table()
    ob.code=code
    ob.type=statu
    ob.Language=Language
    ob.date = datetime.datetime.now().date()
    ob.topic=topic
    ob.USER = user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.GROUP = group_table.objects.get(id=request.session['gid'])
    ob.save()
    return HttpResponse(f'''<script>alert('Program shared ');window.location='/individualgroupview/{gid}'</script>''')


@login_required(login_url='/')
def selfprofileview(request,id):
    ob = user_table.objects.get(id=id)
    return render(request,"user/self profile view.html",{"val":ob})




# ------------------------------   USER COMPILER -------------------------------------


# @login_required(login_url='/')
def user_python(request):
    return render(request, "user/user python.html")


def user_python2(request):
    return render(request, "user/python home.html")


#
# # @login_required(login_url='/')
# def user_python2(request,id):
#     kk=share_group_table.objects.get(id=id)
#     return render(request, "user/python2.html",{"code":kk.code})
#


# @login_required(login_url='/')
def user_java(request):
    return render(request, "user/user java.html")

# @login_required(login_url='/')
# def user_java2(request):
#     kk = share_group_table.objects.get(id=id)
#     return render(request, "user/user java2.html", {"code": kk.code})


@login_required(login_url='/')
def user_c(request):
    return render(request, "user/user C Compiler.html")



@login_required(login_url='/')
def user_cpp(request):
    return render(request, "user/user C++ Compiler.html")



# --------------------------------ADMIN COMPILER -------------------------------------



@login_required(login_url='/')
def admin_python(request):
    return render(request, "admin/admin python.html")



@login_required(login_url='/')
def admin_java(request):
    return render(request, "admin/admin java.html")


@login_required(login_url='/')
def admin_c(request):
    return render(request, "admin/admin C Compiler.html")



@login_required(login_url='/')
def admin_cpp(request):
    return render(request, "admin/admin C++ Compiler.html")




# @login_required(login_url='/')
def setsession(request):

    rr=request.GET['s'].split("\n")
    print(rr,"===============")
    s=""
    res = []

    for i in rr:
        try:
            a = int(i)
        except:
            if i.startswith('\xa0') or i.startswith('%0A%C2%A0%C2%A0%C2%A0%C2%A0') or i.startswith('%3A'):
                i=i.replace("%0A%C2%A0%C2%A0%C2%A0%C2%A0","")
                i=i.replace("\xa0","")
                # i=i.replace("%3A","")
                res[-1] += i
            else:
                res.append(i)

    # k=len(rr)//2
    # if len(rr)%2==1:
    #     k=k+1
    print(res)
    for i in range(0,len(res)):
        s+=res[i]+"\n"

    request.session['code']=s
    return JsonResponse({"task":"ok"})





# @login_required(login_url='/')
def setsession1(request):
    rr=request.GET['s']

    request.session['ccode']=rr
    return JsonResponse({"task":"ok"})




# def setsession2(request):
#     rr = request.GET['s']
#     request.session['ccode'] = rr
#     return JsonResponse({"task": "ok"})
#

