from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index',views.index,name="index"),
    path('reg',views.reg,name="reg"),
    path('std',views.std,name="std"),
    path('delete/<int:id>',views.delete,name='delete'),
    path('dele/<int:id>',views.dele,name='dele'),
    path('profile/<int:id>/',views.profileview,name='profileview'),
    path('update/<int:id>/',views.update_student,name='update_student'),
    path('stdcourse', views.stdcourse,name="stdcourse"),
    path('courseview', views.courseview),
    path('tablejoin/<int:id>/', views.tablejoin, name='tablejoin'),
    path('edit/<int:id>/', views.edit_course,name='edit_course'),
    path('certification',views.certification),
    path('add_certification',views.add_certification,name='add_certification'),
    path('show_course',views.show_course,name="show_course"),
    path('add_coursetype',views.add_coursetype, name="add_coursetype"),
    path('option_view',views.option_view),
    path('deleaddcourse/<int:id>',views.deleaddcourse,name='deleaddcourse'),
    path('updatecer/<int:id>/',views.update_cer,name='update_cer'), 
    path('deletetype/<int:id>',views.deletetype,name='deletetype'),
    path('updatetype/<int:id>/',views.update_type,name='update_type'), 
    path('show_duration',views.show_duration),
    path('add_duration',views.add_duration, name='add_duration'),
    path('deleteduration/<int:id>',views.deleteduration,name='deleteduration'),
    path('updateduration/<int:id>/',views.update_duration,name='update_duration'), 
    path('batch',views.batch,name='batch'),
    path('',views.log,name='log'),
    path('logout',views.logout,name='logout'),
    path('managesyllabus',views.managesyllabus,name='managesyllabus'), 
    path('added_by/<int:id>/',views.added_by,name='added_by'), 
    path('added_on/<int:id>/',views.added_on,name='added_on'), 
    path('view_syllabus',views.view_syllabus,name='view_syllabus'),
    path('update_syllabus/<int:id>/',views.update_syllabus,name='update_syllabus'), 
    path('delesyllabus/<int:id>',views.delesyllabus,name='delesyllabus'),
    path('viewbatch',views.viewbatch,name='viewbatch'),
    path('update_batch/<int:id>/',views.update_batch,name='update_batch'), 
    path('delebatch/<int:id>/',views.delebatch,name='delebatch'),
    path('application/<int:id>/',views.application,name='application'),
    path('add_category',views.add_category,name="add_category"),
    path('show_category',views.show_category,name="show_category"),
    path('deletecategory/<int:id>/',views.deletecategory,name="deletecategory"),
    path('update_category/<int:id>/',views.update_category,name="update_category"),
    path('application_course/<int:id>/',views.application_course,name='application_course'),
    path('add_instructor',views.add_instructor,name='add_instructor'),
    path('show_instructor',views.show_instructor,name='show_instructor'),
    path('update_instructor/<int:id>/',views.update_instructor,name='update_instructor'), 
    path('delete_instructor/<int:id>',views.delete_instructor,name='delete_instructor'),
    path('popularadd/<int:id>',views.popularadd,name='popularadd'),
    # path('some_view',views.some_view,name='popularsome_viewadd'),
  


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


