from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Test, Answer
from .serializers import AnswerSerializer


class AnswerSubmitAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve the test based on the provided test ID
        test_id = kwargs['test_id']
        test = Test.objects.get(pk=test_id)

        # Get the list of submitted answers
        submitted_answers = serializer.validated_data.get('answers', [])

        # Calculate the number of correct answers
        correct_answers_count = 0
        for submitted_answer in submitted_answers:
            answer_id = submitted_answer.get('id')
            is_true = submitted_answer.get('is_true')

            # Retrieve the corresponding answer from the database
            try:
                answer = Answer.objects.get(pk=answer_id)
            except Answer.DoesNotExist:
                continue

            if answer.is_true == is_true:
                correct_answers_count += 1

        # Calculate the percentage of correct answers
        total_questions_count = test.question.count()
        percentage = (correct_answers_count / total_questions_count) * 100

        # Perform any additional business logic here
        # For example, save the test result to the user's profile

        return Response({'percentage': percentage}, status=status.HTTP_201_CREATED)
