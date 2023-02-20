from rest_framework import generics
from .models import Mission, CompletedMission
from .serializers import MissionSerializer, CompletedMissionSerializer

# GET/받아올 Mission 리스트
class MissionList(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

# 미션 세부보기
class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

# 완료한 미션 보기
class CompletedMissionCreate(generics.CreateAPIView):
    queryset = CompletedMission.objects.all()
    serializer_class = CompletedMissionSerializer