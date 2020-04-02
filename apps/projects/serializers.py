from rest_framework import serializers

from testcases.models import Testcases
from utils import validates
from .models import Projects
from debugtalks.models import DebugTalks
from interfaces.models import Interfaces


class ProjectsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ('update_time', )  # 更新时间不输入也不输出，直接排除

        extra_kwargs = {
            'create_time': {
                'read_only': True  # 创建时间只输出
            }
        }

    def create(self, validated_data):
        project_obj = super().create(validated_data)
        DebugTalks.objects.create(project=project_obj)
        return project_obj


class ProjectNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')


# class InterfaceNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Interfaces
#         fields = ('id', 'name')


# class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
#     interfaces = InterfaceNameSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Projects
#         fields = ('id', 'interfaces')

class ProjectsRunSerializer(serializers.ModelSerializer):
    """
    运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      validators=[validates.whether_existed_env_id])

    class Meta:
        model = Testcases
        fields = ('id', 'env_id')