from survey import AnonymousSurvey

question = 'what language did you first learn to speak ?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('enter q at any time to quit')
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

print('\n thank you to everyone who participated in the survey ~!')
my_survey.show_results()

