import json

from django.http import Http404, HttpRequest, JsonResponse  # noqa F401
from django.shortcuts import get_object_or_404  # noqa F401
from django.shortcuts import render  # noqa F401
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from issues.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        # fields = "__all__"
        fields = ["id", "title", "body", "junior_id", "senior_id"]


@api_view()
def get_issues(request) -> Response:
    # issues = Issue.objects.create()
    # issues = Issue.objects.update()
    # issues = Issue.objects.get()
    # issues = Issue.objects.delete()
    # issues = Issue.objects.all()
    issues = Issue.objects.all()

    result: list[IssueSerializer] = [
        IssueSerializer(issue).data for issue in issues
    ]  # noqa

    return Response(data=result)
    # return Response(data={"results": results})


@api_view()
def retrieve_issues(request, issue_id: int) -> Response:
    try:
        issues = Issue.objects.get(id=issue_id)
    except Issue.DoesNotExist:
        raise Http404
    return Response(data={"result": IssueSerializer(issues).data})


@api_view(["POST"])
@csrf_exempt
def post_issues(request) -> Response:
    if post_issues(request):
        try:
            payload: dict = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            raise Exception("Request Body is invalid")

        serializer = IssueSerializer(data=payload)
        serializer.is_valid(raise_exception=True)

        issue = Issue.objects.create(**serializer.validated_data)

        return Response(data=IssueSerializer(issue).data)
