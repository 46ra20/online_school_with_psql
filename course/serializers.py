from .models import CourseModel,CourseCategory
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    department=serializers.ReadOnlyField(source='department.category')
    department_id=serializers.ReadOnlyField(source='department.id')
    # user = str(first_name+' '+last_name)
    class Meta:
        model = CourseModel
        # fields=['title','description','assessment_methods','learing_outcomes','course_duration','prerequisites','image','date','price','department','first_name','last_name']
        exclude=('user',)
        
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id','category']



class PostCourseSerializer(serializers.ModelSerializer):
    # user = str(first_name+' '+last_name)
    class Meta:
        model = CourseModel
        fields='__all__'
        # exclude=('user',)