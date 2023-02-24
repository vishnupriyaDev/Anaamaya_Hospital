from django.urls import path
from . import views
  

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('blog_details/',views.blog_details),
   path('blog/',views.blog),
   path('contact/',views.contact),
   path('doctor_details/',views.doctor_details),
   path('doctor/',views.doctor),
   path('faq/',views.faq),
   path('giving_back/',views.giving_back),
   path('login/',views.login),
   path('mission_vission/',views.mission_vission),
   path('privacy/',views.privacy),
   path('refund_policy/',views.refund_policy),
   path('registration/',views.registration),
   path('service_details/',views.service_details),
   path('service_two/',views.service_two),
   path('service/',views.service),
   path('term_of_service/',views.term_of_service),
   path('timeline/',views.timeline),

##############################################################################################################################

   path('admin_index/',views.admin_index, ),
   path('admin_login/',views.admin_login, ),
   path('admin_register/',views.admin_register, ),
   path('admin_logout/',views.admin_logout),

]