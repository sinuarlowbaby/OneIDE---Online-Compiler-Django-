
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name="login"),
    path('registration', views.registration,name="registration"),
    path('vieworblock', views.vieworblock,name="vieworblock"),
    path('registration_post', views.registration_post,name="registration_post"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('forgot_password_reset', views.forgot_password_reset, name="forgot_password_reset"),
    path('adminhome', views.adminhome,name="adminhome"),
    path('userhome', views.userhome,name="userhome"),
    path('logout',views.logout, name='logout'),



    path('exampleprogram', views.exampleprogram,name="exampleprogram"),
    path('exampleprogramview/<int:id>', views.exampleprogramview, name="exampleprogramview"),

    path('individual_user/<int:id>', views.individual_user,name="individual_user"),
    path('group_view', views.viewcode,name="group_view"),

    path('feedback', views.feedback,name="feedback"),
    path('viewcode', views.viewcode,name="viewcode"),
    path('individualcodeview/<id>',views.individualcodeview,name='individualcodeview'),
    path('viewcodesearch', views.viewcodesearch,name="viewcodesearch"),

    path('complaint', views.complaint, name="complaint"),
    path('replycomplaint/<cid>', views.replycomplaint, name="replycomplaint"),
    path('deletesharegroupdata/<id>', views.deletesharegroupdata, name="deletesharegroupdata"),
    path('replycomplaintdb', views.replycomplaintdb, name="replycomplaintdb"),
    path('examplesearch1', views.examplesearch1, name="examplesearch1"),
    path('vieworblock', views.vieworblock,name="vieworblock"),
    path('block_user/<lid>', views.block_user,name="block_user"),
    path('unblock_user/<lid>', views.unblock_user, name="unblock_user"),
    path('vieworblocksearch', views.vieworblocksearch,name="vieworblocksearch"),
#    path('replyfeedback', views.replyfeedback, name="replyfeedback"),

#--------------------------------------user---------------------
    path('group', views.group,name="group"),
    path('creategroup', views.creategroup, name="creategroup"),
    path('groupcreate', views.groupcreate,name="groupcreate"),
    path('groupview',views.groupview, name="groupview"),
    path('individualgroupcodeview/<int:id>', views.individualgroupcodeview,name="individualgroupcodeview"),
    path('selfprofileview/<int:id>', views.selfprofileview, name="selfprofileview"),

    path('share_code_to_group', views.share_code_to_group, name="share_code_to_group"),
    path('share_code_to_group_post', views.share_code_to_group_post, name="share_code_to_group_post"),
    path('individualgroupview/<int:id>', views.individualgroupview, name="individualgroupview"),

    path('individual_share', views.individual_share, name="individual_share"),
    path('individual_share_post', views.individual_share_post, name="individual_share_post"),
    path('individualuserfriendcodeview/<id>', views.individualuserfriendcodeview, name="individual_share_post"),


    path('sharetofriend', views.sharetofriend, name="sharetofriend"),
    path('sharetofriendsearch', views.sharetofriendsearch, name="sharetofriendsearch"),


    path('history', views.history,name="history"),
    path('historycode', views.historycode,name="historycode"),

    path('sampleprogram', views.sampleprogram, name="sampleprogram"),
    path('addsampleprogram', views.addsampleprogram, name="addsampleprogram"),
    path('sampleprogramview/<id>',views.sampleprogramview, name='sampleprogramview'),
    path('addsampleprogram_post', views.addsampleprogram_post, name='addsampleprogram_post'),

    path('individualusercodeview/<id>', views.individualusercodeview, name='individualusercodeview'),
    path('userviewcode', views.userviewcode, name='userviewcode'),
    path('usergroupsharelist_post', views.usergroupsharelist_post, name='usergroupsharelist_post'),



    path('logincode', views.logincode,name="logincode"),
    path('sendfeedback',views.sendfeedback,name="sendfeedback"),
    path('sendfeedback_post',views.sendfeedback_post,name="sendfeedback"),
    path('usercodesave', views.usercodesave, name="usercodesave"),
    path('usercodesave_post', views.usercodesave_post, name="usercodesave_post"),

    path('user_program_edit_save', views.user_program_edit_save, name="user_program_edit_save"),
    path('user_program_edit_save_post', views.user_program_edit_save_post, name="user_program_edit_save_post"),


    path('group_code_edit/<id>', views.group_code_edit, name="group_code_edit"),
    path('group_code_edit_post', views.group_code_edit_post, name="group_code_edit_post"),



    path('addgroupmember', views.addgroupmember, name="addgroupmember"),
    path('addgrpmembercode', views.addgrpmembercode, name="addgrpmembercode"),
    path('individual_user_group/<id>', views.individual_user_group, name="individual_user_group"),
    path('managegroupmembers/<int:id>', views.managegroupmembers, name="managegroupmembers"),


    path('replycomplaintuser_post',views.replycomplaintuser_post, name="replycomplaintuser_post"),
    path('replycomplaintuser', views.replycomplaintuser, name="replycomplaintuser"),
    path('send_comp2', views.send_comp2, name="send_comp2"),
    path('delete_user_group_member/<int:id>', views.delete_user_group_member, name="delete_user_group_member"),
    path('delete_user_group/<int:id>', views.delete_user_group, name="delete_user_group"),


# ===================USER COMPILER ===================================================

    path('compiler_python', views.user_python, name='user_python'),
    path('compiler_python2', views.user_python2, name='user_python2'),
    path('compiler_java', views.user_java, name='user_java'),
    # path('compiler_java2', views.user_java2, name='user_java'),
    path('compiler_c', views.user_c, name='user_c'),
    path('compiler_cpp', views.user_cpp, name='user_cpp'),
    path('setsession', views.setsession, name='setsession'),
    path('setsession1', views.setsession1, name='setsession'),
    path('usergroupsharelist', views.usergroupsharelist, name='usergroupsharelist'),



# ===================ADMIN  COMPILER ===================================================

    path('admin_python', views.admin_python, name='admin_python'),
    path('admin_java', views.admin_java, name='admin_java'),
    path('admin_c', views.admin_c, name='admin_c'),
    path('admin_cpp', views.admin_cpp, name='admin_cpp'),

]