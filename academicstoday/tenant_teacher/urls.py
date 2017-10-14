from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from tenant_teacher.views import web_views


urlpatterns = (
    url(r'^teachers$', web_views.master_page, name='at_tenant_teacher_master'),
    # url(r'^dashboard/student$', web_views.student_master_page, name='at_tenant_student_dashboard_master'),
    # url(r'^dashboard/teacher$', web_views.teacher_master_page, name='at_tenant_teacher_dashboard_master'),
)
